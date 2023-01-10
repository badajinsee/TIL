# 문제 1 
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# a = input('문자열을 입력하세요 >')
# list = []
# count = 0

# for i in a:
#     if i in 'e':
#         # b.append(i)
#         count += 1
#         print(count)
#     # else i not in 'e':
#     #     print(-1)


# 문제 2 
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

# a = input('문자열을 입력하세요 >').split()
# b ={}

# for i in a :
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1

# for k, v in b.items():
#     print(k,v)

# 문제 3 
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

# a = list(input('문자열을 입력하세요 >'))

# for i in a:
#     if 'e' in a:
#         a.remove('e')
# c = ''.join(a)
# print(c)

# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

# a, b = input().split()
# count= 0

# for i in a :
#     if b in i:
#        count += 1
# print(count)


# 문제 5
# 단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

# a, b, c = input().split()

# print('{}-{}-{}'.format(a,b,c))

# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요

# a, b, c = list(map(int,input('양의 정수를 입력하세요 > ')))

# if a+b+c > 0:
#         print(a+b+c)
# else :
#         print(-1)


# 강사님 풀이 (10을 나눠서 나머지 더하기, for로 다루기 힘듬, while이용)

# while 사용
# 반복적으로 n을 10 으로 나눈 몫,
# n이 0보다 클 때 계속 반복 ! 
# 결과값은 n을 10으로 나눈 나머지를 더해나갈 것이다!

n = int(input())

if n < 0:
    print(-1)
else:
    result = 0
    while n > 0:
        result += n % 10 # 먼저 나머지 찾기 ? 
        n //= 10
        print(result)

# 문자열 사용 str()

# n = input()
# result = 0

# for i in n:
#     result += int(i)
# print(result)

