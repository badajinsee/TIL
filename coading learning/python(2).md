# 📝 파이썬 (제어문,조건문)

## ✔️제어문

---

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행하는 제어가 필요함
- 제어문은 순서도로 표현이 가능

        while 문
        : 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

        for 문
        : 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건이 필요 없음)

        반복제어
        :break, continue, for-else

---

### while 문

- 조건식이 참인 경우 반복적으로 코드를 실행
- 무한 루프를 하지 않도록 종료조건이 반드시 필요 !
  while <expression>:

---

### for 문

- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체 요소를 모두 순회함
- 별도의 종료조건 필요하지 않다.

        for <변수명> in <iterable>:

---

## ✔️조건문

---

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

        기본형식
        if <expression>:

        else:

        복수 조건문
        if <expression>:

        elif <expression>:

        elif <expression>:

        else:

        중첩 조건문
        if <expression>:

            if <expression>:
        else:

## 레인지(Range)

---

        기본형: range(n)
        0부터 n-1까지의 숫자의 시퀀스

        범위 지정: range(n,m)
        n부터 m-1까지의 숫자의 시퀀스

        범위 및 스텝지정: range(n,m,s)
        n부터 m-1 까지 s만큼 증가시키며 숫자의 시퀀스

        변경 불가능하며, 반복 가능함

---

## ✔️함수

---

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

- 함수 기본구조

1. 선언과 호출(define & call)
2. 입력(input)
3. 범위(scope)
4. 결과값(output)

---

## ✔️내장함수

- len(s)
  객체의 길이를 반환합니다. 인자는 시퀀스 또는 컬렉션

- sum(iterable, start=0)
  합계

- max(iterable)
  최대값

- min(iterable)
  최소값

- abs
  절대값

- divmod(a,b)
  두 수를 받아 몫과 나머지 반환

- pow(base, exp, mod=none)
  base의 exp 거듭제곱

* round(number, ndigit=None)
  반올림

- map(function, iterable)
  순회 가능한 데이터구조의 모든 요소에 함수 적용하고 그 결과를 map object로 반환

```python
n, m = map(int,input().split())

print(n,m)
print(type(n),type(m))
```

위에 두개가 같은형식 이다.
