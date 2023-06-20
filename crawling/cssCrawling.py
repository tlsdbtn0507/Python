import requests
from bs4 import BeautifulSoup

url = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# result = soup.select('div')

result = soup.select('.bold.blue') #class가 bold이면서 blue인것
result1= soup.select('div#title.bold.blue')  
#div태그중 class가 bold이면서 blue이면서 id가 title인것

# result = soup.select('#title')select은 검색결과가 일치하는 모든 리스트!를 가져옴
# result = soup.select_one('div')

# select(tag명[속성 ~= 값]) =>속성에 단어를 포함한 태그 찾기
# select(tag명[속성 ^= 값]) =>속성에 값으로 시작하는 태그 찾기
# select(tag명[속성 $= 값]) =>속성에 값으로 끝나는 태그 찾기
# select(tag명[속성 *= 값]) =>속성에 값을 포함한 태그 찾기

# select('tag명(#id명 생략가능) p') => tag안에 p태그가 달린 모든것들(후손)
# select('tag명(#id명 생략가능) > p') => tag안에 p태그가 달린 것(자식)

print(result)

