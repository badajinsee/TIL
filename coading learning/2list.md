# ✔️ 이차원 리스트

이차원 리스트는 리스트를 원소로 가지는 리스트 이다.

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])
>>> 1
print(matrix[1][2])
>>> 6
print(matrix[2][0])
>>> 7

보기 좋게 변경하면 행렬 형태로 나온다.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

### 특정 값으로 초기화 된 이차원 리스트를 만들어 보자

```python

# 반복문을 통해 작성할수 있다

100*100

matrix = []

for _ in range(100):
    matrix.append([0]*100)


n = 4 #행
m = 3 #열
matrix =[]

for _ in range(n):
    matrix.append([0]*m)

print(matrix)
>>> [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# 여기서 리스트 컴프리헨션으로 작성해보자

n = 4
m = 3
matrix = [[0]* m for _ in range(n)]

print(matrix)
>>>[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

```

### 행렬의 크기가 입력으로 주어지는 경우

```python

3 4
1 2 3 4
5 6 7 8
9 0 1 2

n,m = map(int,input().split())
matrix = []

for _ in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)


# 컴프리헨션으로 변경하면

matrix = [list(map(int,input().split())) for _ in range(n)]
```

# ✔️ 순회

## 1. 행 우선 순회

```python

# 이중 for문을 이용한 행 우선 순회
3 * 4
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

for i in range(3): # 행 = 매트릭스 전체 길이 3개 len(matrix)
    for j in range(4): # 열 = 매트릭스 안에 있는 길이 len(matrix[0])
        print(matrix[i][j],end=" ")
    print()

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2

```

## 2. 열 우선 순회

```python

# 이중 for문을 이용한 열 우선 순회

matrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

for i in range(4): # 열
    for j in range(3): # 행
        print(matrix[j][i], end=" ")
    print()

>>> 1 5 9
>>> 2 6 0
>>> 3 7 1
>>> 4 8 2
```

## 행 우선 순회를 이용해 이차원 리스트의 총합 구하기

```python

matrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]

total = 0

for i in range(3):
    for j in range(4):
        total += matrix[i][j]

print(total)
>>> 12

# 다른 방법
total = sum(map(sum,matrix)
print(total)
>>> 12

```

### 순회를 통하여 최대값, 최소값 구하기

```python
# 최대값
matrix = [
    [0,5,3,1],
    [4,5,10,8],
    [9,-1,1,5]
]

max_value = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
print(max_value)
>>>10


# 최소값
matrix = [
    [0,5,3,1],
    [4,6,10,8]
    [9,-1,1,5]
]

min_value = 99999999

for i in range(3):
    for j in range(4):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
print(min_value)
>>> -1

# 다른 방법 함께 구하기
matrix = [
    [0,5,3,1],
    [4,6,10,8]
    [9,-1,1,5]
]

max_value = max(map(max,matrix))
min_value = min(map(min,matrix))

print(max_value)
>>> 10
print(min_value)
>>> -1
```

# ✔️ 전치

행과 열을 서로 맞바꾸는것을 의미

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

transposed_matrix = [[0] * 3 for _ in range(4)]
# 행과 열 크기가 반대

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i]
        # 행, 열 맞바꾸기

>>> transposed_matrix = [
    [1,5,9],
    [2,6,0],
    [3,7,1],
    [4,8,2]
]
```

# ✔️ 회전

왼쪽, 오른쪽으로 90도 회전하는 경우

```python
1. 왼쪽으로 90도 회전하기

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = 3
rotated_matrix = [[0] * n for_ in range(n)]

for i in range(n):
    for j in range(n):
        ratated_matrix[i][j] = matrix[j][n-i-1]

>>> rotated_matrix =[
    [3,6,9],
    [2,5,8],
    [1,4,7]
]

2. 오른쪽으로 90도 회전하기
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = 3
rotated_matrix = [[0] * n for_ in range(n)]
for i in range(n):
    for j in range(n):
        ratated_matrix[i][j] = matrix[n-j-1][i]

>>> rotated_matrix = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

```
