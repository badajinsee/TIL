# 2047 신문 헤드라인
# print('The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.'.upper())


# N줄 덧셈 
# a = int(input())
# b = 0

# for i in range(1, a+1):
#     b += i
# print(b)

# 1936 1대1 가위바위보

# a , b = list(map(int,input().split()))

# if a > b :
#     print('A')
# elif a < b :
#     print('B') # 가위 = 1 , 바위 = 2 , 보 = 3 일때 큰 수가 이김, 비기는 경우 x


# 2027 대각선 출력하기

# print('#++++\n+#+++\n++#++\n+++#+\n++++#\n')


# 2058 자릿수 더하기 (re)

a = input()
b = 0

for i in range(len(a)):
    b += int(a[i])

print(b)

# 2019 더블더블

# a = int(input())

# for i in range(0, a+1):
#     i = 2**i
#     print(i, end= " ")
