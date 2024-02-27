def dec2hax(target):
    reminder = []

    while target != 0:
        reminder.append(target%16)
        target//=16

    for i in range(len(reminder)):
        if reminder[i]==10: reminder[i] = 'A'
        if reminder[i]==11: reminder[i] = 'B'
        if reminder[i]==12: reminder[i] = 'C'
        if reminder[i]==13: reminder[i] = 'D'
        if reminder[i]==14: reminder[i] = 'E'
        if reminder[i]==15: reminder[i] = 'F'

    reminder.reverse()
    return reminder

# print(dec2hax(32))
# print(int('0b11010', 16))
# print(int('0X11', 16))
# print(hex(16))
# print(bin(8))
# print()
def sumation(n):
    resault = (n  * (n +1)) /2
    
    return resault

print(sumation(100))