#!/usr/bin/python2.7

from os import getcwd
from os.path import dirname, realpath
import sqlite3

def base_dir(): return dirname(realpath(__file__))
def data_dir(): return base_dir() + "/raw"
def db_path(): return getcwd() + "/db.sqlite"
def get_db_connection():
    con = sqlite3.connect(db_path())
    con.text_factory = str
    return con

def cols(): return ("zip", "type", "primary_city", "acceptable_cities",
    "unacceptable_cities", "state", "county", "timezone", "area_codes",
    "latitude", "longitude", "world_region", "country", "decommissioned",
    "estimated_population", "notes")

def table_name(): return "zip_codes"

def get_zipcode(com_adj=100):
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT zip FROM {}
    WHERE type="STANDARD" AND estimated_population != 0
    ORDER BY RANDOM() * MIN(estimated_population, {})
    LIMIT 1 ;
    """.format(table_name(), 100000 / com_adj)
    zipcode = cur.execute(sql).fetchone()[0]
    return zipcode

def get_zipcode_by_state(state, com_adj=100):
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT zip FROM {}
    WHERE type="STANDARD" AND state="{}" AND estimated_population != 0
    ORDER BY RANDOM() * MIN(estimated_population, {})
    LIMIT 1 ;
    """.format(table_name(), state, 100000 / com_adj)
    zipcode = cur.execute(sql).fetchone()[0]
    return zipcode

def get_all_zipcodes():
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT DISTINCT(zip) FROM {} ;
    """.format(table_name())
    zips = cur.execute(sql).fetchall()
    return [z[0] for z in zips]

def get_state_from_zipcode(zipcode):
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT state FROM {}
    WHERE zip="{}" ;
    """.format(table_name(), zipcode)
    return cur.execute(sql).fetchone()[0]

def get_city_from_zipcode(zipcode):
    con = get_db_connection()
    cur = con.cursor()
    sql = """
    SELECT primary_city, acceptable_cities, unacceptable_cities FROM {}
    WHERE zip="{}" ;
    """.format(table_name(), zipcode)
    row = cur.execute(sql).fetchone()
    return row[0]
