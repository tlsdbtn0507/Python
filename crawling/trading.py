import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

row1=[]
row2=[]
for row in soup.select('table.type_5'):
    for i in  row.find_all('td','no'):
        row1.append(i.text)
    for i in row.select('td>a'):
        row2.append(i.text)
# for i in list(zip(row1,row2)):
    # print(i)

a = []
for row in soup.select('table.type_5 tr'):
    if(len(row.find_all('td')) != 1):
        a.append(row)
        print(a)
    # for i in a:
    #     print(*i.select('img').attrs['src'])
# print(a)