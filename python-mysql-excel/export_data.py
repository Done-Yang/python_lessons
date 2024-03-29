import mysql.connector
from openpyxl import Workbook

# database
db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='doneMySQL1582022',
    database='done_want_to_buy'
)

cursor = db.cursor()
sql = '''
    SELECT *
    FROM products
'''

cursor.execute(sql)

products = cursor.fetchall()

# Excel
workbook = Workbook()
sheet = workbook.active
sheet.append(['id', 'name', 'cost', 'need', 'date'])

for p in products:
    print(p)
    sheet.append(p)

workbook.save(filename='export.xlsx')
