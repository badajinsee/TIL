 # 2071 평균값 구하기 

# T = int(input())

# for t in range(1, T+1): # (1, 4) 3까지 반복 
#     numbers = list(map(int,input().split())) # 수 입력 받기 
#     a = sum(numbers) # 합 계산 a 
#     b = len(numbers) # 길이 계산 b 
#     print(f'#{t} {round(a/b)}') # 횟수 , 합/길이 , 반올림 계산 

   
# 아주 간단한 계산기 

a, b = list(map(int, input().split()))

print(a + b)
print(a - b)
print(a * b)
print(int(a / b)) # 소숫점 이하 버리기 위해 정수 int , a//b도 가능 

# print(a+b, a-b, a*b, int(a/b),sep='\n') # 한줄로 sep = '\n'

# 2046. 스탬프 찍기

# a = int(input())
# print('#'* a)   
# print('#'*int(input()))

# # 2068 최대수 구하기

# T = int(input())

# for t in range(1,T+1):
#     a = list(map(int,input().split()))
#     b = max(a)
#     print(f'#{t} {b}')

# # 2029 몫과 나머지 출력하기

# T = int(input())

# for t in range(1,T+1):
#     a,b = list(map(int,input().split()))
#     x = a // b
#     y = a % b
#     print(f'#{t} {x} {y}')

# 2072 홀수만 더하기

# T = int(input())

# for t in range(1,T+1):
#     a = list(map(int, input().split()))
#     b = 0
#     for i in a:
#         if i % 2 == 1:
#             b += i
#     print(f'#{t} {b}')
        
# 2070 큰놈, 작은놈, 같은놈 

# T = int(input())

# for t in range(1, T+1):
#     a, b = map(int,input().split())
#     if a > b :
#         print(f'#{t} >')
#     elif a == b :
#         print(f'#{t} =')
#     elif a < b :
#         print(f'#{t} <')

    
