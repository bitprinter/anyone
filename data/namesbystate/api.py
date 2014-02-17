#!/usr/bin/python2.7

from os import getcwd
from os.path import dirname, realpath
import sqlite3

def base_dir(): return dirname(realpath(__file__))
def data_dir(): return base_dir() + "/raw"
def db_path(): return getcwd() + "/db.sqlite"
def get_db_connection(): return sqlite3.connect(db_path())

def cols(): return ("state", "sex", "year", "name", "count")
def table_name(): return "first_names"

def get_name(sex, year, state, com_adj=100):
    # Constrain year to be within range of data
    year = min(year, 2012)
    year = max(year, 1910)

    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT name FROM {}
    WHERE sex='{}' AND year={} AND STATE='{}'
    ORDER BY RANDOM() * MIN(count, {})
    LIMIT 1 ;
    """.format(table_name(), sex, year, state, 10000 / com_adj)
    name = cur.execute(sql).fetchone()[0]
    return name

def get_all_states():
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT DISTINCT(state) from {}
    WHERE year=2012 and sex="M"
    ORDER BY state
    """.format(table_name())
    states = cur.execute(sql).fetchall()
    return [str(s[0]) for s in states]

