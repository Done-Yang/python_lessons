def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n

# for i in range(10):
#     print(fib(i))


def factorial(n):
    if n <= 1:
       return n
    else:
        return n * factorial(n - 1)
    

def sum_digit(n):
    if n < 10:
        return n
    return n % 10 + sum_digit(n // 10)
print(sum_digit(121))

# def flip(some_list):
#     middle_index = len(some_list) // 2
#     if len(some_list) == 1:
#         return some_list
#     return flip(some_list[middle_index] + some_list[middle_index])

# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# some_list = flip(some_list)
# print(some_list)

