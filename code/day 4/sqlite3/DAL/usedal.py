# import the DAL   - BAL/PAL
import dal as db            # if not working try DAL.daldb as db
import time

# open Connection to Database
cursor= db.open_connection()
db.create_table(cursor)
db.data_entry(cursor)
#Read records from table
db.read_from_db(cursor)

#dynamically inserting record
db.dynamic_data_entry(cursor)
db.read_from_db(cursor)

# inserting batch of records
for i in range(5):
    db.dynamic_data_entry(cursor)
    time.sleep(1)     # sleep 1sec  for timestep to increment value
print("5 records are added to newstuff database  in stuffplot table")

#check  table 
db.read_from_db(cursor)

   
'''
    #c.execute("SELECT * FROM stuffPlot WHERE value = 3 AND keyword = 'Python' ")
    print(50 * '-')
    c.execute("SELECT unix,keyword,value FROM stuffPlot WHERE unix > 100000 ")
    [print(row) for row in c.fetchall()]
    # [print(row[0]) for row in c.fetchall()]  # this will print only unix  (Note: cursor closed after fetch of all records)
'''

# update and delete
db.del_and_update(cursor)

# close database connection
db.close_connection()