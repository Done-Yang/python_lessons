"""
# Crack function for random the password
def crack():
    import random
    screen_password = "d0n3"

    result = ""
    while result != screen_password:
        result = ""
        for letter in range(len(screen_password)):
            list_number = random.choice("1234567890abcdefghijklnmopqstuvwxyz")
            result = "".join(list_number)+str(result)
            print("searched number is: ", result)
    print("the screen password is: ", result)
crack()

# Threading "time module"

import time

start = time.perf_counter()

def do_something():
    print("sleeping 2 second...")
    time.sleep(2)   # wait for 2 second
    print("don't sleep...")
do_something()

finish = time.perf_counter()

print(f'Finish in {round(finish-start, 2)} second(s)')

# Python Cool shapes "turtle"
from  turtle import  *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)
done()

# The class
class My_table:
    def __init__(self, high, color, wide):
        self.high = high
        self.color = color
        self.wide = wide

    def show(self):
        print("my table tall: ", self.high,",", "color: ", self.color,",", "and wide: ", self.wide)

t1 = My_table("35cm", "black", "40x50")
t1.show()



# Inheritance (child class)
class Employee:
    raise_amt = 2
    liohien = 20

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        print("name", self.first, self.last)

    def apply_rais(self):
        self.pay = int(self.pay * self.raise_amt + self.liohien)

class developer(Employee):
    raise_amt = 3
    liohien = 20

    def __init__(self, firs, last, pay, add):
        super().__init__(firs, last, pay)
        self.add = add

    def fullname(self):
        print("name: (", self.first, self.last, ").\tnew experience: (", self.add, ")")


m1 = Employee('Done', 'Yang', 400)
m2 = developer("Done", "Yang", 400, "programing language")

print("working as a developer")
print("the liohien is: ", m2.liohien)
print("the rais is: ", m2.raise_amt)
m2.fullname()
print("often salary: ", m2.pay)
m2.apply_rais()

print("target salary: ", m2.pay)
"""
x = 2
y = 3
z = x+y
print(z)

