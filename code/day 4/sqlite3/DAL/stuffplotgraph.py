#  line chart with matplotlib  - Data Visualization

import sqlite3
import time
import datetime
import random

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# pip install matplotlib       ( Goto terminal of sqllite3 folder and run this command to install matplotlib)
# visit https://pythonprogramming.net/matplotlib-intro-tutorial/
# you can configure, zoom , save picture , Pan Axis by clicking icons at the bottom in graph window

# try simple plot
#plt.plot([1,2,3],[5,7,4])
#plt.show()


conn = sqlite3.connect('mystuff.db')
c = conn.cursor()

def graph_data():
    c.execute('SELECT unix,value FROM stuffPlot')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])  # value column

    plt.plot_date(dates, values, '-')  # '-' means plot line graph  , 'o' means point chart
    plt.show()


graph_data()
c.close()
conn.close()
print("Observe the graph please......")
