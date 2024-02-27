"""
# THE Function
# To do the function and ask function
def say_laos():
    print("sabai dee")

def say_thai():
    print("savat dee")
def say_english():
    print("hello")
def sum():
    x = 44 + 33
    print(x)
    y = 12
    y += x
    print(y)
for i in range(2):
    say_english()
say_english()

# Global variable/ Local variable

def display_Number():
    x = 10   # local variable
    print("Hello = ", x)

x = 20  # global variable
display_Number()
print("Hello = ", x)

# to receive the value
def mydata(name, lname):  # here is the parameter
    print("Name: "+ name, lname)
# mydata("Done", "yang")
# mydata("Vansure", "yang")
fname = "done" # here is the Argument
lname = "yang"


# TO calculate the number (int) in function
def data(a, b):
    print("equal= ", a+b)
x = 3
y = 7
data(x, y)

# TO look for the single and the couple number

def my_number_type(a):
    if a % 2 == 0:
        print("couple")
    else:
        print("single")
a = 4
b = 9
my_number_type(a)
my_number_type(b)

# search single or couple number
def search_number(number):
    if number % 2 == 0:
        print("couple")
    else:
        print("single")
number = int(input("type your number: "))
search_number(number)

# Arbitrary Arguments (args) to add tuple n function def add(*....):
def add(*args):
    sum = 0
    for item in args:
        sum += item
    print("the sum is: ", sum)
add(2,5,6,5,7,5,446,55,4455,44)

# keyword Argument
def my_data(fname, lname, age):
    print("firs name: ", fname)
    print("lastname: ", lname)
    print("age: ", age)
my_data(age="19", lname="yang", fname="done")

# default parameter
def my_data(fname, lname, age="18"):
    print("firs name: ", fname)
    print("lastname: ", lname)
    print("age: ", age)
my_data(age="19", lname="yang", fname="done")
my_data("done", "yang")

# list + tuple parameter
def display_fruit(item):
    for i in range(len(item)):
        print("fruit number", i+1, item[i])
def display_food(item):
    for i in range(len(item)):
        print("the food number", i+1, item[i])


fruit = ["mango", "dragon"]
food = ("rice", "bread", "beef", "pork")
display_fruit(fruit)
display_food(food)

# function return
# find the regard of random by blank negative money
def random_number(x):
    if x == "100":
        print("random corrected")
        return 1000
    else:
        print("un corrected")
        return 0
money = random_number("100")
x = -300
result = money+x
print("regard: ", money)
print("you can earn: ", result, "because your negative is: ", x)

# "return" work like break in loop
def random_number(x):
    if len(x) != 3:
        return
    if x == "100":
        print("corrected")
        return 1000
    else:
        print("un corrected")
        return 0
money = random_number("343")
print("you collection: ", money)

# Arbitrary Argument (kwargs) to add dic contend "def .....(**...)"


# function call function
def equal(x, y, z):
    return bring_max(bring_max(x, y), z)

def bring_max(x, y):
    if x > y:
        return x
    else:
        return y

max = equal(34, 54, 64)
print("the max number: ", max)

# Recursive Function
def print_number(number):
    if number == 100:
        return

    number += 1
    print(number)
    print_number(number)

print_number(0)


# to sum number n from 1 to n (n is mean in parameter)
def sum_number(number):
    if number == 1:
        return number
    else:
        return number + sum_number(number-1)

x = sum_number(5)
print(x)

# to find factorial 9!=?
def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)
    factorial(number)

x = factorial(6)
print(x)

# to find Fibonacci number " Fn = Fn-1 + Fn-2 "
# to find F5
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(5):
    print(fibonacci(i))

# pass in function "to jump out of the error"
def have_no_idea(name):
    if name == "done":
        print("correct")
    else:
        pass
have_no_idea("don")

# Anonymous Function
# lambda function "lambda parameter : expression"

sum = lambda x, y: x+y
multiply = lambda x, y: x*y
print(sum(3, 7))
print(multiply(4, 6))


# lambda in function # do x uppercase with a
def my_multiply(x):
    return lambda a: x**a
y = my_multiply(3)
result = y(3)
print(result)

# FUNCTION ASSIGNMENT
# Assignment 1 "to summation the number"
def summation(number):
    total, avg = 0, 0
    for i in number:
        total += i
    avg = total/len(number)
    return total, avg


x = [1, 2, 3, 4, 5]
y, z = summation(x)
print("the summation is: ", y)
print("the avg is: ", z)

# to count the uppercase and the lowercase in the sentences
def find_case(name):
    result = {"UPPER": 0, "LOWER": 0}
    for c in name:
        if c.isupper():
            result["UPPER"] += 1
        elif c.islower():
            result["LOWER"] += 1
        else:
            pass
    return result

x = find_case(input("type your massage: "))
print(x)

# to find the phone number
ph = {"126": "fire", "109": "sos", "1423": "police"}
def phone_number(canter):
    for key, value in ph.items():
        if value == canter:
            print("call canter: ", key)
        else:
            print("not canter")
            return
canter = input("choose your canter: ")
phone_number(canter)

# tower of hanoi
def hanoi(n, a, b, c):
    if n == 0:
        return
    hanoi(n-1, a, c, b)
    print("plat: ", n, "from: ", a, "to", c)
    hanoi(n-1, b, a, c)

hanoi(3, "A", "B", "C")



# lambda function

def fill_in(x):
    return x ** 2


print(fill_in(4))
# >>>
ldft = lambda x: x ** 2
print(ldft(4))
# map(fun, seq)
a = (1, 2, 3, 4)
map_function = map(lambda x: x + 2, a)
print(tuple(map_function))
# filter(func, seq)
filter_function = filter(lambda x: x % 2 != 0, a)
print(tuple(filter_function))

# reduce(func, seq)
from functools import reduce
a = (1, 2, 3, 4)
reduce_function = reduce(lambda x, y: x+y, a)
print(reduce_function)



# class and object in pyhton
class computer_year1:
    def __init__(self, name, lastname, how_old):
        self.name = name
        self.lastname = lastname
        self.how_old = how_old

    def search_info(self):
        print(self.name + "\t", self.lastname + "\t", self.how_old)

no1 = computer_year1("mr done", "yang", "19")
no2 = computer_year1("mr sai", "vang", "21")
no3 = computer_year1("mr. yoa", "vang", "19")
no4 = computer_year1("mr chee", "thor", "20")
no5 = computer_year1("mss pokky", "saiyaso", "18")
no1.search_info()
no2.search_info()
no3.search_info()
no4.search_info()
no5.search_info()


# iterator
class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
my_class = mynumber()
my_iter = iter(my_class)

for i in my_iter:
    print(i)
"""
done = 120000
chit = 300000
try:
    customer_choosing = input('choose option: ')
    while customer_choosing == 'deposit':
        customer_choosing = input('choose your option: ')

    def deposit(name):
        dps = int(input('enter your deposit money:'))
        if not type(dps) is int:
            raise TypeError('Sorry try again with the numeric character')
        else:
            name += dps
            print('complete deposit. your money now is: ', name)


    def exchanging():
        pass
    if customer_choosing == 'deposit':
        print('your money now is: ', done)
        deposit(done)


except:
    print('your function not default')

