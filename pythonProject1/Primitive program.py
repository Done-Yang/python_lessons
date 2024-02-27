"""
# I. this part is Primitive
print("hello world")
# this title is show about the loop

try1 = 10
try2 = "hey you"
try3 = True

print("last try =" + str(try3))


# this title is show the string
meal1 = "rice, pork, water"
meal2 = "apple, fruit, mill"

if meal1 == "mill":
    print(meal1 + "yes you have eaten")
else:
    print("maybe" + "meal2")

food1, food2 = meal1, meal2
print("food1 is: ({}), food2 is: ({})".format(food1, food2))

if "pork" in food2:
    print("yes")
else:
    print("not me")

x = input("your information: ")
print("this is your information =" + x)
x = 50
y = 20

print("negative", x-y)
print("positive", x+y)
print("two slash", x//y)
print("one slash", x/y)
print("get the ເສດ", x % y)
print("**", x**2)
print(y >> x)
# operator
x1 = (10 > 5)
x2 = (10 == 5)
y1 = x1 or x2
print(not y1)

# control structure
age = int(input("enter your age: "))

if age <= 18:
    print("your age not pass")
    print("finish")
else:
    print("continue")
if age <= 15:
    print("children")
elif age >= 15 and age<=19:
    print("teenager")
elif age >= 20:
    print("twen-teen")

print("finish")
if age <= 15:
    print("children")
else:
    print("teenager")


print("finish")


# ternary operator
print("children") if age <= 15 else print("teenager")

print("finish")

# if in if
level = int(input("grade: "))

if level <= 15:
    print("Secondary school")
    if level == 14:
        print("M 3")
    elif level == 13:
        print("M 2-M 1")
    elif level <= 12 and level >= 1:
        print("primary")
else:
    print("upper secondary school")

# Assignment 1
# ການຄຳນວນລະດັບຄວາມອ້ວນ
weight = int(input("please put your weight (kg): "))
high = int(input("please put your high (cm): "))/100
print("BMI",  weight/(high*high))
# Assignment 2
# more than and less than
a = int(input("enter your number"))
b = int(input("enter your number"))

if a > b:
    print(a, "more than" , b)
else:
    print(a,"less than" ,b)
# Assignment 3
# ການຊອກຫາວ່າ ອິນພຸດເປັນເລກຄູ່ຫຼືຄີກ
number = int(input("enter your number: "))
if number % 2 == 0:
    print("ເລກຄູ່")
else:
    print("ເລກຄີກ")

# Assignment 4
# money exchange
number = int(input("enter your money: "))

if number >= 100000:
    print("the 100 000 kip: " + str(number//100000))
    number %= 100000
if number >= 10000:
    print("the 10 000 kip:" + str(number//10000))
    number %= 10000
if number >= 2000:
    print("the 2 000 kip:" + str(number//2000))
    number %= 2000
if number >= 500:
    print("the 500 kip: " + str(number//500))
    number %= 500

# Assignment 5
# find the ຄສ to ພສ and ພສ to ຄສ

numbers = int(input("enter ຄສ: "))
numbers += 543
print("to ພສ: " + str(numbers))

# BMI testing
print("# ການວັກແທກລະດັບ BMI ຂອງທ່ານ #")
weight = int(input("ປ້ອມນ້ຳໜັກຂອງທ່ານ: "))
high = int(input("ປ້ອມລວງສູງຂອງທ່ານ: "))/100

bmi = weight/(high**2)
if bmi >= 0 and bmi <= 18.5:
    result = "ຈ່ອຍຫຼາຍ ເພີ່ມແນວກີນໄຫ້ເພີ່ມນຳ້ໜັກເນເດ່"
elif bmi >= 18.6 and bmi <= 22.9:
    result = "ພໍດີ"
elif bmi >= 23.0 and bmi <= 24.9:
    result = "ນຳ້ໜັກເກີນ ຄວນຜ່ອນການກີນ ແລະ ອອກກຳລັງກາຍເນເດ່"
elif bmi >= 25.0 and bmi <= 29.9:
    result = "ເຈົ້າເປັນໂລກອ້ວນແລ້ວ ຄວນປຶກສາໝໍ"
elif bmi > 30:
    result = "ເປັນໂລກອ້ວນລະດັບອັນະລາຍແລ້ວເດິ"
else:
    result = "ບໍ່ສາມາດອ່ານຄ່າໄດ້"

print("ຄ່າ BMI ຂອງທ່ານ: ",  bmi, "ໄຫ້ຮູ້ວ່າ: ", result)

# string
name = "the dog"
personality = "like to eat the bon"
term = "1 h"
x = "name: {}\tpersonality: {}\tterm: {}"

print(x.format(name, personality, term))
print(type(x))
if x.startswith("the"):
    print("true")
else:
    print("fals")
if personality.endswith("bon"):
    print("yes")
else:
    print("no")
# assignment 7
# calculate the tamp
temp = input("enter your temp with c or f: ")

degree = int(temp[:-1]) # take the C or F
unit = temp[-1].upper()

if unit == "C":
    result = (9*degree)/5+32
    unit_result = "F"
if unit == "F":
    result = (degree - 32)*5/9
    unit_result = "C"

print("turn= ", temp, "to", unit_result, " = ", result)

# while loop
# Assignment 8:ການຫາຜົນລວມຂອງຈຳນວນຮອບຂອງ while loop

i = 1
summation = 0
while i <= 8:
    summation += i
    average = summation/8
    print("the while of i= ", i, "the sum: ", summation)
    i += 1
print("tottle of summation: ", summation)
print("the average: ", average)

# for loop
summation = 0
for i in range(10,1,-2):
    summation += i
    print("round:",i," hello world!")
print("sum: ", summation)

# while loop in while loop

i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print("first round= ", i, "position= ", j)
        j += 1
    i += 1

for i in range(1, 11):
    print("round: ", i)
    for j in range(1, 6):
        print("floor: ", j)

# ສ້າງບັ້ງສູດ ໃຫ້ຮອດບັ້ງ 12
# use loop n loop
start = int(input("ປ້ອມບັ້ງສູດບັ້ງທຳອິດ: "))
stop = int(input("ເຖີງບັ້ງສູດບັ້ງທີ່: "))
for x in range(start, stop+1):
    print("ບັ້ງ: ", x)
    for y in range(1, 11):
        print(x, " x ", y, " = ", x*y)

#
# break, continue in while loop and in for loop
#

# summation in while loop

sum = 0
while True:
    number = int(input("enter your numer: "))
    sum += number
    if sum > 100:
        break
    print("title: ", sum)


# Assignment 11
# ຄົ້ນຫາຄ່າໃຫຍ່ສຸດ
max, min =0,9999
while True:
    number = int(input("enter your number: "))
    if number<0:
        break
    if number > max:
        max=number
    if number < min:
        min=number
print("max: ", max)
print("min: ", min)

# the floor of the number
last = int(input("enter yor number: "))

for row in range(1, last+1):
    for column in range(1, row+1):
        print(column, end=" ")

    print(" ")

# Assignment 13 ການສ້າງພາບລ່ຽມຈະຸຕຸລັດ
number = int(input("enter the size: "))

for row in range(number+1):
    for column in range(number):
        print("x", end="")
    print(" ")


# ສ້າງຕາກາໂລ້ ໝາກຄອກ
number = int(input("enter your size: "))
for row in range(number):
    for column in range(number):
        print("x", end="") if (row+column)%2 == 0 else print("o", end="")
    print(" ")

# ສ້າງຂອບຕາຕະລາງ
number = int(input("enter your size: "))
for row in range(number):
    for column in range(number):
        if row == 0 or row == number-1 or column == 0 \
                or column == number-1:
            print("x", end="")
        else:
            print(" ", end="")
    print(" ")
"""
# Assignment 18
# ແກມທາຍລູກເຕົ໋າ
import random
print("you can play around 3 time \n")
correct = False
my_random = random.randrange(1, 7)
print(my_random)
k = 1
while True:
    number = int(input("enter your number: "))
    correct = (number == my_random)
    if not correct:
        if number > my_random:
            print("less than")
        if number < my_random:
            print("more than")

    if correct:
        print("you can earn 1 000 000")
        print("marry with you")

        break
    else:
        print("lucky for next time: ")
    if number <= 0 or k == 3:
        break
    k += 1
if not correct:
    print("the random is: ", my_random)
    print("feel sed with you")
""""""

