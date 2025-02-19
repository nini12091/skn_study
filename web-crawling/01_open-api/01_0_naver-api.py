import urllib.parse
import urllib.request

client_id = 'ybWfCj4ayOhq1WU4TnO1'
client_secret = 'K8cpqo2J_Z'

encText = urllib.parse.quote("오늘 점심")

# url = 'https://openapi.naver.com/v1/search/news.json?query=' + encText
url = 'https://openapi.naver.com/v1/search/news.xml?query=' + encText


request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

print(response.getcode())

response = response.read()
print(response.decode('utf-8'))