import.socket


HOST, PORT = '', 5555
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s'% PORT)
while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print(request.decode().split(' ')[1][1:])

	text= ''
	with open('index.html', 'r') as f:
		text=f.read()

	http_response='''\
	HTTP/1.1 200 OK
    '''+ text 
	client_connection.sendall(http_response.encode())
	client_connection.close()

----------------------------------------------------------------------------

import socket
import pymysql.cursor
	
connection = pymysql.conect(host='localhost',
	user='user',
	password='',
	db='employees',
	chartset='utf8',
	cursorclass=pymysql.cursor.DictCursor)

try:
    with connection.cursor() as cursor:
        sql =f"SELECT * FROM employees WHERE emp_no = {request.decode().split(' ')[1][1:]}" 
        cursor.execute(sql)       
        result = cursor.fetchone()
        print(str(result))
        res = str(result)
finally:
    connection.close()	

HOST, PORT = '', 3333
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s'% PORT)
while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print(request.decode().split(' ')[1])

	text= ''
	with open('index.html', 'r') as f:
		text=f.read()

	http_response='''\
	HTTP/1.1 200 OK
    '''+ text 
	client_connection.sendall(http_response.encode())
	client_connection.close()	