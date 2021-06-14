import unittest
from solution import JsonValidator
import json
import os

class TestJsonValidator(unittest.TestCase):
    def setUp(self):
        self.validator = JsonValidator()

    def tearDown(self):
        os.remove('/tmp/test-file.json')

    def test_valid_records(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'2', 'address':'2',  'zip':'00002', 'id': 2},
            {'name':'3', 'address':'3',  'zip':'00003', 'id': 3}
        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(len(ids) == 0)

    def test_null_empty_missing_name(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'', 'address':'2',  'zip':'00002', 'id': 2},
            {'name': None, 'address':'3',  'zip':'00003', 'id': 3},
            {'address':'4',  'zip':'00004', 'id': 4}
        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(sorted(ids) == [2, 3, 4])

    def test_null_empty_missing_address(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'2', 'address':'',  'zip':'00002', 'id': 2},
            {'name': '3', 'address':None,  'zip':'00003', 'id': 3},
            {'name': '4',  'zip':'00004', 'id': 4}
        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(sorted(ids) == [2, 3, 4])

    def test_null_empty_missing_zipcode(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'2', 'address':'2',  'zip':'', 'id': 2},
            {'name': '3', 'address': '3',  'zip':None, 'id': 3},
            {'name': '4', 'address': '4', 'id': 4}
        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(sorted(ids) == [2, 3, 4])

    def test_invalid_zipcode(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'2', 'address':'2',  'zip':'12345-6789', 'id': 2},
            {'name': '3', 'address': '3',  'zip':'123456789', 'id': 3},
            {'name': '4', 'address': '4',  'zip':'12', 'id': 4},
            {'name': '5', 'address': '5',  'zip':'1a234', 'id': 5},
            {'name': '6', 'address': '6',  'zip':'acbdea', 'id': 6},
            {'name': '7', 'address': '7',  'zip':'1231243423434143', 'id': 7}
        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(sorted(ids) == [4, 5, 6, 7])


    def test_invalid_duplicates(self):
        test_data = [
            {'name':'1', 'address':'1',  'zip':'00000', 'id': 1},
            {'name':'2', 'address':'2',  'zip':'12345-6789', 'id': 2},
            {'name': '3', 'address': '3',  'zip':'123456789', 'id': 3},
            {'name': '3', 'address': '3',  'zip':'123456789', 'id': 4},
            {'name': '3', 'address': '3',  'zip':'123456789', 'id': 5},
            {'name':'2', 'address':'2',  'zip':'12345-6789', 'id': 6}

        ]
        test_file = '/tmp/test-file.json' # test is *nix only, sorry!
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        ids = self.validator.validate_file(test_file)
        self.assertTrue(sorted(ids) == [2, 3, 4, 5, 6])
