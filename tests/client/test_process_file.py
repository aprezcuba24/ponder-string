from unittest.mock import MagicMock, call, mock_open, patch

from client.main import process_file


def test_process_file():
    read_file_values = ["a", "b", "c"]
    filename_in = "filename_in.txt"
    filename_out = "filename_out.txt"
    mock_s = MagicMock()
    with patch(
        "client.main.socket.socket.__enter__", return_value=mock_s
    ) as mock_socket, patch("client.main.open", mock_open()) as mocked_file, patch(
        "client.main.read_file", return_value=read_file_values
    ):
        mock_s.recv.side_effect = [b"100" for i in read_file_values]
        process_file(filename_in, filename_out)
        mock_socket.assert_called_once()
        mocked_file.assert_called_once_with(filename_out, "w+")
        mock_s.connect.assert_called_once_with(("127.0.0.1", 65432))
        calls = [call(bytes(content, "utf-8")) for content in read_file_values]
        mock_s.send.assert_has_calls(calls)
        calls = [call("100.0\n") for i in read_file_values]
        mocked_file().write.assert_has_calls(calls)
