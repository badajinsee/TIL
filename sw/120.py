# 최빈수 구하기

T = int(input())

for t in range(1,T+1):
    a = int(input()) 
    score = list(map(int,input().split())) 
    
    num_dic = {} # 빈 딕셔너리 생성 

    for i in score:
        if i in num_dic:
            num_dic[i] += 1  # 값 있으면 +1 
        else:
            num_dic[i] = 1 # 값 없으면 그냥 1 

max_cnt = max(num_dic.vqlue())
result = []
for key, value in num_dic.items():
    if value == max_cnt:
        result.append(key)
print(f'#{a} {max(result)}') # 모르겠슈 ...

# 문자열의 거울 상

# T = int(input())

# for t in range(1,T+1):
#     word = input() # 문자로 입력 받기 
#     a = '' 
#     for i in word[::-1]: # 거꾸로 range
#         if i == 'b':
#             a  += 'd'
            
#         elif i == 'd':
#             a += 'b'
        
#         elif i == 'p':
#             a += 'q'

#         elif i == 'q':
#             a += 'p'

#     print(f'#{t} {a}')

# 직사각형 길이 찾기 

# T = int(input())
# num = []

# for t in range(1,T+1):
#     a, b, c = list(map(int,input().split())) 
   
#     if a != b:
#         d = a + b - c
#         print(f'#{t} {d}')
#     elif a == b == c:
#         e = a
#         print(f'#{t} {e}')
#     elif b != c:
#         f = a + c - b
#         print(f'#{t} {f}')

# 신용카드 만들기 1


# 시간이 없어서 못풀었어요 ㅠ 


# 신용카드 만들기 2 

# T = int(input())
# for t in range(1,T+1):
#     number = list(map(int,input())) 
#     # uumber = list(map(int,input().split('-')))
#     number = number.replace("-","")
#     if number[0] == ['3','4','5','6','9']:
#         print(f'#{t} 1')
#     else:
#         print(f'#{t} 0')

# - 을 어떻게 처리해야하는지 거기서 막혔어요 

# 소득 불균형

# T = int(input())
# for t in range(1,T+1):
#     people = int(input())

#     for i in range(people):
#         money = map(int,input().split())
#         avg = sum(money)/2



# T = int(input())
# for t in range(1,T+1):
#     people = int(input())
#     money = map(int,input().split())
#     avg = sum(money) // people
#     count = 0

#     for i in money:
#         if i <= avg:
#             count +=1
#     print(f'#{t} {count}')

# 시간이 모자라서 덜 풀었어용 . . . 

        
# 제로 
# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

num = int(input())
b = []
for i in range(num):
    a = int(input())
    
    if a == 0: 
        b.pop()
    else:
        b.append(a)
print(sum(b))


# import sys
# input = sys.stdin.readline

