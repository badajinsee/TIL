"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
newspaper = Newspaper.objects.get(pk=1)
journalist = newspaper.journalist

print(journalist)
Laney Mccullough

"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""
count = Newspaper.objects.filter(journalist='Laney Mccullough').count()

print(count)
858

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""

newspapers = Newspaper.objects.all().order_by('-pk')

print(newspapers)
<QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, <Newspaper: Newspaper object (9998)>, <Newspaper: Newspaper object (9997)>, <Newspaper: Newspaper object (9996)>, <Newspaper: Newspaper object (9995)>, <Newspaper: Newspaper object (9994)>, <Newspaper: Newspaper object (9993)>, <Newspaper: Newspaper object (9992)>, <Newspaper: Newspaper object (9991)>, <Newspaper: Newspaper object (9990)>, <Newspaper: Newspaper object (9989)>, <Newspaper: Newspaper object (9988)>, <Newspaper: Newspaper object (9987)>, <Newspaper: Newspaper object (9986)>, <Newspaper: Newspaper object (9985)>, <Newspaper: Newspaper object (9984)>, <Newspaper: Newspaper object (9983)>, <Newspaper: Newspaper object (9982)>, <Newspaper: Newspaper object (9981)>, '...(remaining elements truncated)...']>

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""

news = Newspaper.objects.all().order_by('-created_at')

print(news)
<QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, <Newspaper: Newspaper object (5500)>, <Newspaper: Newspaper object (4918)>, <Newspaper: Newspaper object (5753)>, <Newspaper: Newspaper object (3706)>, <Newspaper: Newspaper object (4012)>, <Newspaper: Newspaper object (452)>, <Newspaper: Newspaper object (6865)>, <Newspaper: Newspaper object (3265)>, <Newspaper: Newspaper object (2643)>, <Newspaper: Newspaper object (7022)>, <Newspaper: Newspaper object (3700)>, <Newspaper: Newspaper object (3236)>, <Newspaper: Newspaper object (9607)>, <Newspaper: Newspaper object (4461)>, <Newspaper: Newspaper object (419)>, <Newspaper: Newspaper object (251)>, <Newspaper: Newspaper object (8613)>, <Newspaper: Newspaper object (1670)>, '...(remaining elements truncated)...']>

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

britney = Newspaper.objects.filter(journalist__contains='Britney').count()

print(britney)
799

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""
name = ['Britney Mahoney', 'Arianna Walls', 'Carl Short']
manyname = Newspaper.objects.filter(journalist__in=name).count()

print(manyname)
2469

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""

day = Newspaper.objects.filter(created_at__gte='2000-01-01').count()
print(day)
4355

"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""

last = Newspaper.objects.latest('pk')

print(f"title : {last.title}\ncontent: {last.content}\nJournalist: {last.journalist}")
# title : Teach father within million consumer baby its.
# content: <class 'django.db.models.fields.TextField'>
# Journalist: Laney Mccullough
