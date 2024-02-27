# count the fruit item
def count_fruit():
    print('count fruit')
    fruit = ['apple', 'banana', 'apple', 'mango', 'banana', 'mango', 'banana', 'apple', 'kiwi', 'mango', 'coconut',
             'banana', 'kiwi', 'coconut']
    ip = str(input('Chose your fruit type: '))
    if ip in fruit:
        show = fruit.count(ip)
        print('the\t', ip, 'have', show, 'one')
    else:
        print('Not found your fruit type')

# tell the age stage
"""
Infant = 0-1 year.
Toddler = 2-4 yrs.
Child = 5-12 yrs.
Teen = 13-19 yrs.
Adult = 20-39 yrs.
Middle Age Adult = 40-59 yrs.
Senior Adult = 60
"""
def age_stage():
    print('Check Your Age Stage')
    ip = int(input('Enter your age: '))
    if ip == 0:
        print('Impossible!\t =>try with another age number')
    elif ip == 1:
        print(ip, 'year old is \'Infant\'')
    elif 2 <= ip <= 4:
        print(ip, 'years old is \'Toddler\'')
    elif 5 <= ip <= 12:
        print(ip, 'years old is \'Child\'')
    elif 13 <= ip <= 19:
        print(ip, 'years old is \'Teenager\'')
    elif 20 <= ip <= 39:
        print(ip, 'years old is \'Adult\'')
    elif 40 <= ip <= 59:
        print(ip, 'years old is \'Middle Age Adult\'')
    else:
        print(ip, 'years old is \'Senior Adult\'')

def homework3():
    i = 0
    while i < 5:
        name = input('sign your name and lastname: ')
        age = int(input('sign your age: '))
        From = input('come from (province): ')
        From1 = input('come from(districts): ')
        From2 = input('come from (village): ')
        live = input('now live(village): ')
        collage = input('your collage: ')
        year = str(input('grade: '))
        major = input('your major: ')

        print('ຊື່ ແລະ ນາມສະກຸນ', name, 'ອາຢຸ', age, 'ປີ ມາຈາກແຂວງ', From, 'ເມືອງ', From1, 'ບ້ານ', From2)
        print('ປັດຈຸບັນຢູ່ບ້ານ', live, 'ກຳລັງສຶກສາຢູ່', collage, 'ປີ', year, 'ສາຂາ', major)
        i += 1


# for i in range(1, 101):
#     if i % 3 == 0:
#         print('x')
#     else:
#         print(i)


# for i in range(1, 11):
#     if i == 4 or i == 5 or i == 6 or i == 7:
#         continue
#     print(i, end=' ')


# lis = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# lis.sort()
# print(lis)


# import math as m
# li = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# li = m.fsum(li)
# print(li)



# for i in range(2, 10):
#     print()
#     for j in range(1, 11):
#         print(i, '*', j, '=', i*j)


# text = input('Enter the alphabet:')
# if text.isupper():
#     print('upper')
# elif text.islower():
#     print('lower')
# else:
#     print('new')


# for i in range(2, 9):
#     for j in range(2, 9, 7):
#         print(i, '*', j, '=', i*j)

# def func1(a, b):
#     print(f'{a} * {b} = {a*b}')
#
# func1(3, 2)

# n = int(input('Enter the position: '))
# x = 0
# for j in range(n):
#     print(j[])


