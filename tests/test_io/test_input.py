import unittest

import pandas

from app.io import input


class TestInputMethods(unittest.TestCase):
    def test_read_from_file_builtin_reads_file(self):
        expected = "test is successful!"
        actual = input.read_from_file_builtin("../../data/test_file.txt")
        self.assertEqual(expected, actual)

    def test_read_from_file_builtin_reads_blank_file(self):
        expected = ""
        actual = input.read_from_file_builtin("../../data/blank_file.txt")
        self.assertEqual(expected, actual)

    def test_read_from_file_builtin_raises_exception_if_file_doesnt_exist(self):
        with self.assertRaises(FileNotFoundError):
            input.read_from_file_builtin("non existent file")

    def test_read_from_csv_file_pandas_reads_file(self):
        expected = """   test   was   successful
0  1111   222   3333333333"""
        actual = input.read_from_csv_file_pandas("../../data/test_file.csv")
        self.assertEqual(expected, actual)

    def test_read_from_csv_file_pandas_raises_exception_if_file_is_blank(self):
        with self.assertRaises(pandas.errors.EmptyDataError):
            input.read_from_csv_file_pandas("../../data/blank_file.csv")

    def test_read_from_csv_file_pandas_raises_exception_if_file_doesnt_exist(self):
        with self.assertRaises(FileNotFoundError):
            input.read_from_csv_file_pandas("non existent file")


if __name__ == '__main__':
    unittest.main()
