import glob
import os
import unittest
from pathlib import Path

from html_table_tools.html_table_rotator import reverse_html_table

TESTDATA_DIR = os.path.dirname(__file__)
os.path.join(TESTDATA_DIR, 'testdata.html')


class TestReverseHTMLTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method is called once before all tests
        # Find and delete all *_output.html files
        for file in glob.glob('*_output.html'):
            if os.path.exists(file):
                print(f"Removing {file}")
                os.remove(file)

    def setUp(self):
        # Find and delete all *_output.html files
        # for file in glob.glob('*_output.html'):
        #     if os.path.exists(file):
        #         os.remove(file)
        self.created_files = []

    @classmethod
    def tearDownClass(cls):
        pass
        # for file in glob.glob('*_output.html'):
        #     if os.path.exists(file):
        #         os.remove(file)
        # self.created_files = []
        # Delete the created test files
        # for test_file in self.created_files:
        #     if test_file and os.path.exists(test_file):
        #         print("Teardown: deleting " + test_file)
        #         os.remove(test_file)

    def test_basic(self):
        output_file = os.path.join(TESTDATA_DIR, "basic_test_output.html")
        reverse_html_table(os.path.join(TESTDATA_DIR, "basic_test.html"),
                           "asdf")
        self.created_files.append(output_file)
        # Add assertions to check the output file content

    def test_no_header(self):
        output_file = os.path.join(TESTDATA_DIR, "no_header_test_output.html")
        reverse_html_table(os.path.join(TESTDATA_DIR, "no_header_test.html"),
                           "Data 1", output_file,
                           has_header=False)
        self.created_files.append(output_file)
        # Add assertions to check the output file content

    def test_multiple_tables(self):
        output_file = os.path.join(TESTDATA_DIR,
                                   "multiple_tables_test_output.html")
        with self.assertRaises(SystemExit) as context:
            reverse_html_table(os.path.join(TESTDATA_DIR,
                                            "multiple_tables_test.html"),
                               "Data",
                               output_file)
            self.assertEqual(context.exception.code, 2)
        self.created_files.append(output_file)

    def test_empty_table(self):
        output_file = os.path.join(TESTDATA_DIR, "empty_table_test_output.html")
        reverse_html_table(os.path.join(TESTDATA_DIR,
                                        "empty_table_test.html"), "Header 1",
                           output_file)
        self.created_files.append(output_file)
        # Add assertions to check the output file content

    def test_no_table_found(self):
        output_file = os.path.join(TESTDATA_DIR,
                                   "no_table_found_test_output.html")
        # with self.assertRaises(ValueError):
        with self.assertRaises(SystemExit) as context:
            reverse_html_table(os.path.join(TESTDATA_DIR,
                                            "no_table_found_test.html"),
                               "Table 1",
                               output_file)
            self.assertEqual(context.exception.code, 1)
        self.created_files.append(output_file)

    def test_different_identifier(self):
        output_file = os.path.join(TESTDATA_DIR,
                                   "different_identifier_test_output.html")
        with self.assertRaises(SystemExit) as context:
            reverse_html_table(os.path.join(TESTDATA_DIR,
                                            "different_identifier_test.html"),
                               "Table 2", output_file)
            self.assertEqual(context.exception.code, 1)
        self.created_files.append(output_file)

    def test_jscript(self):
        output_file = Path(os.path.join(TESTDATA_DIR,
                                        "jscript_test_output.html"))
        reverse_html_table(os.path.join(TESTDATA_DIR, "jscript_test.html"),
                           "h1", output_file)
        content=output_file.read_text(encoding="utf-8")
        self.assertIn("comment", content)
        self.assertIn("showMessage", content)

        self.created_files.append(str(output_file.absolute()))

    def test_large_table(self):
        output_file = os.path.join(TESTDATA_DIR,
                                   "large_table_test_output.html")
        reverse_html_table(os.path.join(TESTDATA_DIR,
                                        "large_table_test.html"), "Column 1",
                           output_file)
        self.created_files.append(output_file)
        # Add assertions to check the output file content


if __name__ == "__main__":
    unittest.main()
