#!/usr/bin/python2.7

import argparse
from random import getrandbits
from textwrap import dedent

import data.birthdays.api as birthdays
import data.namesbystate.api as first_names
import data.surnames.api as last_names
import data.zipcodes.api as zipcodes

MOST_COMMON = 5

class Anyone():
    def __init__(self, **kwargs):
        self.com_adj = self.parse_common(**kwargs)
        self.birthday = self.parse_birthday(**kwargs)
        self.gender = self.parse_gender(**kwargs)
        self.zipcode = self.parse_zipcode(**kwargs)

        self.age = birthdays.get_age_from_birthday(self.birthday)
        self.state = zipcodes.get_state_from_zipcode(self.zipcode)
        self.city = zipcodes.get_city_from_zipcode(self.zipcode)
        self.first_name = first_names.get_name(self.gender, self.birthday.year,
            self.state, com_adj=self.com_adj)
        self.last_name = last_names.get_name(com_adj=self.com_adj)

    def __str__(self):
        template = dedent("""\
        %s %s
        %s, %s %s
        Gender: %s
        Born: %s
        Age: %s""")
        string = template % (self.first_name, self.last_name, self.city,
            self.state, self.zipcode, self.gender, str(self.birthday), self.age)
        return string

    def parse_birthday(self, **kwargs):
        age = kwargs.get('age')
        min_age = kwargs.get('min_age')
        max_age = kwargs.get('max_age')
        return birthdays.get_birthday(age=age, min_age=min_age, max_age=max_age)

    def parse_zipcode(self, **kwargs):
        if kwargs.get('zip'):
            zipcode = kwargs.get('zip')
        elif kwargs.get('state'):
            zipcode = zipcodes.get_zipcode_by_state(kwargs.get('state'))
        else:
            zipcode = zipcodes.get_zipcode(com_adj=self.com_adj)
        return zipcode

    def parse_gender(self, **kwargs):
        if not kwargs.get('male') and not kwargs.get('female'):
            is_male = getrandbits(1)
        else:
            is_male = kwargs.get('male')
        return 'M' if is_male else 'F'

    def parse_common(self, **kwargs):
        commonness = MOST_COMMON - kwargs.get('common')
        return 10**commonness

class HelpFormatter(argparse.HelpFormatter):
    def _metavar_formatter(self, action, default_metavar):
        if action.metavar is not None:
            result = action.metavar
        elif action.choices is not None:
            result = '{%s..%s}' % (min(action.choices), max(action.choices))
        else:
            result = default_metavar

        def format(tuple_size):
            if isinstance(result, tuple):
                return result
            else:
                return (result, ) * tuple_size
        return format

def get_states(): return first_names.get_all_states()
def valid_zipcode(string): return string

def get_parser():
    parser = argparse.ArgumentParser(prog="anyone.py",
        description="Create a random identity.", formatter_class=HelpFormatter)

    parser.add_argument("-a, --age", default=None, type=int, dest="age",
        help="Specify an age, overrides --min-age and --max-age")

    parser.add_argument("--min-age", default=25, type=int, dest="min_age",
        help="Specify a minimum age (default: 25)")

    parser.add_argument("--max-age", default=75, type=int, dest="max_age",
        help="Specify a maximum age (default: 75)")

    location = parser.add_mutually_exclusive_group()

    location.add_argument("-s, --state", default=None, choices=get_states(),
        dest="state", help="Specify a state")

    location.add_argument("-z, --zip-code", default=None, type=valid_zipcode,
        dest="zip", help="Specify a zip-code")

    gender = parser.add_mutually_exclusive_group()

    gender.add_argument("-m, --male", action="store_true", dest="male",
        help="Choose from masculine first names")

    gender.add_argument("-f, --female", action="store_true", dest="female",
        help="Choose from feminine first names")

    parser.add_argument("-c, --common", default=3, type=int,
        choices=range(1, MOST_COMMON + 1), dest="common",
        help="Likelihood of common values (default: 3)")

    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    print Anyone(**vars(args))
