"""
from datetime import datetime

start = datetime.now()

ret = 0
for i in range(1000000):
    ret += i
print('output: %d', ret)

end = datetime.now()
elapsed = end - start
print("Working time: ", end=" "); print(elapsed)

elapsed_ms = int(elapsed.total_seconds()*1000)

print("Tottle working time(ms) : %dms"%elapsed_ms)

# count number 8 between 1-10000
# first
a = str(list(range(1, 10000))).count('8')
print('first type: ', a)
# second
count = 0
for i in range(1, 10000):
    if '8' in str(i):
        count += str(i).count('8')
print('second type: ', count)
# sort hand from second
op = str([i for i in range(1, 10000)]).count('8')
print(op)
"""

