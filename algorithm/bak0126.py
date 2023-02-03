# 삼각형 외우기 
# https://www.acmicpc.net/problem/10101
# a = int(input())
# b = int(input())
# c = int(input())

# d = a + b + c

# if a == b == c == 60:
#     print('Equilateral')
# elif d == 180:
#     if a == b or b == c or c == a:
#         print('Isosceles')
#     else:
#         print('Scalene')
# elif d != 180:
#     print('Error')

# 세탁소 사장 동혁 
# https://www.acmicpc.net/problem/2720

c = [25,10,5,1]
T = int(input())

for t in range(1,T+1):
    money = int(input())
    li = []

    for i in c:
        li.append(money // i)
        money = money % i
    print(*li)

    # q = money // 25
    # d = money % 25 // 10
    # n = money % 25 % 10 // 5
    # p = money % 25 % 10 % 5

# 피시방 알바 ( 다시 풀기 )
# https://www.acmicpc.net/problem/1453

a = int(input())
b = list(map(int,input().split()))
c = []
d = 0
for i in range(a):
    if b[i] in c:
        d += 1
    else:
        c.append(b[i])
print(d)


# 제로 
# https://www.acmicpc.net/problem/10773

# import sys
# input = sys.stdin.readline    # 시간초과 

# num = int(input())
# b = []

# for i in range(num):
#     a = int(input())
#     if a == 0 :
#         b.pop()
#     else:
#         b.append(a)
# print(sum(b))

# 카드 1 (다시풀기)
# https://www.acmicpc.net/problem/2161


# a = int(input())
# b = list(range(1,a+1))
# card = []

# while len(b) >1 :
#     card.append(b.pop(0))
#     b.append(b.pop(0))

# print(*card,b[0])

# 괄호 

T = int(input())
for t in range(1,T+1):
    vps = input()
   

