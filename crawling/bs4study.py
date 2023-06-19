import requests 
from bs4 import BeautifulSoup

url = 'https://crawlingstudy-dd3c9.web.app/01/'

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
result = soup.find('title')
# result = soup.find('p')
resultAll = soup.find_all('p')
# resultAll = soup.find_all('p',limit=1) limit은 생략 가능하고 몇개까지 가져올건지 고름
# resultAll = soup.find_all('th','tablehead') th태그 중 class가 tablehead인 것들

# resultAll = soup.find_all('h1', attrs={'title':'welcome'}) 이는 h1중 title이 
# welcome인 것만


# result = soup.find(id='cook') id가 cook인 것


result = soup.find('table')
result2 = result.find('tbody')

# print(result.text)
# print(resultAll)

# print(result.text)
# print(result2)


# challenges
# 1
# realRes = soup.find(id='cook')

# 2
th = soup.find_all('th','tablehead')
td = soup.find_all('td')

te = soup.find('table').find('tbody').find_all('tr')

ths = []

for i in range(len(th)):
    th[i] = th[i].text

for e in te:
    temp = []
    for e1 in e.find_all('td'):
        temp.append(e1.text)
    ths.append(dict(zip(th,temp)))
    
# print(ths)


# for i in range(len(th)):
#     key.append(th[i].text)

# for i in range(len(th)):
#     temp = []
#     for j in range(len(td)):
#         temp.append(td[j].text)
#     # value.append(temp)
#     print(temp)
    
# print(temp)
# print(value)

# 3
a = soup.find_all('a')

urls =[]

for i in range(1,5):
    i = '0'+ str(i)
    urls.append(url+i+'.html')
    
for i in range(len(urls)):
    res = requests.get(urls[i])
    soup = BeautifulSoup(res.text,'html.parser')
    result = soup.find('p').text
    print(result)







