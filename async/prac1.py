import requests
import json

url = 'https://jsonplaceholder.typicode.com/photos'

res = requests.get(url).json()

done = []

for idx,i in enumerate(res):
    
    if idx == 3 :
        break
     
    body = []
    
    u = requests.get('https://jsonplaceholder.typicode.com/comments?postId={}'.format(i['id']))
    
    for j in u.json():
        body.append(j['body'])
        
    done.append({
        'id':i['id'],'title':i['title'],
        'comments':body
        })
print(done)

with open('data1.json','w') as json_file:
    json.dump(done,json_file)
