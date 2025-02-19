import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='sky',
    password='sky',
    database='menudb'
)

cursor = connection.cursor()

cursor.execute("SELECT menu_code, menu_name, menu_price FROM tbl_menu")
result = cursor.fetchall()

for row in result:
    print("menucode:", row[0], '/', 'menuname:', row[1], '/', 'menuprice:', row[2])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
cursor.close()
connection.close()