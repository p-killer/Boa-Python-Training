"""
Sqlite is lite weight version of Mysql.

Sqlite  allows to create database without server 
so no username/pwd

sqlite database is a single file to perform CRUD operations
to manage data

No Undo here. So take backup before deleting data points (Records)

# Note : No UNDO in sqlite
#      : will not support concurrent update by millions of users
#      : No server, No transactions . It is light weight

Why?
Pulling data as per requirement for data visualization and data analysis
Database contains tables which contains data

Open browser and open google , visit  https://sqlitebrowser.org
click download  64bt for windows  and install it
"""

# working with Sqlite 3.0 in Python
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('mystuff.db')

def open_connection():
    ''' Open connection to mystuff.db'''    
    c = conn.cursor()  #open cursor to perform CRUD operations
    return c

def close_connection():
    ''' close connection on database'''
    conn.close()

def create_table(c):
    ''' create_table() used for creating new stuffPlot in mystuff.db'''

    # type all capitails for sqlite commands
    # Data types in Sqlite   - REAL  , TEXT, BLOB , INT ..
    c.execute('CREATE TABLE IF NOT EXISTS stuffPlot (unix REAL, datestamp TEXT, keyword TEXT,value REAL)')
    print("stuffplot table created successfully")

def data_entry(c):
    ''' To insert new static record in stuffPlot table'''

    c.execute("INSERT INTO stuffPlot VALUES (132323,'5-07-2018','Python', 5)")
    conn.commit()   # save record

  

def read_from_db(c):
    '''Reading records from database'''

    c.execute("SELECT * FROM stuffPlot")
    data=c.fetchall();
    print(50 * '-')
    print(data)
    print("No. of records : "+str(len(data)))
  
def dynamic_data_entry(c):
    ''' Dynamically inserting record'''

    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%D %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffPlot 
    (unix,datestamp,keyword,value) VALUES (?,?,?,?)", (unix, date, keyword, value))
    conn.commit() 
    print("Dyanmic data successfull")


def del_and_update(c):
    ''' Update and delete records'''

    c.execute('SELECT * FROM stuffPlot')
    [print(row) for row in c.fetchall()]

    print("Updating the records")
    c.execute('UPDATE stuffPlot SET value=99 WHERE value=3')
    conn.commit()
    # After update let us check
    print(50 * '-')
    c.execute("SELECT * FROM stuffPlot")
    [print(row) for row in c.fetchall()]
    print(50 * '-')

    print("Now deleting records ")
    c.execute('DELETE  FROM stuffPlot WHERE value = 99')
    conn.commit()
    print(50 * '=')
    c.execute("SELECT * FROM stuffPlot")
    [print(row) for row in c.fetchall()]
    print(50 * '-')





"""
Open browser and open google , visit  https://sqlitebrowser.org
click download  64bt for windows  and install it

What is sqlite browser:

DB Browser for SQLite is a high quality, visual, open source tool to create, design,
 and edit database files compatible with SQLite.

It is for users and developers wanting to create databases, search, and edit data.
 It uses a familiar spreadsheet-like interface, and you don't need to learn complicated SQL commands.

Controls and wizards are available for users to:

- Create and compact database files
- Create, define, modify and delete tables
- Create, define and delete indexes
- Browse, edit, add and delete records
- Search records
- Import and export records as text
- Import and export tables from/to CSV files
- Import and export databases from/to SQL dump files
- Issue SQL queries and inspect the results
- Examine a log of all SQL commands issued by the application

Try opening database from sqlite browser and 
perform CRUD on stuffPlot table
"""

