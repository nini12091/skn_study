import urllib.parse
import urllib.request
import json
import mysql.connector

client_id = 'ybWfCj4ayOhq1WU4TnO1'
client_secret = 'K8cpqo2J_Z'

searchText = urllib.parse.quote("소나기")

url = 'https://openapi.naver.com/v1/search/book.json?query=' + searchText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-id", client_id)
request.add_header("X-Naver-Client-secret", client_secret)

response = urllib.request.urlopen(request)
response_body = response.read()
response_body = json.loads(response_body)

book_list = response_body['items']

connection = mysql.connector.connect(
    host="localhost",
    user="sky",
    password="sky",
    database="bookdb"
)

cursor = connection.cursor()

sql = "INSERT INTO naver_book(book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"

for book_info in book_list:
    values = (book_info['title'], book_info['image'], book_info['author'], book_info['publisher'], book_info['isbn'], book_info['description'], book_info['pubdate'])
    cursor.execute(sql, values)

connection.commit()

cursor.close()
connection.close()