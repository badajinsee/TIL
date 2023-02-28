# 2676 홀수
# https://www.acmicpc.net/problem/2576

# number=[]
# for i in range(7):
#     a = int(input())
#     if a % 2 == 1:
#         number.append(a)
# if number:
#     print(sum(number))
#     print(min(number))
# else:
#     print(-1)

# 10822 더하기
# https://www.acmicpc.net/problem/10822

# num = map(int,input().split(","))
# print(sum(num))

# 2574 학점계산
# https://www.acmicpc.net/problem/2754

# score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,

#         'B+': 3.3, 'B0': 3.0, 'B-': 2.7,

#         'C+': 2.3, 'C0': 2.0, 'C-': 1.7,

#         'D+': 1.3, 'D0': 1.0, 'D-': 0.7,

#         'F': 0.0}

# a = input()
# print(score[a])

# 5622 다이얼
# https://www.acmicpc.net/problem/5622

number={"A": 3, "B": 3, "C": 3,
        "D": 4, "E": 4, "F": 4,
        "G": 5, "H": 5, "I": 5,
        "J": 6, "K": 6, "L": 6,
        "M": 7, "N": 7, "O": 7,
        "P": 8, "Q": 8, "R": 8, "S": 8,
        "T": 9, "U": 9, "V": 9,
        "W": 10, "X": 10, "Y": 10, "Z": 10}
count = 0
push = input()
 
for i in push:
    count +=  number.get(i)

print(count)

# 숫자의 개수
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

x = str(a * b * c)

for i in range(10): # 0부터 9 까지 
   print(x.count(str(i)))

# 회사에 있는 사람 (모르겠ㄴ음ㄴ데여 ㅠ)