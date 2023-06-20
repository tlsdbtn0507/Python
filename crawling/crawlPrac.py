import requests
from bs4 import BeautifulSoup

url = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

#-----------------------------------------------------------------------
#1
# prac1Name = soup.select('ul.lst_pop > li > a')
# prac1Price = soup.select('ul.lst_pop > li > span')

# prac1Res = []

# for i in range(len(prac1Price)):
#     prac1Res.append([prac1Name[i].text,prac1Price[i].text])
# # print(prac1Res)

# prac2Name = soup.select('ul.lst_major > li > a')
# prac2Price = soup.select('ul.lst_major > li > span')

# prac2Res = []

# for i in range(len(prac2Price)):
#     prac2Res.append([prac2Name[i].text,prac2Price[i].text])
# print(prac2Res)

#-----------------------------------------------------------------------
#2

# prac1Name = soup.select('ul.lst_pop > li')
# prac1Res = []

# for i in prac1Name:
#     prac1Res.append([i.find('a').text,i.find('img').attrs['alt']])
# # print(prac1Res)

# prac2 = soup.select('ul.lst_major > li')
# prac2Res = []

# for i in prac2:
#     prac2Res.append([i.find('a').text,i.find('img').attrs['alt']])
# # print(prac2Res)


#-----------------------------------------------------------------------
#3

# prac1 = soup.select('ul.lst_pop')
# pop = [] 

# for i in prac1:
#     for j in i.find_all('li','up'):
#         pop.append([j.find('a').text,j.find('span').text])
# # print(pop)


# prac2 = soup.select('ul.lst_major')
# major = []

# for i in prac2:
#     for j in i.find_all('li','up'):
#         major.append([j.find('a').text,j.find('span').text])
    
# print(major)


#-----------------------------------------------------------------------
#4
pracInfo = []
pracName = []

res = []

for i in soup.find_all('dl','detail_info'):
    pracInfo.append(i.select('.txt'))
for i in soup.find_all('div','sale_tit'):
    pracName.append(i.text.replace("\n",''))
    
for i in pracName:
    a={}
    a['name'] = i
    res.append(a)

temp = []
for i in pracInfo:
    a=[]
    for j in i:
        a.append(j.text)
    temp.append(a)

final = []

for i in temp:
    a = {}
    [b,c,d] = i[0:3]
    c1,c2 = c.split('|')
    d1,d2 = d.split('|')
    a['분양가'] = b.replace(',','').replace('만원','')
    a['유형'] = c1
    a['분양유형'] = c2
    a['세대수'] = d1
    a['평형'] = d2
    final.append(a)
    
for i in range(len(final)):
    res[i].update(final[i])
for i in res:
    print(i)

