"""
Unit tests for the tmp module.

This test suite verifies the behavior of functions in src/tmp.py, including:
- Logging with a test-specific logger to ensure test logs do not interfere with
    production logs.
- Functionality of str_func and print_hi, including correct output and error handling.
- Use of logger-injecting decorator factories for flexible and isolated logging
    during tests.

Tested with unittest and compatible with pytest.
"""

# import pytest
import unittest
from unittest.mock import patch
from io import StringIO

# from src.tmp import print_hi, str_func
from src.utils.logger import create_logger, func_wrapper


test_logger = create_logger(file_name="Test_File_Test", file_mode="w")
# src.tmp.my_function = func_wrapper(test_logger)(src.tmp.func_wrapper.__wrapped__)

# def test_print_hi(capsys):
#     print_hi()
#     captured = capsys.readouterr()
#     assert captured.out == "Hi\n"


class TestTmp(unittest.TestCase):
    """Test cases for the tmp module."""

    def setUp(self):
        """Set up the test environment."""
        # # # return super().setUp()
        # # self.logger = create_logger(file_name="Test_File_Test", file_mode="w")
        # # src.tmp.logger = self.logger  # Patch the module-level logger in src.tmp
        # # # pass
        # self.func_wrapper=func_wrapper(test_logger)(src.tmp.func_wrapper.__wrapped__)
        # Decorate the undecorated functions with the test logger for isolated logging
        import src.tmp

        self.decorated_print_hi = func_wrapper(test_logger)(
            src.tmp.print_hi.__wrapped__
        )
        self.decorated_str_func = func_wrapper(test_logger)(
            src.tmp.str_func.__wrapped__
        )

    def tearDown(self):
        # return super().tearDown()
        pass

    def test_print_hi(self):
        """Test print_hi function."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            # print_hi()
            # print_hi.__wrapped__()
            self.decorated_print_hi()
            self.assertEqual(fake_out.getvalue(), "Hi\n")

    def test_str_func_valid(self):
        """Test str_func with a valid string input."""
        # resp = str_func("test")
        # resp = str_func.__wrapped__("test")
        resp = self.decorated_str_func("test")
        self.assertEqual(resp, "You sent:  test")

    def test_str_func_none(self):
        """Test str_func with None input."""
        with self.assertRaises(TypeError):
            # str_func(None)
            # str_func.__wrapped__(None)
            self.decorated_str_func(None)


if __name__ == "__main__":
    unittest.main()
