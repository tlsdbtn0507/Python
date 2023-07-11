import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'
#비동기 사이트를 크롤링 할때 원하는 사이트에서 데이터를 요청(get)해올 url을 써야함

res = requests.get(url)

print(res.status_code)
print(res.text)

print(res.json())# res로 받아온 데이터를 딕셔너리로 바꿈

resJson = json.loads(res.text)# json으로 받은 데이터 딕셔너리화
with open('data.json','w') as json_file:
    json.dump(resJson,json_file); #'data.json'라는 이름과 읽기 형식으로 json파일을 만듬