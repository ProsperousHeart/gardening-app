import unittest
import sqlite3
from unittest import mock
from src.main import create_database

class TestCreateDatabase(unittest.TestCase):
    def test_create_database(self):
        # Create a temporary in-memory database for testing
        conn = sqlite3.connect(':memory:')
        path_to_db = ':memory:'

        # Call the create_database function
        create_database(path_to_db)

        # Check if the required tables are created
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]

        self.assertIn('plants', table_names)
        # Add more assertions for other tables

        # Close the connection
        conn.close()

    def test_create_database_with_mock(self):
        # Create a mock connection object
        mock_conn = mock.Mock()

        # Call the create_database function with the mock connection
        create_database(mock_conn)

        # Check if the required tables are created
        mock_conn.cursor.assert_called()
        mock_conn.cursor.return_value.execute.assert_called_with("SELECT name FROM sqlite_master WHERE type='table'")

if __name__ == '__main__':
    unittest.main()
