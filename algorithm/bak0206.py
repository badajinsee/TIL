# 10769 행복한지 슬픈지 

a =input()

happy = a.count(":-)")
sad = a.count(":-(")

if happy == 0 and sad == 0: 
    print("none")
elif happy > sad: 
    print("happy")
elif happy == sad: 
    print("unsure")
elif happy < sad: 
    print("sad")


# 2455 지능형 기차 

train = []
c = 0
for i in range(4):
    a, b = map(int,input().split())
    c = c - a + b
    train.append(c)
print(max(train))

# 2606 바이러스 (런타임 오륲)

n = int(input()) 
v = int(input()) 
visited=[0]*(n+1) 
graph = [[] for i in range(n+1)] 
for i in range(v): # 그래프 생성
    a, b=map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a) 

def dfs(start):
    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = 1
                stack.append(adj)
                
dfs(1)
print(sum(visited)-1)

# 4693 섬의 개수 





