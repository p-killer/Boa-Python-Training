# Learning Python Machine Mearning
## From DSR Murthy
print("Welcome to Jypyter")
# !pip list
%lsmagic
%pwd
%ls

theList = [iter*iter for iter in range(5)]
print(theList)
print(type(theList))

listofCountries = ["India","America","England","Germany"]
firstLetters=[ country[0] for country in listofCountries ]
print(firstLetters)

%%timeit
square_evens=[n*n for n in range (1000)]
#This will profile time taken to execute

%%html
<h1>Franklin templeton</h1>
<div>Welcome to python</div>
<a href="python.org">Visit python site</a>

import pandas as pd
import numpy as np  # numpy allows to work with array/matrix with numbers
df = pd.DataFrame(np.random.rand(100,5))
df.head() # it will print top 5 records  (df.tail())

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
json.dumps(todos, indent=2)

Pandas:
#Pandas Pandas contains high level data structures and
# manipulation tools to make data analysis fast and easy in Python.

import pandas as pd #I am importing pandas as pd
from pandas import Series, DataFrame # Series and Data Frame
# are two data structures available in python
import pandas as pd #I am importing pandas as pd
from pandas import Series, DataFrame
# Series and Data Frame are two data structures available in python
Series
Series is a one-dimensional array like object
containing an array of data(any Numpy data type, and an
associated array of data labels, called its index.

mjp= Series([5,4,3,2,1])# a simple series
print mjp
# A series is represented by index on the left and values on the right
print mjp.values
# similar to dictionary. ".values" command returns values in a series
print mjp.index # returns the index values of the series
eeva = Series([5,4,3,2,1,-7,-29], index =['a','b','c','d','e','f','h']) # The index is specified
print jeeva # try jeeva.index and jeeva.values
print jeeva['a'] # selecting a particular value from a Series, by using index

jeeva['d'] = 9 # change the value of a particular element in series
print jeeva
jeeva[['a','b','c']] # select a group of values
print jeeva[jeeva>0] # returns only the positive values
print jeeva *2 # multiplies 2 to each element of a series

import numpy as np
np.mean(jeeva) # you can apply numpy functions to a Series

player_salary ={'Rooney': 50000, 'Messi': 75000, 'Ronaldo': 85000,
                'Fabregas':40000, 'Van persie': 67000}
new_player = Series(player_salary)# converting a dictionary to a series
print new_player # the series has keys of a dictionary

players =['Klose', 'Messi', 'Ronaldo', 'Van persie', 'Ballack']
player_1 =Series(player_salary, index= players)
print player_1 # I have changed the index of the Series.
# Since, no value was not found for Klose and Ballack,
# it appears as NAN
pd.isnull(player_1)#checks for Null values in player_1,
# pd denotes a pandas dataframe
pd.notnull(player_1)# Checks for null values that are not Null
player_1.name ='Bundesliga players' # name for the Series
player_1.index.name='Player names' #name of the index
player_1

player_1.index =['Neymar', 'Hulk', 'Pirlo', 'Buffon', 'Anderson']
# is used to alter the index of Series
player_1

states ={'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
                  'Population': [36, 44, 67,89,34],
                  'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states) # creating a data frame
india

DataFrame(states, columns=['State', 'Language', 'Population'])
# change the sequence of column index
new_farme = DataFrame(states, columns=['State', 'Language',
            'Population', 'Per Capita Income'],
            index =['a','b','c','d','e'])
#if you pass a column that isnt in states, it will appear
# with Na values
print new_farme.columns
print new_farme['State'] # retrieveing data like dictionary

new_farme.Population # like Series
new_farme.ix[3] # rows can be retrieved using .ic function
# here I have retrieved 3rd row
new_farme
new_farme['Per Capita Income'] = 99
# the empty per capita income column can be assigned a value
new_farme
new_farme['Per Capita Income'] = np.arange(5)
# assigning a value to the last column
new_farme

series = Series([44,33,22], index =['b','c','d'])
new_farme['Per Capita Income'] = series
#when assigning list or arrays to a column,
# the values lenght should match the length of the DataFrame
new_farme # again the missing values are displayed as NAN

new_farme['Development'] = new_farme.State == 'Gujarat'
# assigning a new column
print new_farme
del new_farme['Development'] # will delete the column 'Development'
new_farme

new_data ={'Modi': {2010: 72, 2012: 78, 2014 : 98},
           'Rahul': {2010: 55, 2012: 34, 2014: 22}}
elections = DataFrame(new_data)
print elections# the outer dict keys are columns
# and inner dict keys are rows
elections.T # transpose of a data frame
DataFrame(new_data, index =[2012, 2014, 2016])
ex= {'Gujarat':elections['Modi'][:-1], 'India': elections['Rahul'][:2]}
px =DataFrame(ex)
px









import matplotlib.pyplot as plt
#Training data
X=[ [6],[8],[10],[14],[18]]       #features  (Diameter of Pizza)
y=[ [7],[9],[13],[17],[18]]     #label  (Price)
plt.figure()
plt.title("Pizza price plotted againist diameter")
plt.xlabel("Diameter in Inches")
plt.ylabel("Price in Dollars")
plt.plot(X,y,'k')  #try k.  for plots
plt.axis([0,20,0,20])
plt.grid(True)
plt.show()

# India vs Pakistan population line chart
year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
plt.plot(year, pop_pakistan, color='g')
plt.plot(year, pop_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2019')
plt.show()

