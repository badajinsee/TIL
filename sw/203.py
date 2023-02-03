# 파리퇴치 

# T = int(input())

# for t in range(1,T+1):
#     a, b = list(map(int,input().split()))
#     c = [[0]*a for _ in range(a)]
#     for i in range(a):
#         c[i] = list(map(int,input().split()))
    
#     for i in range(a-b+1):
#         for j in range(a-b+1):
#             cnt = 0

# 모르겠어요 . . . . .... ....... 

# 조교의 성적 매기기

# T = int(input())

# grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     totals = []

#     for _ in range(N): 
#         a, b, c = map(int, input().split())
#         total = (a * 0.35) + (b * 0.45) + (c*0.2)
#         totals.append(total)
     
#     k_score = totals[K-1] # 0부터 -1
    
#     totals.sort(reverse=True)  # 내림차순
    
#     div = N//10
#     final_k_score = totals.index(k_score) // div

#     print('#{} {}'.format(t, grade[final_k_score]))

# 민석이의 과제 체크하기 

# T = int(input())

# for t in range(1,T+1):
#     # 수강생수 , 과제 제출한 사람 
    # a, b = list(map(int,input().split()))
#     # 제출 사람 번호 
#     c = list(map(int,input().split()))
#     d = []
#     for i in range(1,a+1):
#         if i not in c :
#             d.append(i)
#     print(f'#{t}', *d)

# 암호생성기 

# T = 10

# for t in range(1,T+1):
#     n = input()
#     a = list(map(int,input().split()))

#     while True:
#         for i in range(1,6):
#             n = a.pop(0)
            
#     print(f'#{t}')
# ㅎㅎ.. 덜 풀었어요 

# 단어

# T = int(input())

# for t in range(1, T+1):
#     N, K = map(int, input().split())

#     a = [[''] * N for _ in range(N)]


