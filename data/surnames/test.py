import api

print "Testing surname generator ..."
con = api.get_db_connection()
cur = con.cursor()
table_name = api.table_name()

print "Testing table `%s` ..." % table_name

# Test table has 151671 rows
test_row_count = """
SELECT COUNT(*) FROM {} ;
""".format(table_name)
count = cur.execute(test_row_count).fetchone()[0]
assert count == 151671

print "Sample surname: %s" % api.get_name()

print "Surname generator OK!"
