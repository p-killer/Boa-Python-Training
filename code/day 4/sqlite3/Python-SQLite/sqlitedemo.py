import sqlite3
from employee import Employee 

def connectdb():
    global conn
    conn= sqlite3.connect('emp.db')
    global cursor 
    cursor = conn.cursor()  
  

def create_table():
    try:       
        cursor.execute("""CREATE TABLE emp (
            first text,
            last text,
            pay integer
            )""")
    except Exception as ex:
        print(ex)
    

def insert_emp(emp):
    try:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
    except Exception as ex:
        print(ex)
    

def get_emps_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return cursor.fetchall()

def remove_emp(emp):
    cursor.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


# let us test it
connectdb()
create_table()

emp1 = Employee('Sriram', 'Murthy', 80000)
emp2 = Employee('Kiran', 'Kumar', 90000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Murthy')
print(emps)

remove_emp(emp1)

emps = get_emps_by_name('Murthy')
print(emps)

conn.close()
