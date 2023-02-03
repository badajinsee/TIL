# ✔️ 완전탐색

## 1. 무식하게 풀기 (Brute-force)

- 모든 경우의 수를 탐색하여 문제를 해결하는 방식이다.
- 단순조건문과 반복문을 이용해서 풀 수 있다.
- 아이디어를 어떻게 코드로 구현할 것인지가 중요하다.

```python
ex) 1부터 100까지의 합을 구하라
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
.
.
.
4950 + 100 = 5050
```

### 블랙잭 문제

##### https://www.acmicpc.net/problem/2798

---

```python

def blackhack(n,m,cards):
    max_total = 0

    for i in range(n-2):
        for j in range(j+1, n):
            for k in range(j+1 ,n):
                total = cards[i] + cards[j] + cards[k]

                # 현재 가장 큰 합보다 크고, m을 넘지 않으면 갱신
                if max_total < total <= m:
                    max_total = total
                # 합과 m이 같으면 더이상 탐색 의미 x 종료
                if total == m:
                    return total
    return max_total
```

## 2. 델타 탐색 (delta search)

- 상하좌우 탐색
- (0,0)에서부터 이차원 리스트의 모든 원소를 순회하며 각 지점에서
  상하좌우에 위치한 다른 지점 조회 하거나 이동

```python
3*3 가운데 (1,1) 기준

1) 행을 x , 열을 y로 표현
dx = [-1,1,0,0]
dy = [0,0,-1,1]
      상 하 좌 우

2) 행을 r, 열을 c로 표현
dr = [-1,1,0,0]
dc = [0,0,-1,1]
      상 하 좌 우

# 상(x-1,y)
nx = n + dx[0]
ny = y + dy[0]

# 하(x+1,y)
nx = x + dx[1]
ny = y + dy[1]

# 좌(x,y-1)
nx = x + dx[2]
ny = y + dy[2]

# 우(x,y+1)
nx = x + dx[3]
ny = y + dy[3]

# 상하좌우
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

** 상하좌우로 이동 후 범위를 벗어나지 않는지 확인 및 갱신 필요 !
# 1. 델타값을 이용해 상하좌우로 이동
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

# 2. 범위를 벗어나지 않으면 갱신
if 0 <= nx <3 and 0 <= ny <3:
    x = nx
    y = ny

--------------
정리하자면

이차원 리스트의 상하좌우 탐색

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(n):
    for y in range(m):

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny <m :
                x = nx
                y = ny

# 참고 8방향 델타값

# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]
```
