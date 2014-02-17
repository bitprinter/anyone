#!/usr/bin/python2.7

from os import getcwd
from os.path import dirname, realpath
import sqlite3

def base_dir(): return dirname(realpath(__file__))
def data_dir(): return base_dir() + "/raw"
def db_path(): return getcwd() + "/db.sqlite"
def get_db_connection(): return sqlite3.connect(db_path())

def cols(): return ("name", "rank", "count", "prop100k", "cum_prop100k",
    "pctwhite", "pctblack", "pctapi", "pctaian", "pct2prace", "pcthispanic")
def table_name(): return "last_names"

def get_name(com_adj=100):
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT name FROM {}
    ORDER BY RANDOM() * count * MIN(rank, {})
    LIMIT 1 ;
    """.format(table_name(), com_adj)
    name = cur.execute(sql).fetchone()[0]
    return name.title()
