import api

print "Testing zipcode generator ..."

con = api.get_db_connection()
cur = con.cursor()
table_name = api.table_name()

print "Testing table `%s` ..." % table_name

# Test table has 42522 rows
test_row_count = """
SELECT COUNT(*) FROM {} ;
""".format(table_name)
count = cur.execute(test_row_count).fetchone()[0]
assert count == 42522

# Test table has mappings to states
test_states_map = """
SELECT COUNT(*) FROM {}
WHERE state='NY' AND type='STANDARD' ;
""".format(table_name)
count = cur.execute(test_states_map).fetchone()[0]
assert count == 1667

test_city_timezone = """
SELECT DISTINCT(timezone) from {}
WHERE primary_city="New York" AND state="NY" ;
""".format(table_name)
query = cur.execute(test_city_timezone).fetchall()
assert len(query) == 2
assert query[0][0] == "America/New_York"

print "Sample zipcode: %s" % api.get_zipcode()

print "Zipcode generator OK!"
