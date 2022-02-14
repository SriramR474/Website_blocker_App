import sqlite3
from datetime import datetime


def create_password_table():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS password_details (password TEXT)")
    con.commit()
    con.close()

def insert_password(passcode):
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO password_details VALUES(?)",(passcode,))
    con.commit()
    con.close()

def select_password():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM password_details LIMIT 1")
    pass_detail = cur.fetchall()
    con.close()
    return pass_detail



def create_website_table():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS website (id INTEGER PRIMARY KEY,web_address TEXT,end_date TEXT)")
    con.commit()
    con.close()

def insert(web,end_date):
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO website VALUES(NULL,?,?)",(web,end_date))
    con.commit()
    con.close()

def delete(id):
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM website WHERE id=?",(id,))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM website")
    rows = cur.fetchall()
    con.close()
    return rows



def select_website_details():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute("SELECT web_address,end_date FROM website")
    web_detail = cur.fetchall()
    con.close()
    return web_detail


def select_address_id(i):
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute(f"SELECT web_address,id FROM website where end_date = '{i}'")
    details = cur.fetchall()
    con.close()
    return details


def date():
    con = sqlite3.connect("blocksite.db")
    cur = con.cursor()
    cur.execute(f"SELECT end_date FROM website")
    dates = cur.fetchall()
    d = [dates[i][0] for i in range(len(dates))]
    con.close()
    return d



create_website_table()
create_password_table()
