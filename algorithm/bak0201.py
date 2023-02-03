# 오븐시계 

# h, m = list(map(int,input().split()))
# a = int(input())

# m += a # 분 더하기 
# h += m //60 # 시에 분 더해서 60 나눈 몫 

# m %= 60 # 60분으로 나눈 나머지
# h %= 24 # 24시로 나눈 나머지 
# print(h,m)

# 블랙잭 
# n, m = map(int, input().split())
# num = list(map(int, input().split()))

# total = 0
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             if(num[i] + num[j] + num[k] > m):
#                 continue
#             else:
#                 total = max(total ,num[i] + num[j] + num[k])

# print(total)
           
# 점수 집계 

# T = int(input())

# for t in range(1,T+1):
#     a = list(map(int,input().split()))
#     a.remove(max(a)) # max 값 제거
#     a.remove(min(a)) # min 값 제거 

#     if max(a) - min(a) >= 4: # 남은 리스트에서 max와 Min 차이가 4보다 크거나 같으면
#         print('KIN') # kin
#     else:
#         print(sum(a)) # 나머지는 합계 

# 가장 큰 금민수

a = input()

while True:
    if len()


# 영화 감독 숌 

# https://www.acmicpc.net/problem/1436

# a = int(input())
# num = 666
# while True:
#     if '666' in str(num):
#         a -= 1
#     if a == 0:
#         break
# num += 1
# print(num)
