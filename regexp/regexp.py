# ^ + str: 문자열의 시작에 str가 있는지 확인 만약 str가 있어도 맨 처음이 아니면 반환x
# $ + str: 문자열의 끝에 str가 있는지 확인 만약 str가 있어도 맨 끝에 다른 문자가 있다면 마찬가지로 반환x
# ₩(\) + 특수 문자: 특수문자를 찾고 싶을때 특수문자 앞에 ₩(\)를 붙임
# . : 그냥 .만 쓰면 모든 문자열 추출 .를 3개쓰면 4개 문자씩 추출

# [0-9]*i : 숫자가 i개 연속 있는 문자를 추출
# [0-9] : 모든 숫자
# [A-za-z] : 대소문자 구분없이 모든 알파벳 문자열
# [가-힣] : 모든 한글
# [^A-za-z] : 영문을 제외한 모두

#(aran) (aran|b) : aran문자열을 찾음 뒤에껀 aran이나 b를 찾음

#a.c = a와(아무거나)와c가 있는 것들
#a.?c = a와 c사이에 어떤것이 있어도 추출 없어도 추출
#ab*c = a와 c사이에 아무것도 없어도 추출 그 사이에 b가있어도 추출이고 x*는 x가 몇개가 있던 전부 추출
#ab+c = 위에는 다르게 +왼쪽에 있는 게 하나라도 있어야 추출 하나 이상이여도 추출

#[^ ]+ = 공백이 아닌 여러 문자들(특수 포함)
#{숫자(,로 숫자 추가 가능)} = 왼쪽의 조건이 숫자 만큼 추출

#oran(?=ge!) = orange!중 (?=)보다 앞에 있는 것만 추출
#oran(?<=ge!) = orange!중 (?<=)보다 뒤에 있는 것만 추출

#<span>((?!<br>).)<\/span> = span태그 중에 br태그가 없는 것만 추출


import re

#prac1
#--------------------------------------------------------------------

prac1 = '''jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr'''

# res = re.finditer('[a-z]+\@[a-z]+\.[a-z]*.*',prac1)

# for i in res:
#     print(i)

res = re.findall('[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]*.*',prac1)

# print(res)

for i  in res:
    print(i)

#prac2
#--------------------------------------------------------------------

text ="""
안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 
<a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.
"""

res1 = re.sub("<[^>]*>",'',text)
print(res1)

#prac3
#--------------------------------------------------------------------

text = """
<p>
<span>네이버가 뉴스 서비스에 인공지능(AI)을 도입해 페이지 뷰(PV)를 늘리고 이용자를 끌어 모으고 있다.</span>
<span>네이버는 5일 오전 서울 강남구 그랜드 인터컨티넨털 호텔에서 AI 콜로키움 2019를 열고 이 같은 AI 성과와 전략을 소개했다.</span>
<span>이날 기조연설에서 김광현 네이버 서치앤클로바 리더는 "AI 뉴스 추천 시스템인 에어스(AiRS)를 도입하면서 뉴스 소비량이 확대되고 있다" 고 말했다.</span>
</p>
"""

itss = []

res = re.finditer("<span>((?!<span>).)*<\/span>",text)

for i in res:
    itss.append(i.group().replace("<span>","").replace("</span>",""))

print(itss)

#advanced
adv = []
res = re.finditer("(?<=<span>)((?!<span>).)*(?=<\/span>)",text)

for i in res:
    adv.append(i.group())
print(adv)