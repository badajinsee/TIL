# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

# a = int(input('정수를 입력하세요 >'))

# if a > 0 :
#     print('True')
# else :
#     print('False')

# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.

# 두 정수가 같으면 False를 출력하세요.

# a = int(input('첫번째 정수를 입력하세요 >'))
# b = int(input('두번째 정수를 입력하세요 >'))

# if a > b :
#     print(a)
# elif b > a :
#     print(b)
# elif a == b :
#     print("False")

# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.

# a = int(input('정수를 입력하세요 >'))

# if 1 < a and a < 10 :
#     print('True')
# else :
#     print('False')

# 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

# a = int(input('정수를 입력하세요 >'))

# if a > 0 and (a%2==0):
#     print('True')
# else :
#     print('False')

# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

# a = int(input('정수를 입력하세요 >'))

# if a > 100 and a < 0 :
#     print('에러')
# elif a >= 60:
#     print('합격')
# else:
#     print('불합격')

# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.

# a = input('문자열을 입력하세요 >')

# for char in a [::-1]:
#     print(char)

#정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
#두 값이 같으면 False를 출력하세요

# a = int(input('첫 번째 정수를 입력하세요 >'))
# b = int(input('두 번째 정수를 입력하세요 >'))

# if a == b :
#     print('False')
# elif a > b :
#     for i in range(b+1,a):
#         print(i)
# elif a < b :
#     for j in range(a+1,b):
#         print(j)



# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

# 두 값이 같으면 False를 출력하세요

# a = int(input('첫번째 정수를 입력하세요 >'))
# b = int(input('두번째 정수를 입력하세요 >'))

# if a==b:
#     print("False")
# elif a > b:
#     for i in range(a-1,b,-1):
#         print(i, end=(' '))
# elif a < b :
#     for j in range(b-1,a,-1):
#         print(j, end=(' '))

# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

# a = int(input('정수를 입력하세요 >'))

# if a > 1 :
#     for i in range(1,a,2):
#         print(i)

# elif a < 1:
#     print("False")

# 구구단을 출력하세요.

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}')