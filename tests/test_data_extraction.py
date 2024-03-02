import unittest
import pandas as pd
from datetime import datetime
from scripts.data_extraction import DataExtractor  

class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = DataExtractor()

    def test_read_csv_file(self):
        file_path = "test_data.csv"
        expected_columns = ["col1", "col2", "col3"]
        expected_data = [["data1", "data2", "data3"], ["data4", "data5", "data6"]]
        columns, data = self.extractor.read_csv_file(file_path)
        self.assertEqual(columns, expected_columns)
        self.assertEqual(data, expected_data)

    def test_get_columns_and_rows(self):
        file_path = "test_data.csv"
        expected_columns = ["col1", "col2", "col3"]
        expected_data = ["data1;data2;data3\n", "data4;data5;data6\n"]
        columns, data = self.extractor.get_columns_and_rows(file_path)
        self.assertEqual(columns, expected_columns)
        self.assertEqual(data, expected_data)

    def test_chunk_list(self):
        test_list = [1, 2, 3, 4, 5, 6]
        chunk_size = 2
        expected_chunked_list = [[1, 2], [3, 4], [5, 6]]
        chunked_list = self.extractor.chunk_list(test_list, chunk_size)
        self.assertEqual(chunked_list, expected_chunked_list)

    def test_prepare_data_for_pandas(self):
        columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"]
        all_data = [["data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8"]]
        id_prefix = "prefix"
        expected_trajectory_data = (["col1", "col2", "col3", "col4"], [["prefix_data1", "data2", "data3", "data4"]])
        expected_timed_vehicle_data = (["track_id", "col5", "col6", "col7", "col8"], [["prefix_data1", "data5", "data6", "data7", "data8"]])
        trajectory_data, timed_vehicle_data = self.extractor.prepare_data_for_pandas(columns, all_data, id_prefix)
        self.assertEqual(trajectory_data, expected_trajectory_data)
        self.assertEqual(timed_vehicle_data, expected_timed_vehicle_data)

    def test_extract_data(self):
        file_name = "test_data.csv"
        tr_file_name, vh_file_name = self.extractor.extract_data(file_name, return_json=True)
        self.assertTrue(tr_file_name.endswith("trajectory.json"))
        self.assertTrue(vh_file_name.endswith("vehicle_data.json"))

if __name__ == '__main__':
    unittest.main()
