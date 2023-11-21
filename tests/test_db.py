import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from dsdatabase.db import DSDatabase


class MockRowProxy:
    def __init__(self, row_data, column_names):
        self._row_data = row_data
        self._column_names = column_names

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._row_data[key]
        elif isinstance(key, str):
            return self._row_data[self._column_names.index(key)]


class TestDSDatabase(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.db = DSDatabase(dbname="sjbrande_ngl_db")
        self.db.engine.connect = MagicMock(return_value=self.mock_connection)

    @patch("pandas.read_sql_query")
    def test_read_sql_returns_dataframe(self, mock_read_sql_query):
        sql = "SELECT * FROM table"
        mock_df = pd.DataFrame([{"id": 1, "name": "Test"}])
        mock_read_sql_query.return_value = mock_df
        result = self.db.read_sql(sql)
        self.assertIsInstance(result, pd.DataFrame)
        pd.testing.assert_frame_equal(result, mock_df)


if __name__ == "__main__":
    unittest.main()
