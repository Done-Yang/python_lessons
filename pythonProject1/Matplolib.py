
import matplotlib.pyplot as plt
import numpy as np
# start
"""
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.bar(x, y)   # bar shape
plt.plot(x, y)  # line shape
plt.show()
"""

# two lin
# e in a plot()
"""
product1 = [20, 22, 19, 25]
product2 = [50, 80, 44, 65]
month = [1, 2, 3, 4]
plt.plot(month, product1, color='g', marker='.', linestyle=':')    # set color green, '.' marker to product1 line
plt.plot(month, product2, 'y*--')    # short hand color yellow,'*'marker,'--' line style to product2 line
plt.title('Top year 2022', loc='center', size=20, color='y')    # set a title to the matplot
plt.legend(['product1', 'product2'],
           title='sell data',   # title of legend
           title_fontsize='small',
           loc='upper left',    # location of legend
           fontsize='10',
           facecolor='pink',     # background color
           edgecolor='green')  # set expression to the plot
plt.xlabel('Month', size=12, color='r')     # set x label name 'Month'
plt.ylabel('sum product', size=12, color='b')   # set y label name 'sum product'
plt.text(0.8, 21, 'point1')  # Text Function (text point)
# plt.savefig('Matplotlib.png')   # save as a picture path in this project
# plt.savefig('Matplotlib.png', transparent-True)     # save as png picture
plt.show()
"""

# pie charts
"""
student = np.array([20, 40, 50, 60])
lang = np.array(['Javascript', 'css', 'html', 'python'])
color = np.array(['yellow', 'blue', 'red', 'green'])
exp = np.array([0, 0.2, 0.2, 0])
plt.pie(student,
        labels=lang,
        autopct='%.2f%%',
        colors=color,
        shadow=True,
        explode=exp)    # pie chart(%.2f%%=set format percent 00.00% shape)
plt.show()
"""

# Scatter
"""
x = [10, 15, 20, 25]
y = [15, 29, 28, 35]
color = ['yellow', 'green', 'blue', 'pink']
size = [10, 20, 30, 40]
plt.scatter(x, y, c=color, s=size)
plt.show()
"""

# Histograms
"""
age = [10, 20, 15, 12, 10, 15, 12, 20, 15, 12, 20, 15, 16, 17, 19, 17]
plt.hist(age)
plt.show()
# histograms random
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
"""

# Bar chart
"""
course = ['python', 'PHP', 'JAVA']
score = [90, 89, 75]
color = ['yellow', 'blue', 'green']

plt.bar(course, score, color=color, edgecolor='black', linewidth=1)
plt.xlabel('course')
plt.ylabel('score')
plt.title('Term score')
plt.show()
"""

# Stack Bar
"""
room = ['A', 'B', 'C']
boys = [10, 12, 14]
girls = [14, 10, 17]

plt.stackplot(room, boys, girls, labels=['Boy', 'Girl'], colors=['blue', 'pink'])
plt.legend()
plt.show()
"""