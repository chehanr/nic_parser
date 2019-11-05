# nic_parser

A python library to parse Sri Lankan national identity card numbers.

## Features

- Supports both new and old NIC types.

## Installation

    git clone https://github.com/chehanr/nic_parser.git && cd nic_parser
    python setup.py install

Or

    pip install nic-parser

## Usage

    >>> from nic_parser.parser import Parser
    >>> nic = Parser('952903022V')
    >>> nic.birth_date
    datetime.datetime(1995, 10, 16, 0, 0)
    >>> nic.gender
    <Gender.MALE: 0>
    >>> nic.serial_number
    302
    >>> nic.check_digit
    2
    >>> nic.special_letter
    'V'
    >>> nic.id_type
    <IdType.OLD: 0>
    >>>

## TODO

- ~Add NIC number generation.~
- ...
