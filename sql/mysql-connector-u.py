import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='sky',
    password='sky',
    database='menudb'
)

# 1번 메뉴를 여러분의 점심 메뉴로 메뉴명과 가격을 수정

sql = "UPDATE tbl_menu SET menu_name = %s, menu_price = %s WHERE menu_code = 1"

value = ("쌀국수", 8500)

cursor = connection.cursor()

cursor.execute(sql, value)

print(f'{cursor.rowcount}개의 행이 업데이트 되었습니다.')

connection.commit()
connection.close()