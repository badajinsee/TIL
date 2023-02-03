# 별찍기 - 4
# https://www.acmicpc.net/problem/2441

# a = int(input())

# print('*****')
# print(' '+ '****')
# print(' '+' '+'***')
# print(' '+ ' ' +' '+ '**')
# print(' '+ ' '+ ' '+ ' '+ '*')


# a = int(input())

# for i in range(a):
#     print(' ' * i + '*' *(a-i))


# 대표값
# https://www.acmicpc.net/problem/2592
# https://docs.python.org/ko/dev/library/statistics.html

# import statistics 
# a = []

# for i in range(10):
#     num = int(input())
#     a.append(num)

# print(sum(a)//10)
# print(statistics.mode(a))  # 최빈값 구하기 

# 세로읽기
# https://www.acmicpc.net/problem/10798

matrix = []

for _ in range(5):
    word = input()
    matrix.append(word)
for i in range(15):
    for j in range(5):
        # if i < len(matrix[j]):
            print(matrix[j][i], end="")
# ---------

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,0,1,2]
# ]

# for i in range(4):
#     for j in range(3):
#         print(matrix[j][i], end=" ")
#     print()

#  박스 
# https://www.acmicpc.net/problem/9455

# T = int(input())

# for t in range(1,T+1):
