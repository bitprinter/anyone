import api

print "Testing first name generator ..."

con = api.get_db_connection()
cur = con.cursor()
table_name = api.table_name()

print "Testing table `%s` ..." % table_name

# Test table has 5459281 rows
test_row_count = """
SELECT COUNT(*) FROM {} ;
""".format(table_name)
count = cur.execute(test_row_count).fetchone()[0]
assert count == 5459281

# Test table has no data from 2013
test_2013_data = """
SELECT COUNT(*) FROM {}
WHERE year='2013' ;
""".format(table_name)
count = cur.execute(test_2013_data).fetchone()[0]
assert count == 0

# Test table has data from 2012
test_2012_data = """
SELECT COUNT(*) FROM {}
WHERE year='2012' ;
""".format(table_name)
count = cur.execute(test_2012_data).fetchone()[0]
assert count == 92625

# Test table has data from 1910
test_1910_data = """
SELECT COUNT(*) FROM {}
WHERE year='1910' ;
""".format(table_name)
count = cur.execute(test_1910_data).fetchone()[0]
assert count == 16830

# Test table has fewer rows from 1910 when only querying women
test_1910_female_data = """
SELECT COUNT(*) FROM {}
WHERE year='1910' AND sex='F' ;
""".format(table_name)
count = cur.execute(test_1910_female_data).fetchone()[0]
assert count == 10637

# Test most popular boys name in New York in 2000
test_2012_pop_male_names = """
SELECT name, MAX(count) FROM {}
WHERE year='2012' AND sex='M' AND state='NY'
ORDER BY count ;
""".format(table_name)
name = cur.execute(test_2012_pop_male_names).fetchone()
assert name[0] == 'Michael' and name[1] == 1384

# Test most popular girls name in California in 1960
test_1960_pop_female_names = """
SELECT name, MAX(count) FROM {}
WHERE year='1960' AND sex='F' AND state='CA'
ORDER BY count ;
""".format(table_name)
name = cur.execute(test_1960_pop_female_names).fetchone()
assert name[0] == 'Karen' and name[1] == 3168

print "Sample first name: %s" % api.get_name('F', 1990, 'VA')

print "First name generator OK!"
