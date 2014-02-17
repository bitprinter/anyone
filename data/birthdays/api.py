#!/usr/bin/python2.7

import random
from datetime import date, datetime, timedelta
random.seed()

def get_year_from_age(today, age):
    delta = today - timedelta(days=365*age)
    return delta.date()

def get_birthday(age=None, min_age=25, max_age=75):
    now = datetime.now()
    if age is not None:
        max_age = age + 1
        min_age = age
    assert max_age > min_age, "Minimum age must not be greater than the maximum"
    start_date = get_year_from_age(now, max_age)
    end_date = get_year_from_age(now, min_age)
    rand_ordinal = random.randrange(start_date.toordinal(), end_date.toordinal())
    return date.fromordinal(rand_ordinal)

def get_age_from_birthday(birthday):
    delta = date.today() - birthday
    return delta.days / 365
