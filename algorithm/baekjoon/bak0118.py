# 9498 시험성적

# score = int(input())

# if score >= 90 and score<= 100:
#     print('A')
# elif score >= 80 and score<= 89:
#     print('B')
# elif score >= 70 and score < 80:
#     print('C')
# elif score >= 60 and score<70:
#     print('D')
# else:
#     print('F')

# 9093 단어 뒤집기

# for _ in range (int(input())):
#     text = input().split()
#     for i in text:
#         print(i[::-1], end= ' ')


# 11721 열 개씩 끊어 출력하기

# 처음 시도 (x)

# text = input()

# a = text[:10]
# b = text[10:20]
# c = text[20:30]
# d = text[30:40]

# if len(text) <= 10:
#     print(a,b, sep= "\n")
    
# else:
#     print(a,b,c,d, sep= "\n")

# --------

# 두번째 시도 (Re 다시)

# text = input()

# for i in range(0,len(text),10): # 0부터 텍스트 길이까지 10자리까지 (시작, 종료, step)
#     print(text[i:i+10]) # 시작값 [0:10] > [10:20] 10개 문자열 출력 

# # 2947 나무조각

# 대충 생각은 드는데 어떻게 풀어야할지 감을 못잡겠다 

## 이렇게 푸는 방법도 있다 . . .
tree = list(map(int,input().split()))

while True:
    for i in range(len(tree)-1): # -1 하는 이유가 뭐지 ? 
        if tree[i] > tree [i+1]:
            tree[i] , tree[i+1] = tree[i+1] , tree[i]
            print(" ".join(map(str, tree)))

    if tree == [1,2,3,4,5]:
        break

# -------

# 이런 방법도 있다ㅏㅇ 
import sys 

tree = list(map(int,input().split()))

while True:     # 반복실행 한다. 
    for i in range(len(tree)-1): # list index out of range = 입력값은 5 인데 레인지는 0 부터라서 -1 
        if tree[i] > tree[i+1]: # tree[0] > tree[1]이 크면 
            temp = tree[i]   # 빈 temp에 tree[0] 넣고 
            tree[i] = tree[i+1] # tree[0] 값엔 tree[1]
            tree[i+1] = temp # tree[1] 엔 temp 값 넣기 
            print(''.join(map(str,tree))) # 정수형이라서 문자로 바꾸고 조인 쓰기 
    if tree == [1,2,3,4,5]: # 트리 리스트가 1,2,3,4,5 되면 브레이크 
        break