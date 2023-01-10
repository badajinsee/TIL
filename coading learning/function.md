# ✔️사용자 정의 함수

함수 function

input -> output

---

## ✔️ 선언과 호출

    함수의 선언은 def 키워드를 활용함
    들여쓰기를 통해 실행코드를 작성함

    함수는 함수명()으로 호출

    def add(x,y):

    return(a+b)

    add (2,3)

```python
num = 0
num = 1

def func1(a, b):
    return a + b
def func2(a, b):
    return a - b

def func3(a, b)
    return func1(a, 5) + func(5, b)

result = func3(num1, num2)
print(result)

= 9
```

```python
def add(a, b): # 정의
    return a + b

print(add)
print(add(-10, -20)) # 호출
print(add(-10, 20))


def cube(a):
    return a**3

print(cube)
print(cube(2))
print(cube(100))

```

### ✔️ return

---

함수는 반드시 값을 **하나**만 return 한다.

함수는 return과 동시에 종료된다.

명시적인 return문 없는 경우 : None

여러 값을 return 하는 경우 : tuple

```python

a = divmod(4, 2) # 몫 나머지
print(a)

=(2,0)
```

- return vs print
  return은 함수 안에서 값을 반환하기 위해 사용하는 키워드
  print는 출력을 위해 사용되는 함수

### ✔️ input

---

parameter: 함수를 실행할때, 함수 내부에서 사용되는 식별자

Argument: 함수를 호출 할 때, 넣어주는 값

```python
def function(ham) # parameter : ham
    return(ham)

function('spam') # argument : 'spam'
```

- keyword arguments (기본값이 있을때)

add (x=2, y=5) 직졉 변수의 이름으로 특정 argument를 전달 할 수 있음

- Default arguments value

기본 값을 지정하여 함수 호출시 arfument 값을 설정하지 않도록 함

정의된 것 보다 더 적은 개수의 arguments들로 호출 될 수 있음

</br>

- 정해지지 않은 arguments

```python

 def add(*numbers): # numbers 타입은 튜플 이다.
    result = 0
    for n in numbers:
        result += n
    return result

print(add(1, 2, 3))
```

- 정해지지 않은 개수의 key word arguments

```python

def movie(**kwargs): # 별이 두개 > 키워드랑 값을 두개 넣어서 사용
    return kwargs # 딕셔너리 타입

print(movie(name='더글로리', writer:'김은숙'))
```

### scope

함수는 코드 내부에 local scope를 생성하고, 그 외의 공간인 global scope로 구분 한다.

```python
# sum : built-in scopte
print(sum([1, 2, 3]))

# sum : global scope
sum = 1 + 2

print(sum([1, 2, 3]))

del sum # 이미 정의 된 함수로 했을 경우 지우고 해야함


a = 5

def foo():
    print(a) # local scope에 a가 없다 > global에서 찾음

foo()
= 5
--------------------------------------------
a = 5
def boo():
    global a
    a = 3
    print(a)
boo()
= 3
print(a)
= 3

```
