import unittest

from strom.data_puller.context import *


class TestDirectoryContext(unittest.TestCase):
    def setUp(self):
        self.path = "/garden/path/"
        self.file_type = "csv"
        self.mapping_list = [(0,["timestamp"])]
        self.fake_template = {"fake":"template"}
        self.dc = DirectoryContext(self.path, self.file_type, self.mapping_list, self.fake_template)

    def test_init(self):
        self.assertEqual(self.path, self.dc["dir"])
        self.assertEqual(self.file_type, self.dc["file_type"])
        self.assertEqual(self.mapping_list, self.dc["mapping_list"])
        self.assertEqual(self.fake_template, self.dc["template"])

    def test_add_file(self):
        fake_file = "nail_file"
        self.dc.add_file(fake_file)
        self.assertEqual(1, len(self.dc["unread_files"]))
        self.assertIn(fake_file, self.dc["unread_files"])

    def test_set_header_len(self):
        head_len = 13
        self.dc.set_header_len(head_len)
        self.assertEqual(head_len, self.dc["header_lines"])

    def test_set_delimiter(self):
        delim = "^"
        self.dc.set_delimiter(delim)
        self.assertEqual(delim, self.dc["delimiter"])

    def test_read_one(self):
        fake_file = "nail_file"
        faker_file = "toenail_file"
        self.dc.add_file(fake_file)
        self.dc.add_file(faker_file)
        popped = self.dc.read_one()
        self.assertEqual(popped, faker_file)
        self.assertEqual(1, len(self.dc["unread_files"]))
        self.assertEqual(1, len(self.dc["read_files"]))
