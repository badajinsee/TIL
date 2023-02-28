#  9085 더하기

T = int(input())

for t in range(1, T+1):
    number =[]
    a = int(input())
    number = sum(list(map(int,input().split())))
    print(number) 


# 10824 네수

a, b, c, d = map(str, input().split()) # 문지로 입력 받음

one = (a+b) 
two = (c+d)

print(int(one) + int(two)) # 인트형으로 변환 

# 3009 네번째 점

# 히히 .. 어려운데여 ..ㅎㅎ 


# A+B - 5

# 실패한 코드 , 여러번 시도해서 5번이나 틀림 ㅎㅎ .. 

# for i in range(6):
#     a, b = list(map(int,input().split()))
#     if a + b == 0:
#         pass
#     else:
#       print(a+b)   

# while로 다시 만든 코드 (while 어려움 ㅠ)

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else :
        print(a+b)
        
# 1110 더하기 사이클

