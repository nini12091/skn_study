import pymysql

data = [
    {'name': 'Alice', 'age': 30, 'city': 'Seoul'},
    {'name': 'Bob', 'age': 25, 'city': 'Busan'}
]

connection = pymysql.connect(
    host='localhost',
    user='sky',
    password='sky',
    db='mydatabase',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO people (name, age, city) VALUES (%s, %s, %s)"
        for person in data:
            cursor.execute(sql, (person['name'], person['age'], person['city']))
    connection.commit()
finally:
    connection.close()