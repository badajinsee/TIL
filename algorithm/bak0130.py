# 1225 이상한 곱셈
# https://www.acmicpc.net/problem/1225

# n, m = input().split()
# a = []
# b = []

# for i in n:
#     a.append(i)
# for j in m:
#     b.append(j)

# c = list(map(int,a))
# d = list(map(int,b))

# print(sum(c) * sum(d))

# 별찍기 - 1
# https://www.acmicpc.net/problem/2438

# a = int(input())

# for i in range(a):
#     i += 1
#     print('*'* i)

# ------------


# 구구단
# https://www.acmicpc.net/problem/2739

# a = int(input())

# for i in range(1,10):

#     print(f'{a} * {i} = {a*i}')

# ------------

# 나는 요리사다 
# https://www.acmicpc.net/problem/2953

b = []
for i in range(5):
    a = list(map(int,input().split()))
    b.append(sum(a))
print(b.index(max(b))+1,max(b))

# 직사각형 네개의 합집합의 면적 
# 모루겠서용
# for i in range(4):
#     x1,y1,x2,y2 = map(int,input().split())


a = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for _ in range(a))]
print(matrix)