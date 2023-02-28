# 반반 

# T = int(input())

# for t in range(1, T+1):
#     string = sorted(list(input()))

#     if string[0] == string[1] and string[2] == string[3] and string[1] != string[2]:
#         print(f'#{t} Yes')
#     else:
#         print(f'#{t} No')

# 모음이 보이지 않는 사람 

# T = int(input())

# a = ['a','e','i','o','u']

# for t in range(1, T+1):
#     string = input()
#     result =''
#     for i in range(len(string)):
#         if string[i] in a:
#             continue
#         result += string[i]
#     print(f'#{t} {result}')

# 퍼펙트 셔플 

T = int(input())
for tc in range(1,T+1):
    
    N = int(input())
    card = input().split()

    result = ['']*len(card)
    
    if N%2:
        for i in range(N//2+1):
            result[2*i] = card[i]
        for i in range(N//2):
            result[2*i+1] = card[i+N//2+1]
   
    else:
        for i in range(N//2):
            result[2*i] = card[i]
            result[2*i+1] = card[i+N//2]

    print(f'#{tc}',*result)