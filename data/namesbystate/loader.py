#!/usr/bin/python2.7

"""
Load data for common first names, grouped by state and year.
"""

from os import listdir
from os.path import isfile, join
import csv

import api

def get_rows_from_file(f):
    with open(f, 'rb') as fin:
        cols = api.cols()
        reader = csv.DictReader(fin, fieldnames=cols)
        return [ [i[col] for col in cols] for i in reader]

def drop_table(con):
    cur = con.cursor()
    sql = """
    DROP TABLE IF EXISTS {} ;
    """.format(api.table_name())
    print sql
    cur.execute(sql)
    con.commit()

def make_table(con):
    cur = con.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS {} (
        state TEXT,
        sex TEXT,
        year INTEGER,
        name TEXT,
        count INTEGER
    ) ;
    """.format(api.table_name())
    print sql
    cur.execute(sql)
    con.commit()

def process_file(f, con):
    cur = con.cursor()
    sql = """
    INSERT INTO {} {}
    VALUES (?, ?, ?, ?, ?) ;
    """.format(api.table_name(), api.cols())
    print sql
    cur.executemany(sql, get_rows_from_file(f))
    con.commit()

def load_file(p, con):
    if isfile(p):
        print "Processing file %s ..." % p
        process_file(p, con)

def load_files(con):
    data_dir = api.data_dir()
    for f in listdir(data_dir):
        load_file(join(data_dir, f), con)
    con.close()

def run():
    con = api.get_db_connection()
    print "Dropping old table if it exists ..."
    drop_table(con)
    print "Making new table ..."
    make_table(con)
    print "Populating table from raw data ..."
    load_files(con)
