from unittest.mock import mock_open, patch

from client.main import read_file


def test_read_file():
    values = ["a", "b", "c"]
    file_content_mock = "\n".join(values)
    fake_file_path = "file/path/mock"
    with patch(
        "client.main.open", new=mock_open(read_data=file_content_mock)
    ) as mocked_file:
        for k, value in enumerate(read_file(fake_file_path), start=0):
            assert values[k] == value
        mocked_file.assert_called_once_with(fake_file_path, "r")
