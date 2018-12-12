import pymysql.cursors

email = 'beka.bk00@gmail.com'

connection = pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    db = 'db',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO db.employ SELECT * FROM employees.employees')
        
    connection.commit()

finally:
    connection.close()
