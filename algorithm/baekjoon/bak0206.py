# 10769 행복한지 슬픈지 

# a =input()

# happy = a.count(":-)")
# sad = a.count(":-(")

# if happy == 0 and sad == 0: 
#     print("none")
# elif happy > sad: 
#     print("happy")
# elif happy == sad: 
#     print("unsure")
# elif happy < sad: 
#     print("sad")


# 2455 지능형 기차 

# train = []
# c = 0
# for i in range(4):
#     a, b = map(int,input().split())
#     c = c - a + b
#     train.append(c)
# print(max(train))

# 바이러스
# ==================== 강사님 풀이 ====================
import sys
sys.stdin = open("input.txt")

# 정점의 수 
n = int(input())

# 간선의 수
m = int(input())

# 그래프 표현 방법 1
# 인접 리스트
# 리스트의 수는 노드의 수 
# n+1 만큼 리스트를 가진 리스트
graph = []
for _ in range(n+1):
    graph.append([])


# 정점의 쌍 입력(간선만큼)
for _ in range(m):
    node1, node2 = list(map(int,input().split()))
    # 양방향 그레프
    graph[node1].append(node2) # node1의 인접리스트에 node 2 추가
    graph[node2].append(node1) # node2의 인접리스트에 node 1 추가

start = 1 # 시작점은 문제에서 줬음 

# 스택 
stack = []
# 방문 여부를 확인할 변수
# visit = [False] * (n+1)
visit = set()

# 시작점 스택에 넣기
stack.append(start)
# 시작점 방문 표시
visit.add(start)

visit_count = 0

# 탬플릿 4번 
while len(stack) != 0 :
    # 탬플릿 5-1 
    current_node = stack.pop()

    # 탬플릿 5-2 
    adj_graph = graph[current_node]

    # 탬플릿 5-3 
    for node in adj_graph:
        # 미방문확인
        if node not in visit:
            # 탬플릿 5-3-1 
            stack.append(node)
            
            # 탬플릿 5-3-2
            visit.add(node)

            # 방문한 횟수 + 1
            visit_count += 1

# 문제에서 요구하는 것 
# 1번 컴퓨터와 연결된 모든 노드의 수 
# 방문한 모든 노드의 수 
# 방문한 횟수 
# 방문한 횟수 == 1번 컴퓨터와 연결된 모든 컴퓨터 수 
print(visit_count)

# ===== 인접 행렬 풀이 ==== 
n = int(input())
m = int(input())

graph = []
for _ in range(n+1):
    temp = [0] * (n+1) # [0,0,0...]
    graph.append()

for _ in range(m):
    node1, node2 = list(map(int,input().split()))

    graph[node1][node2] = 1
    graph[node2][node1] = 1
# 시작점 1 , 스택 , 방문 확인 변수 
start = 1
stack = []
visit = set()

# 시작점을 스택에 넣고, 방문 표시 
stack.append(start)
visit.add(start)
# 무한반복 -> 스택에 값이 있을 때
while len(stack) != 0 :
    # 스택에서 값을 꺼내기
    current_node = stack.pop()

    for index_node in range(n+1):
        # 인접한 정점 > 간선 여부가 1인 
        # 인접 정점 확인 
        if graph[current_node][index_node] == 1:
            # 방문 확인
            if index_node not in visit:
                # 스택에 연결 정점 append
                stack.append(index_node)
                # 인접 정점 방문 표시 
                visit.add(index_node)



# 4693 섬의 개수 





