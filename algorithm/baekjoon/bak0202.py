# 공 
# a = int(input()) # 횟수 
# w = [1, 2, 3]
# for i in range(a):
#     b, c = map(int,input().split())
#     d = w.index(b)
#     e = w.index(c)
#     w[d], w[e] = w[e],w[d]
# print(w[0])


# 콘테스트
# https://docs.python.org/ko/3/howto/sorting.html#ascending-and-descending

# w = []
# k = []

# for i in range(10):
#     a = int(input())
#     w.append(a)
# for j in range(10):
#     b = int(input())
#     k.append(b)

# w = sorted(w,reverse=True) # 내림차순 , False는 오름차순
# k = sorted(k,reverse=True) 

# w_sum = 0
# k_sum = 0

# for n in range(3):
#     w_sum += w[n]
# for m in range(3):
#     k_sum += k[m]

# print (w_sum, k_sum)

# 오르막길 

n = int(input())
a = list(map(int,input().split()))
b = 0
c =[]
for i in range(n-1):
    if a[i] < a[i+1]:
        b += a[i+1] - a[i]
    else:
        c.append(b)
        b = 0
c.append(b)
print(max(c))


# # 단어 나누기

word = input()
word_li =[]
for i in range(len(word)-2):
    for j in range(i+1,len(word)-1):
        for k in range(j+1,len(word)):
            a = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
        word_li.append(a)
b = sorted(word_li)
print(b[0])

# 어려우ㅝ용 