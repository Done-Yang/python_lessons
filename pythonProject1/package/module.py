def number():
    print("Average temperature")
    num1 = int(input("type your number first number: "))
    num2 = int(input("type your second number: "))
    avg = (num1 + num2)/2
    print("answer: ", avg)

def tem():
    temp = {"XKH": "21 c", "VT": "29 c"}
    print("the temperature to day is: ", temp)

def win():
    win_avg = {
        "XKH": ["morning: 12 hz", "evening: 17 hz", ],
        "VT": ["morning: 10 hz", "evening: 12 hz"]
    }
    print("the win avg in VT: ", win_avg["VT"])

