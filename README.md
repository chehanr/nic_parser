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

    >>> from nic_parser import NICParser
    >>> nic = NICParser('952903022V')
    >>> nic.birth_date
    datetime.datetime(1995, 10, 16, 0, 0)
    >>> nic.gender
    'M'
    >>> nic.serial_number
    302
    >>> nic.check_digit
    2
    >>> nic.special_letter
    'V'
    >>> nic.id_type
    'Old'
    >>>

## TODO

- Add NIC number generation.
- ...