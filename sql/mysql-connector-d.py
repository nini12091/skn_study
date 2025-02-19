import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='sky',
    password='sky',
    database='menudb'
)

# menu_code가 100번 이상인 메뉴 삭제
sql = "DELETE FROM tbl_menu WHERE menu_code > %s"
values = (99, )

curser = connection.cursor()
curser.execute(sql, values)

print(f'{curser.rowcount}개의 행이 삭제되었습니다.')

curser.close()
connection.close()