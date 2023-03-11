import unittest
from unittest.mock import call, mock_open, patch

from app.main import write_file


def test_write_file():
    content = "AAA"
    fake_file_path = "temp.txt"
    with patch("app.main.open", mock_open()) as mocked_file, patch(
        "app.main.get_random_string", return_value=content
    ):
        write_file(fake_file_path, 10)
        mocked_file.assert_called_once_with(fake_file_path, "w+")
        calls = [call(f"{content}\n") for i in range(0, 10)]
        mocked_file().write.assert_has_calls(calls, any_order=True)
