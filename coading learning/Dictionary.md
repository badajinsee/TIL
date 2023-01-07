# 딕셔너리😯

키-값 쌍으로 이뤄진 모음

    키 :불변 자료형만 가능

    값 : 어떠한 형태든 관계 없음

    변경 가능하며, 반복 가능함

## 딕셔너리 순회

---

- keys() : key로 구성된 결과

- value(): value로 구성된 결과

- items(): (key, value)의 튜플로 구성된 결과

```python
grages = {'john':80, 'eric': 90}
print(grades.keys())
print(grades.value())
print(grages.items())

# dict_keys(['john','eric'])
# dict_values([80, 90])
# dict_items([('john', 80),('eric', 90)])

# 딕셔너리 리스트 열거
fruits = {'banana':300 , 'apple' : 200, 'mango':400}

list(fruits.keys())
['banana', 'apple', 'mango']

sorted(fruits.keys()) # 정렬된 목록을 리스트 형으로 얻어낸다

#['apple', 'banana', 'mango']



# for 구문과 함께
fruits = {
    '바나나':3000,
    '오렌지':2400,
    '딸기':3500,
    '망고':4000
}

for name in fruits.keys():
    price = fruits[name]
    s = '{0}는 {1}원 입니다.'.format(name, price)
    print(s)

# 바나나는 3000원 입니다. 등등 출력

# 다른 방법
    for name, price in fruits.items():
        s = '{0}는 {1}원 입니다.'.format(name,price)
    print(s)



```

- for 키, 값 in 딕셔너리.items(): # 키와 값을 이용한 처리

```python
# 영단어의 출연하는 횟수

text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 단어 구분
text = text.replace(";","")
text = text.replace(",","")
text = text.replave(".","")
words = text.split()

counter = {} # 빈 딕셔너리 생성
for w in words:
    ws = w.lower() # 소문자로 변환
    if ws in counter: # 딕셔너리에 이미 키가 있으면 값을 1개 추가
        counters[ws] += 1
    else:     # 딕셔너리에 키가 없으면 값을 1로 바꾸고 키 등록
        counters[ws] = 1

# 결과 표시

for k,v in sorted(counter.items()):
    if v >= 3:
        print(k,v)

```
