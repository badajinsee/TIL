# 17608 막대기 
import sys 
a = int(input())
b = []
count = 1
for i in range(a):
    b.append(int(sys.stdin.readline()))
num = b.pop()
for j in range(a-1):
    number = b.pop()
    if number > num :
        count += 1
        num = number
print(count)

# 덩치 

a = int(input())
c = []
for i in range(a):
    b = list(map(int,input().split()))
    c.append(b)

for i in c:
    result = 1
    for j in c:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    print(result, end=" ")

# 기본 순위 1위로 고정, 나머지 값 비교하여 자신보다 큰 덩치 result 증가 