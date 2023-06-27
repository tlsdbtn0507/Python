import requests 
import re #정규표현식 사용

#정규표현식 사용예
#ex) re.sub('정규표현식',치환할 문자,대체 받을 문자열)
from bs4 import BeautifulSoup

url = 'https://www.musinsa.com/categories/item/001'

src = requests.get(url)

soup = BeautifulSoup(src.text,'html.parser')

lists=[]

for i in soup.select('ul#searchList > li'):
    if i.select_one('p.item_title') == None: 
        continue
    # print(i.select_one('p.item_title').text.strip())
    print((i.select_one(' .article_info p.price').text).strip().split(' '))
    # for j in soup.select('div.article_info'):
    #     brand = j.select_one('p.item_title').text.strip()
    #     title = j.select_one('p.list_info').text.strip()
        
    #     lists.append({
    #         'brand':brand,
    #         'name': title
    #     })

        # print(j.select_one('p.price'))
        # print(i.select_one('p.list_info'))
        # print(i.find(class_='price').text.strip())
# print(lists)