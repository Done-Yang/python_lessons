""""""

# while loop
import random


def while_loop():
    a = 1
    c = 1
    n = 1
    end = int(input("enter your number: "))
    while n <= end:
        a *= n
        n += 1
    while c <= end - 1:
        print(c, "*", end=" ")
        c += 1
    print(end, " = ", a)


# homework
# 1. "show numeric1-20 step 2 continue on 14"

def homework1():
    num = 0
    show = 0
    while num <= 20 - 1:
        num += 2
        show += num

        if num == 14:
            continue

        print(num, end=" ")


# 2. "show numeric 1-20 step 3 break on 12"
def homework2():
    num = 0
    show = 0
    while num <= 20:
        show += 3
        print(show, end=" ")
        if show == 12:
            break
        num += 1


# for loop (start, atop, step)
def bansuk():
    j = 2
    x = int(input('ປ້ອມບັ້ງທໍາອິດ: '))
    y = int(input('ປ້ອມບັ້ງສຸດທ້າຍ: '))
    for i in range(x, y + 1):
        for j in range(2, 13):
            x = i * j
            print(i, '*', j, '=', x)
        print()


def triangle():
    a = input("enter your character type: ")
    z = int(input("enter your triangle tall size: "))
    for i in range(z + 1):
        for j in range(i):
            print(a, end=" ")
        print()


# searching function commend
"""
# searching function choice by key bord
x = input("your functon: ")
if x == 'triangle':
    print(triangle())
elif x == 'bansuk':
    print(bansuk())
elif x == 'homework1':
    print(homework1())
elif x == 'homework2':
    print(homework2())
elif x == 'homework3':
    print(homework3)
"""


# homework
# turn the triangle position to up-size-down
def homework3():
    try:

        a = input('chose your character: ')
        b = int(input('put your triangle size: '))

        for i in range(b):
            for j in range(i, b):
                print(a, end='')
            print()

    except ValueError:
        print("triangle size must be integer")
    else:
        print('completed')


def activity1():
    for i in range(7):
        for j in range(i, 7):
            print('', end=' ')
        for j in range(i):
            print('*', end=' ')
        print()
    for i in range(7):
        for j in range(i):
            print('', end=' ')
        for j in range(i, 7):
            print('*', end=' ')
        print()


def activity2():
    try:
        while True:
            bun = int(input('fist number: '))
            num = int(input('end number: '))
            for i in range(bun, num + 1):
                for j in range(1, 13):
                    print(i, '*', j, '=', i * j)
            end = str(input('Do you want to end the program? Y/N: '))
            y, Y = 'y', 'Y'
            n, N = 'n', 'N'
            if end == y or end == Y:
                continue
            if end == n or end == N:
                print('thanks')
                break

            if end != y or end != Y and end != n or end != N:
                stop = 3
                while True:
                    end2 = input('Try Again: just allow \"n or N and y or Y\": ')
                    if end2 == n or end2 == N:
                        print('thanks')
                        return
                    if end2 == y or end2 == Y:
                        print('<<replaying>>')
                        break
                    stop -= 1
                    if stop <= 0:
                        print('<<more trying. wait for new round>>')
                        return

    except TypeError:
        print('input must be integer')
    except ValueError:
        print('input type must be integer')


# input ten time of str to append in the list empty list
# input int and * 2 to list by 10 time
def homework4():
    lis = []
    for i in range(5):
        ip = input('typ your text: ')
        lis.append(ip)
    print(lis)


def homework5():
    lis = []
    for i in range(5):
        ip = int(input('Enter your number: '))
        lis.append(ip)
    for i in range(len(lis)):
        print('index', i, 'is', lis[i])


def find_max_min():
    # print the max number and min number without max and min
    number = []
    while True:
        ip = int(input('Enter your list: '))
        if ip > 0:
            print('<<press exit to end>>')
            number.append(ip)
        else:
            break

    print(number)
    mx = number[0]
    mn = number[0]
    for i in range(len(number)):
        if mx < number[i]:
            mx = number[i]
        elif mn > number[i]:
            mn = number[i]
        else:
            pass
    print('max number is: ', mx)
    print('min number is: ', mn)


def homework6():
    print('<<Dividing Number>>')
    odd = []
    even = []
    number = []
    i = 0
    while i < 10:
        ip = int(input('Enter your list: '))
        number.append(ip)
        i += 1

    for i in range(len(number)):
        if number[i] % 2 == 0:
            even.append(number[i])
        else:
            odd.append(number[i])
    print('your list: ', number)
    print('odd number: ', odd)
    print('even number: ', even)


def homework7():
    lis_name = ['Yao', 'Vick', 'Sam', 'Done']
    Say = ['hi ', 'how are you ', 'nice to meet you']
    show = []
    lis2 = ['nice to meet you too']
    lis_name += lis2
    for i in lis_name:
        for j in Say:
            show.append(j + i)
    print(show)


def homework8():
    num = 100
    n = 1
    lis = []
    while n <= num:
        lis.append(str(n))
        n += 1
    for i in range(len(lis)):
        lis[i] = lis[i].replace('3', 'X')
        lis[i] = lis[i].replace('6', 'X')
        lis[i] = lis[i].replace('9', 'X')
        print(lis[i])
# set: un indexed, un cheng able, not allow duplicating
"""
def python_array():
    a = {'hello', 'hi', 'good morning'}
    b = {'hi', 'how are you?', 'hello'}
    difference = {}
    same = {}
    Union = a.union(b)
    print(Union)        # union: ການຮົມ(print all union)
    Intersection = a.intersection(b)
    print(Intersection)     # intersection():print same value
    Difference = a.difference(b)
    print(Difference)       # print the difference of a to b
    print('update part')
    a.intersection_update(b)  # a assigned the same data now
    print(a)

    b.difference_update(a)      # b assigned the difference data now
    print(b)
"""
