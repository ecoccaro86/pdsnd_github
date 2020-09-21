#filename = 'chicago.csv'

import pandas as pd

#CITY_DATA = { 'chicago': 'chicago.csv',
              #'new york city': 'new_york_city.csv',
              #'washington': 'washington.csv' }

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
print(groceries)
