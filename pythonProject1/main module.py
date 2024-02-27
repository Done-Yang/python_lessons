"""
# Importing Module
# avg temp
import package.module as MO # "as" is set a new name to model
# also use .."from package import module as MO"..
MO.tem()
MO.win()
MO.number()

# use "from" (to specific ona e function or one part in module, able to specific all part by '*')
from module import tem

tem()
from module import *

tem()
win()

# "package" import the duplicate file
from package.module import *

tem()
win()
number()



# Utility Is Python Module
# datetime now module
import datetime

result = datetime.datetime.now() # must show 'year-month-date time'
print(result)

# set datetime by us
import datetime

result = datetime.datetime(2022, 3, 10, 0, 0, 58)
print(result)

# format time ('%x': m/d/y, '%X': time, '%c': day/ month/ date/ time/ year)
import datetime
result = datetime.datetime.now()

print(result)
print(result.strftime("%x"))
print(result.strftime("%X"))
print(result.strftime("%c"))
print(result.strftime("%m"))
print(result.strftime("%y"))
print(result.strftime("%H:%M:%S %p"))
print(result.strftime("%a"))
# to find the day in date of birthday
new_date = datetime.datetime(2002, 11, 3)
print(new_date.strftime("%A"))

# make a beautiful datetime
import datetime

print("=>DateTime today<=")
my_format = datetime.datetime.now()
print(my_format.strftime("Day: %A Date: %d Month: %m Year: %Y"))

# Module Of Python Mathematical
# basic of math: (max, min, abs"absolute", pow"**", sqrt, floor"ປັບເລກເສດລົງ", ceil"ປັບເສດຂື້ນ", pi"=3,14"...)

import math
floor = math.floor(34.464)
print(floor)
two = math.pow(7, 2)
print(two)

# dimensional trigonometry math
import math
x = math.sin(30)
y = math.cos(30)
z = math.tan(30)
print(x, y, z)

# find the radians
import math
convert = math.radians(30)
print(convert)

x = math.sin(convert)
print(x)
y = math.cos(convert)
print(y)

# 1. to find the distance between P1 and P2
import math
p1 = [2, -3]
p2 = [7, -3]
x = math.dist(p1, p2)
print("the distance p1 and p2 is: ", int(x))

# 2. distance p[5,4] and p[5,13]
import math
p1 = [5, 4]
p2 = [5, 13]
x = math.dist(p1, p2)
print("the distance p[5,4] and p[5,13] is: ", x)

# logarithm
import math
a = math.log10(1000)    #
print("log floor 10 of 1000=  ", a)

# random math
import random
for i in range(3):
    x = random.randint(2, 5)
    print(x)

# random from list
import math
import random

my_list = [1, 2, 4, "A", "B", "C", True, False, 1.1, 1.2, 1.3]
for i in range(10):
    x = random.choice(my_list)  # "Choice" is to put you own info for random

random.shuffle(my_list)     # "shuffle" is to slate the position of the info in list, tuple, dic
print(x)

# Itertools: ( product, permutation, combination, accumulate, groupby, infinite iterators
from itertools import product
a = [2, 3]
b = [4, 5]
prod = product(a, b)
print(prod)

from itertools import permutations
a = [2, 3, 1]
prod = permutations(a)
print(list(prod))

from itertools import combinations
a = [2, 3, 4, 5]
prod = combinations(a, 2)
print(list(prod))

from itertools import accumulate
a = [2, 3, 4, 5]
print(a)
prod = accumulate(a)
print(list(prod))

from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_ojt = groupby(a, key=smaller_than_3)
for key, value in group_ojt:
    print(key, list(value))

from itertools import groupby

a = [1, 2, 3, 4]
group_ojt = groupby(a, lambda x: x < 3)
for key, value in group_ojt:
    print(key, list(value))
"""


