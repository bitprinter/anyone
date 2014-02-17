from datetime import datetime
import api

print "Testing birthday generator ..."

birthday = api.get_birthday()
assert datetime.now().year - 25 >= birthday.year
assert datetime.now().year - 75 <= birthday.year

birthday = api.get_birthday(age=21)
assert datetime.now().year - 21 >= birthday.year
assert datetime.now().year - 22 <= birthday.year

birthday = api.get_birthday(min_age=30, max_age=40)
assert datetime.now().year - 30 >= birthday.year
assert datetime.now().year - 40 <= birthday.year

print "Birthday generator OK!"
