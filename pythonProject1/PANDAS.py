"""
Pandas Tutorial
"""
# make a Series from list and tuple(Series: Array 1D)
"""
import pandas as pd
list_info = ['moon', 2, True, 2.1]
tuple_info = ('erth', 5, False, 1.0)
print(pd.Series(list_info))
print('===========================================')
print(pd.Series(tuple_info))
"""

# make a Series from numpy
"""
import pandas as pd
import numpy as np
data_ar = np.array(['start', 'many', 10, False])
print(pd.Series(data_ar))
"""

# make a Serie by define index
"""
import pandas as pd

item = ['apple', 'banana', 'mengo']
idx = [23, 40, 32]
pd_sr = pd.Series(item)
print(pd_sr)
pdsr_idx = pd.Series(item, index=idx)
print(pdsr_idx)
"""

# make Series from dictionary
"""
import pandas as pd
color_dic = {'red': 'ແດງ', 'blue': 'ຟ້າ', 'pink': 'ຊົນພູ'}
idx = pd.Series(color_dic)
print(idx)
print(idx['red'])   # assess to imfomation
print(idx[1])   # assess to imfomation
"""

# Slice the Series
"""
import pandas as pd
import numpy as np
data = np.array([13, 43, 54, 1, 42])
data_pd = pd.Series(data)
print(data_pd)
print(data_pd[2])
"""

# DataFrame = Array 2D
"""
import pandas as pd

cols = ['age']
data = [10, 40, 50]
df = pd.DataFrame(data)
print(df)
print("==================================")
print(pd.DataFrame(data, columns=cols))
"""

# list more than 1Dimension to DataFrame
"""
import pandas as pd

cols = ['Item', 'type', 'coast']
data = [['iPone pro 12', 'phone', 5000000], ['note book', 'computer', 4000000], ['mouse', 'computer', 50000]]
data_frame = pd.DataFrame(data, columns=cols)
print(data_frame)
print('====================================')
"""

# Zip the list (Zip: "to compile many list together")
"""
import pandas as pd

name = ['python', 'java', 'java script']
late_version = [3.10, 7, 7.8]
used = [5000, 4800, 8000]

data = list(zip(name, late_version, used))
cols = ['language name', 'version', 'used']
data_frame = pd.DataFrame(data, columns=cols)
print(data_frame)
"""

# make dataframe from dic
"""
import pandas as pd

data = [
    {'Name': 'analise info', 'Content': 'data', 'Price': 200000},
    {'Name': 'algorithm', 'Content': 'flow chat', 'Price': 150000},
    {'Name': 'correctAGRTH', 'Content': 'repair', 'Price': 100000},
    {'Name': 'programming', 'Content': 'PG language', 'Price': 5000000},
    {'Name': 'tasting', 'Content': 'compile or interpreting', 'Price': 500000},
    {'Name': 'documentation', 'Content': 'app', 'Price': 700000},
]

dataF = pd.DataFrame(data)
dataF.set_index(['Name'], inplace=True)

print(dataF)
"""

#   tat-turn the serie to dataframe
# file management
"""
import pandas as pd

name = ['Computer', 'drinking bottom', 'glass']
category = ['electronic', 'use', 'thing']
cost = [2000000, 55000, 65000]
name_serie = pd.Series(name)
category_serie = pd.Series(category)
cost_serie = pd.Series(cost)
dic_frame = {
    'Name': name_serie,
    'Category': category_serie,
    'cost': cost_serie
}

data_frame = pd.DataFrame(dic_frame)
"""
"""
# data_frame.to_csv('pandas dataframe', header=True, index=True)    # save the data frame to the csv file
# df.to_csv('file defending', 'file name', header=True/False, index= True/False)

read_data_frame_csvfile = pd.read_csv('pandas dataframe')  # to open csv file
read_some_cols = pd.read_csv('pandas dataframe', usecols=('Name', 'cost'))  # 'usecols=' is to define the column
# data_frame.to_csv('pandas dataframe2', header=False)      # file no header
header = ['Name', 'category', 'price']
add_header = pd.read_csv('pandas dataframe2', names=header)     # add header from 'header valuable'

# excel file
excel_file = pd.read_excel('dataupdate.xlsx', 'weather', index_col='Day', dtype=str)    # open excel file

print(excel_file)
"""
# match in pandas
"""
import pandas as pd

rf = pd.read_excel("dataupdate.xlsx", "score")
print(rf.dtypes)
print(rf.Score.max())   # max number of score
print(rf.Score.mean())  # mean of student score
"""

# entry by index
"""
import pandas as pd
rf = pd.read_excel("dataupdate.xlsx", "score", index_col=False)
print(rf.Score[:3])  # print index of Score colunm from first index to index 2
print(rf[["Score", "Grade"]][1:3])      # print col 'score and row index1:3
"""

# index
"""
import pandas as pd
rf = pd.read_excel("dataupdate.xlsx", "weather", index_col="Day")
print(rf[:])    # print all info
print(rf.loc["2020-12-2":"2020-12-4"]["Event"])# or rf[slice].col    # print date and event from 12/2/2020-12/4/2020 
"""

# search data "math" and "contain"
"""
import pandas as pd
rf = pd.read_excel("dataupdate.xlsx", "weather", index_col="Day")
rf = rf[rf.Event.str.match("เมฆมาก")]  # or
# "if you put: rf = rf.Envent.str.match("เมฆมาก")" will return "True and False"
rf = rf[rf.Event.str.contains("ตก")]  # contain can be match with a latter in cell
print(rf)
"""

# check the temperature in the tale cell of Excel
"""
import pandas as pd

df = pd.read_excel("dataupdate.xlsx", "weather", index_col="Day")
for idx, row in df.iterrows():
    print("the tem is: {} make the weather: {}".format(row.Temperature, row.Event))
    print(idx)
"""

# into the data in dataframe
"""
import pandas as pd

df = pd.read_excel("dataupdate.xlsx", "weather", index_col="Day")

maxTem25 = df[df.Temperature <= 25]    # just show only the temperature that lower or = 25

Event_hot = df[df.Event.str.contains("แดดร้อน")]    # just return only the Event that contains"แดดร้อน"

rain30up = df.loc[(df.Event.str.contains("ฝนตก")) & (df.Temperature >= 30)] # show the raining that upto 30 celsius

cool18down = df.loc[(df.Event.str.contains("เมฆมาก")) | (df.Temperature <= 18)] # show the Event เมฆมาก or tem 18 down

threedays = df.loc[(df.Temperature == 18) | (df.Temperature == 20) | (df.Temperature == 25)]    # long show about three
                                                                                                # days that define

threedays_short = df.loc[(df.Temperature.isin([18, 20, 25]))]   # isin(): shorthand of three days showing

show_hot_in30 = df.loc[(df.Temperature.isin([30]))][df.Event.str.contains("แดดร้อน")]   # show the hot 30 celsius
"""

# sort index
"""
import pandas as pd

df = pd.read_excel("Stock.xlsx", index_col="Name")

# df.sort_index(ascending=True, inplace=True)   # inplace=True make doesn't need any valuable
df.sort_values("Price", inplace=True)
df['cost'] = 100    # add a column
print(df)
"""

# Rename the column
"""
import pandas as pd

df = pd.read_excel("Stock.xlsx", index_col="Name")

Rename_col = {'Price': 'Cost'}

df.rename(columns=Rename_col, inplace=True)
print(df)
"""

# Removing management
"""
import pandas as pd

df = pd.read_excel("Stock.xlsx", index_col="Name")
# remove column
rm = df.drop("Category", axis=1)  # Or "df.drop("Category", axis=1, inplace=True) and print(df)

# append row
list_append = [['mouse', 'hw', 1000], ['computer', 'o', 250]]

col = ['Name', 'Category', 'Price']
new_data = pd.DataFrame(list_append, columns=col)
df = df.append(new_data)

# remove row
is_null = df.isnull()  # is the cell empty or not
sum_null = df.isnull().sum()  # count the empty cell
sum_notnull = df.notnull().sum()  # count the contained data cell
describe = df.describe()  # print the description of the information
df['Amount'] = df['Amount'].fillna(df['Amount'].mean())     # Fill the mean number to the empty cell of Amount column
df['Name'] = df['Name'].fillna(df['Name'].fillna('Done'))
copy_upper_info = df.fillna(method='pad')  # fill by copy the topper information
delete_all = df.dropna()  # delete all row that contained the empty cells
delete_some = df.dropna(subset='Amount')  # delete the empty cell in the Amount column
delete_col = df.dropna(axis='columns')      # delete the columns that contain the empty cell
# print(df.duplicated())
print(df.dele)
"""
"""
import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())
"""

