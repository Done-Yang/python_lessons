"""
# try....exception
try:
    x = int(input("type your number: "))
    y = int(input("type your number: "))
    result = x%y
    print(result)

except ValueError:  # to manage with Exception
    print("only the integer")
except ZeroDivisionError:
    print("unable /, % with '0'")
except TypeError:
    print("unable between 'string', 'int', 'tuple'")
finally:    # be able to continue working with the error
    print("finishes")

# "Exception" object is to tell case error for us
try:
    x = int(input("type your number: "))
    y = int(input("type your number: "))
    result = x % y
    print(result)
except Exception as e:
    print(e)
else:   # work when didn't have the error if error it won't be work
    print("finish")

# while loop in exception
while True:     # It won't be out the loop without the condition
    try:
        x = int(input("type your number: "))
        y = int(input("type your number: "))
        if x == 0 and y == 0:
            print("finish")
            break
        if x < 0 or y < 0:  # to manage type of error in "Exception" object
            raise Exception("un support negative number")
        result = x / y
        print("answer", result)
    except Exception as e:
        print(e)

    finally:
        print("continue...")

# accounting program
account = {"done": 1000, "chit": 0}
def saving():
    print("your sentry info:", account)

def deposit(number):
    if not type(number) is int:
        raise Exception("must be the number")
    if number < 0:
        raise Exception("unable negative money")
    account["done"] += number
    print("your deposit money to 'done':", number)
    print(saving())

def withdraw(number):
    if not type(number) is int:
        raise Exception("must be the number")
    if account["done"] < number:
        raise Exception("un support")
    if number < 0:
        raise Exception("un support")
    account["done"] -= number
    print("done withdraw money: ", number)
    print(saving())

def transfer(number):
    if not type(number) is int and not type(number) is float:
        raise Exception("must be the number")
    if number > account["done"]:
        raise Exception("un support")
    account["done"] -= number
    account["chit"] += number
    print("done transfer: ", number, "to 'chit'")
    print("chit receive: ", number, "from 'done'")
    print(saving())

try:
    transfer(22.23)
except Exception as e:
    print(e)
"""
