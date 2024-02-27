# stack
my_stack = []

def put_data(data):
    global my_stack
    my_stack.append(data)

def pop_data():
    global my_stack
    if len(my_stack) == 0:
        return None
    return my_stack.pop()

put_data(1)
put_data(2)
put_data(3)
put_data(4)

print('<stack status>', end=''); print(my_stack)


ret = pop_data()
print(ret)
while ret != None:
    print('pop data: ', end='')
    print(ret)
    print('Stack status: ', end=''); print(my_stack)
    ret = pop_data()

