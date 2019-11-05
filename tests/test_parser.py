import unittest
from datetime import datetime

from nic_parser.parser import Gender, IdType, Parser


class TestParser(unittest.TestCase):
    def test_is_bad_match(self):
        with self.assertRaises(ValueError):
            Parser('INVALID')

    def test_birth_year(self):
        nics = {
            '952903022V': 1995,
            '199602235437': 1996,
        }

        for key, value in nics.items():
            self.assertEqual(Parser(key).birth_year, value)

    def test_birth_date(self):
        nics = {
            '952903022V': datetime(1995, 10, 16, 0, 0),
            '199602235437': datetime(1996, 1, 21, 0, 0),
        }

        for key, value in nics.items():
            self.assertEqual(Parser(key).birth_date, value)

    def test_gender(self):
        nics = {
            '952903022V': (0, 'MALE'),
            '957903022V': (1, 'FEMALE'),
            '199602235437': (0, 'MALE'),
            '199652235437': (1, 'FEMALE'),
        }

        for key, value in nics.items():
            # Test values.
            self.assertEqual(Parser(key).gender.value, value[0])
            # Test names.
            self.assertEqual(Parser(key).gender.name, value[1])

    def test_serial_number(self):
        nics = {
            '952903022V': 302,
            '199602235437': 3543,
        }

        for key, value in nics.items():
            self.assertEqual(Parser(key).serial_number, value)

    def test_check_digit(self):
        nics = {
            '952903022V': 2,
            '199602235437': 7,
        }

        for key, value in nics.items():
            self.assertEqual(Parser(key).check_digit, value)

    def test_special_letter(self):
        nics = {
            '952903022V': 'V',
            '199602235437': None,
        }

        for key, value in nics.items():
            self.assertEqual(Parser(key).special_letter, value)

    def test_id_type(self):
        nics = {
            '952903022V': (0, 'OLD'),
            '199602235437': (1, 'NEW'),
        }

        for key, value in nics.items():
            # Test values.
            self.assertEqual(Parser(key).id_type.value, value[0])
            # Test names.
            self.assertEqual(Parser(key).id_type.name, value[1])


if __name__ == '__main__':
    unittest.main()
