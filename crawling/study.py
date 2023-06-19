import requests

url = 'https://httpbin.org/get'
postUrl = 'https://httpbin.org/post'

params = {'data':1,'data1':2,'data-3':3}
data = {'data':1,'data1':2,'data-3':3}
headers = {'Content-Type':'application/json; charset=utf-8','test':'test'}

# response = requests.get(url,params=params,headers=headers) 
response1 = requests.post(postUrl,params=params,headers=headers,data=data)

print(response1.status_code)
print(response1.text)