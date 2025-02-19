import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='sky',
    password='sky',
    database='menudb'
)

if connection.is_connected():
    print("MYSQL에 성공적으로 연결되었습니다.")

connection.close()