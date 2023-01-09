# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.
# 단, count() 함수는 사용하지마세요.

# a = str(input('문자열을 입력하세요 >'))
# count = 0

# for i in a:
#     if i == ('e') :     
#         count += 1
# print(count) 

# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)
# 단, count() 함수는 사용하지마세요.

# x = input('문자열을 입력하세요 >')
# count = 0

# for i in x:
#     if i in ['a','A','e','E','i','I','o','O','u','U']:
#         count += 1
# print(count)

# 문데 3
# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.  

# dict_variable = {
#     '이름': '정우영',
#     '생년': '2000',
#     '회사': '하이퍼그로스',
# }

# if '나이' not in dict_variable:
#     dict_variable['나이'] = '24'
# print('나이:', dict_variable['나이'],end='세')

# 문제 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고,
# 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

# a = input('이름을 입력하세요 > ')
# b = input('전화번호를 입력하세요 >')
# c = input('거주지를 입력하세요 > ')

# dict_variable = {
#     '이름': a,
#     '전화번호': b,
#     '거주시': c,
# }

# print(dict_variable)
# for key in dict_variable:
#     print("{} : {}".format(key, dict_variable[key]))


# 문제 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
# Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.

a = input('이름을 입력하세요 > ')
b = input('전화번호를 입력하세요 >')
c = input('이메일을 입력하세요 > ')
d = input('거주지를 입력하세요 > ')

dict = { 
    a : {
        '전화번호':b,
        '이메일':c,
        '거주지':d
    }
}
print(dict)

# 문제 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

a = input('문자열을 입력하세요 >').split()
b = dict()

for i in a:
    if i in b :
        b[i] += 1
    else:
        b[i] = 1

for key, value in b.items():
    print(f'{key} {value}')