import unittest
from generated_code import load_csv, handle_missing_values, convert_data_types, remove_duplicates, data_transformation, save_cleaned_data

class TestFunctions(unittest.TestCase):

    def test_load_csv(self):
        # Mock input
        mock_file_path = "path/to/mock/file.csv"
        mock_data = [["id", "name"], ["1", "John"], ["2", "Jane"]]

        # Assert function call
        self.assertEqual(load_csv(mock_file_path), mock_data)

    def test_handle_missing_values(self):
        # Mock input
        mock_data = [["id", "name"], ["1", "John"], [None, "Jane"]]

        # Assert function call
        self.assertEqual(handle_missing_values(mock_data), [["id", "name"], ["1", "John"], ["1", "Jane"]])

    def test_convert_data_types(self):
        # Mock input
        mock_data = [["id", "age"], ["1", 25], ["2", 30]]

        # Assert function call
        self.assertEqual(convert_data_types(mock_data), [["id", "age"], ["1", "25"], ["2", "30"]])

    def test_remove_duplicates(self):
        # Mock input
        mock_data = [["id", "name"], ["1", "John"], ["1", "John"], ["2", "Jane"]]

        # Assert function call
        self.assertEqual(remove_duplicates(mock_data), [["id", "name"], ["1", "John"], ["2", "Jane"]])

    def test_data_transformation(self):
        # Mock input
        mock_data = [["id", "age"], ["1", 25], ["2", 30]]

        # Assert function call
        self.assertEqual(data_transformation(mock_data), [["id", "age"], ["1", 25.0], ["2", 30.0]])

    def test_save_cleaned_data(self):
        # Mock input
        mock_data = [["id", "name"], ["1", "John"], ["2", "Jane"]]
        mock_file_path = "path/to/mock/file.csv"

        # Assert function call
        self.assertEqual(save_cleaned_data(mock_data, mock_file_path), None)

if __name__ == "__main__":
    unittest.main()