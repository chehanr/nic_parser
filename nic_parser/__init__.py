
"""A python library to parse Sri Lankan national identity card numbers (by chehanr)."""

import re
from datetime import datetime
from string import ascii_letters


class NICParser:
    """Parsing NIC numbers.

    :param nic_number: [str] NIC number.
    """

    def __init__(self, nic_number):
        self.__nic_number = nic_number
        self.__old_nic_pattern = r'^(\d{2})(\d{3})(\d{3})(\d{1})(\w)$'
        self.__new_nic_pattern = r'^(\d{4})(\d{3})(\d{4})(\d{1})$'
        self.__match()

    def __match(self):
        old_nic_matches = re.search(self.__old_nic_pattern, self.__nic_number)
        new_nic_matches = re.search(self.__new_nic_pattern, self.__nic_number)

        if old_nic_matches is not None:
            self.__matches = old_nic_matches
            self.__match_type = 0
        elif new_nic_matches is not None:
            self.__matches = new_nic_matches
            self.__match_type = 1
        else:
            raise AttributeError('No matches.')

    def __get_special_letter(self, matches, nic_type):
        if nic_type == 0:
            match = matches.group(5)
            if match not in ascii_letters:
                match = None
        elif nic_type == 1:
            match = None

        return match

    def __get_check_digit(self, matches):
        match = int(matches.group(4))

        return match

    def __get_serial_number(self, matches):
        match = int(matches.group(3))

        return match

    def __get_gender(self, matches):
        match = int(matches.group(2))
        if match > 500:
            gender = 'F'
        else:
            gender = 'M'

        return gender

    def __get_birth_date(self, matches, year):
        try:
            match = int(matches.group(2)) - 1
            if match > 500:
                match -= 500

            _str = '{0},{1}'.format(match, year)
            date_time = datetime.strptime(_str, '%j,%Y')
        except ValueError:
            raise ValueError('Birth date not within range.')

        return date_time

    def __get_birth_year(self, matches, nic_type):
        if nic_type == 0:
            match = matches.group(1)
            year = '19{}'.format(match)
        elif nic_type == 1:
            match = matches.group(1)
            year = match

        return int(year)

    @property
    def birth_year(self):
        """
        :return: [int] Birth year.
        """

        year = self.__get_birth_year(self.__matches, self.__match_type)

        return year

    @property
    def birth_date(self):
        """
        :return: [datetime.datetime] Birth date.
        """

        date_time = self.__get_birth_date(self.__matches, self.birth_year)

        return date_time

    @property
    def gender(self):
        """
        :return: [str] Gender type (`M`/ `F`).
        """

        gender = self.__get_gender(self.__matches)

        return gender

    @property
    def serial_number(self):
        """
        :return: [int] Serial Number.
        """

        serial_number = self. __get_serial_number(self.__matches)

        return serial_number

    @property
    def check_digit(self):
        """
        :return: [int] Check Digit.
        """

        check_digit = self.__get_check_digit(self.__matches)

        return check_digit

    @property
    def special_letter(self):
        """
        :return: [str] Special Letter.
        """

        special_letter = self.__get_special_letter(
            self.__matches, self.__match_type)

        return special_letter

    @property
    def id_type(self):
        """
        :return: [str] ID type (`Old`/ `New`).
        """

        if self.__match_type == 0:
            id_type = 'Old'
        elif self.__match_type == 1:
            id_type = 'New'

        return id_type
