# 10818 최소, 최대

# a = int(input())
# b = list(map(int,input().split()))

# print(min(b) , max(b))

# 11720 숫자의 합 

# a = int(input())
# b = input()
# total = 0 

# for i in b:
#     total += int(i)
# print(total)

# 다른 방법

# a = int(input())
# print(sum(map(int,input())))

# 2750 수 정렬하기

# a = int(input())
# number = []

# for i in range(a):
#     number.append(int(input()))
# number.sort()

# for i in number:
#     print(i)

# 2562 최대값 (Re)

# 생각을 해보자 최대값은 일단 max 잖아 그리고 그 위치를 알아야해 위치
# 그럼 리스트에 넣어보는건 어떨까 

number = []

for i in range(9):
    number.append(int(input()))

print(max(number))
print(number.index(max(number))+1) # index(x) x값이 있으면 x 위치에 돌려준다. 인덱스는 기본 0부터 시작
# 문제에서 1부터 시작한 인덱스 때문에 +1 을 해준다.