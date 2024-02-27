# reference module ('random')
import random
"""
print(random.randint(1, 5))
print(random.random() * 5)

rd = random.choice(["a", "b", "c", "d", "e"])
print(rd)

list = ["name", "last name", 22, 11.2, False]
random.shuffle(list)
print(list)

lst = [i for i in range(10)]
random.shuffle(lst)
print(lst)

for i in range(10):
    print(random.randrange(20))
"""

# reference module ('statistics')
import statistics

number = [1, 6, 7, 5, 9, 15, 10]
print(statistics.mean(number))  # SAME print((sum(number)/len(number)))
print(statistics.median(number))    # print the median values of the number in the list
print(statistics.median_high(number))
print(statistics.median_low(number))
print(statistics.mode(number))  # print the more values in the list
print(statistics.median_grouped(number))
print(statistics.stdev(number))
print('your name is [%d] your lastname is [%d]' %'done', 'yang')


