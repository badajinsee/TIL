# 1. 공백으로 구분된 정수

numbers = list(map(int,input().split()))

print(*numbers)

# 2. 공백으로 구분된 문자열

string = input().split()

print(*string)

# 3. 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T = int(input())
for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        number = int(input())
        print(number)

# 4. 테스터 케이스 수와 입력 줄 수가 주어지는 입력

T = int(input())

for t in range(1,T+1):
    N = int(input())
    for i in range(N):
        number =list(map(int, input().split()))
        print(number)

# 5 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# T = int(input())

# for t in range(1,T+1):
#     N = int(input())
#     for i in range(N):
#         string = input().split()
#         print(*string)

# 6 테스트 케이스 수와 입력 줄 수가 주어지는 입력 
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     for _ in range(N):
#         numbers = list(map(int,input().split()))
#         print(*numbers)

# 7 
# T, N = list(map(int,input().split()))

# for t in range(1, T+1):
#     for _ in range(1,N+1):
#         number = int(input())
#         print(number)

# 8 
# T, N = list(map(int,input().split()))

# for t in range(1, T+1):
#     for _ in range(1,N+1):
#         number = int(input())
#         print(number)

# 9 
T, N  = list(map(int,input().split()))

for t in range(1,T+1):
    for _ in range(1,N+1):
        numbers = list(map(int,input().split()))
        print(numbers)