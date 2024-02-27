"""
# is digit()
# enumerate()
for i, letter in enumerate(['a', 'b', 'c'], start=1):
    print(i, letter)

num = input('type your number: ')
if num.isdigit():
    num = num[::-1]
    ret = ' '
    for i, c in enumerate(num):
        i += 1
        if i != len(num) and i % 3 == 0:
            ret += (c+',')
        else:
            ret += c
    ret = ret[::-1]
    print(ret)

else:
    print('it not number')

# activity
# move the first index to last nuber
y_input = input('enter your text: ')

ret = ''
for i in range(len(y_input)):
    if i != len(y_input) - 1:
        ret += y_input[i+1]
    else:
        ret += y_input[0]
print(ret)
"""
print('hello')
