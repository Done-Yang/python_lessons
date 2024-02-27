"""
# THE LIST
# Assignment 1-2
# to find the smallest number to the greatest number
number = []
while True:
    x = int(input("enter your number: "))
    if x < 0:
        break
    number.append(x)
print("the smallest number: ", min(number))
print("the greatest number: ", max(number))
print("the tottle of all the number: ", sum(number))

# Assignment 3
# the single and couple number
number = []
even = []
odd = []
while True:
    x = int(input("enter your number: "))
    if x < 0:
        break
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)

print("all of the number: ", number)
print("the couple number: ", even)
print("the single number: ", odd)

# Assignment 4
# Do the No of the name
name = ["ana", "berry", "cuter", "gury", "bon"]
print(name)
name.sort()
print(name)
name.reverse()
print(name)

# Assignment 5
# return the No of the list
fruit = ["apple", "sherry", "kivy", "corn"]
print(fruit[::-1])

# Assignment 5
# find the Exponentiation of the list
number = int(input("type your number here: "))
exponentiation = number*number
print("you result is: ", exponentiation)


# Assignment 7
# to couple the text
greeting = ["hi: "]
name = ["done", "chit", "yang", "sana"]
result = []
result = [x+y for x in greeting for y in name]
print(result)

# Assignment 8
# to couple the goods with the cost
fruits = ["mango", "kiewy", "dragon"]
cost = [10000, 15000, 13000]
for i, j in zip(fruits, cost[::-1]):
    print("the goods: ", i, "the cost: ", j)

# Assignment 9
# to find how much alphabet in the list
massage = ["aa", "ss", "ass", "ho", "hie"]
result = []
for item in massage:
    result.append(item.count("a"))
print(result)

# THE TUPLE
tup = ("my age", 19, 44, "name", "done", True)
lis = list(tup)
lis[1] = 20
print(lis)

# return variable to tuple
tup = (1, 4, 3, 5)
a, s, d, f = tup
g = a+f
print(d, f, a, s)
print(g)

# string to tuple
y = "done", "yang"
x = tuple(y)
print(x)

# THE SET
# Union operator
fruitA = {"potato", "banana", "rice", "milk", "beans"}
fruitB = {"mango", "potato", "banana", "tomato", "orange"}

fruitC = fruitA.difference(fruitB)
print(fruitC)

# super set
fish = {"loma", "dark", "shrimn", "small fish"}
# subset
x = {"loma", "dark"}

print(x.issubset(fish))

# max and min number
number = {2,33,4,4,11,133,4,89,77,65,5,766,788,878}
print("the min number is: ", min(number))
print("the max number is: ", max(number))

# THE FrozenSet
# frozenset
food = frozenset(["rice", "meet", "milk"])
for item in food:
    print("the food will be eaten by us today: ", item)

# THE DICTIONARY
# the structure of dictionary ( {"key":"value"} )
house_number = {"fa": "phone number= 22744869 house numer= 248", "mom": 135, "sister": 321}
print(house_number["fa"])


# to cheng the dict
# place the key then = the new value
age = {"mom": "39", "pa": "50", "bro": "20", "sister": "15", "me": "19"}
x = age.copy()
print(age)

school = {
    "l-kr collage": {
        "subject": ["cpt component", "basic cpt", "english"],
        "store": ["inner", "out side"],
        "cpt class": ["class 1", "class 2", "class 3", "class 4"]
    },
    "Jommany school": {
        "subject": ["laos", "math", "english"],
        "store": ["inner", "near by"],
        "class": ["p1", "p2", "p3", "p4", "p5"]
    }
}
print("the store in l-kr collage:", school["l-kr collage"]["store"])
school.pop("Jommany school")
print(school["Jommany school"]["store"])

if "p1" in "Jommany school":
    print("yes")
else:
    print("no")
"""
