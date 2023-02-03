# 10039 평균 점수

# total = 0 

# for i in range(5): # 5번 
#     score = int(input()) # 점수 입력값 

#     if score < 40 : # score가 40점 미만이면 
#         score = 40 # 40점 

#     total += score # total+score 

# print(total//5) # 몫만 


# 10871 x보다 작은 수 (re)

# N, X = list(map(int,input().split()))
# a = list(map(int, input().split()))
# for i in a:
#     if i < X:
#         print(i, end= " ")

# N, X = list(map(int,input().split())) 
# a = list(map(int,input().split())) # 리스트 형태로 들어감 
# for i in range(N): # n-1번 까지 반복 
#     if a[i] < X: #  x 값 보다 작은 값 출력 
#         print(a[i], end= " ")

# 2480 주사의 세개

# a, b, c = list(map(int,input().split()))

# if a == b == c :
#     print(10000 + a * 1000) # 같은 눈 3 개 
# elif a == b or a == c:
#     print(1000 + a * 100)  # 같은 눈 2개 (a,b)(a,c)
# elif b == c:
#     print(1000 + b * 100) # 같은 눈 2개 (b,c)
# else:
#     print(max(a, b, c)*100) # 그 외

# 10886 0 = not cute / 1 = cute (re)

N = int(input())
cute = not_cute = 0

for i in range(N):
    if int(input()) == 1:
        cute += 1 
    else:
        not_cute += 1

print('junhee is cute!' if cute > not_cute else 'junhee is not cute!') # print(참 if 조건 else 거짓)

# 2506 점수계산

n = int(input())
a = 0
result = 0
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        a += 1
        result += a
    else:
       a = 0

print(result)


