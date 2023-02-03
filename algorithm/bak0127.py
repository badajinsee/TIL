# 10817 세수 
# https://www.acmicpc.net/problem/10817

num = list(map(int,input().split()))

a = sorted(num) # 정렬

print(a[1]) # 두번째로 높은 값 출력 

# 20001 고무오리 디버깅 (몰라)
# https://www.acmicpc.net/problem/20001

a = input()
b = 0

while True:
    c = input()

    if c == '고무오리 디버깅 끝':
        break
    else:
        if c == '문제':
            b += 1
        elif c == '고무오리':
            if c == 0:
                b += 2
            else:
                b -= 1

if c == 0:
    print('고무오리야 사랑해')
else :
    print('힝구')

# 1269 대칭 차집합
# https://www.acmicpc.net/problem/1269

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = []
e = []

d.append(b)
e.append(c)

num = list(set(b) - set(c))
num_2 = list(set(c) - set(b))

print(len(num)+len(num_2))


#3052 나머지 
# https://www.acmicpc.net/problem/3052

c = []
for i in range(10):
    a = int(input())
    b = a % 42
    c.append(b)
    d = set(c)
print(len(d))

# 1181 단어 정렬 
# https://www.acmicpc.net/problem/1181

n = int(input())
word = []

for i in range(n):
    word.append(input())
word_li = set(word) # 조건 3

word_sort = []
for j in word_li:
    word_sort.append((len(j), j)) # 조건 1, 2
result = sorted(word_sort)

for key, value in result:
    print(value)

# 절댓값 힙 

a = int(input())
b = []
for i in range(a):
    c = int(input())

    if c != 0:
        b.append(c)
    else:
        d = abs(b)
