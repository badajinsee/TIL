# 사용자 정의 클래스 ✔️

객체와 타입
객체 - 특정 타입의 인스턴스 이다.

객체 지향 프로그래밍 - 프로그램을 여러개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

```python
class person:
    pass
print(type(person))
# type
p1 = person()
type(p1)

```

- 특정 기능을 하는 타입(추상화)

```python

class person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greeting_message(self):
        return f'안녕하세요, {self.name}입니다.'

jimin = person('지민','남')
print(jimin.greeting_message())
#안녕하세요, 지민입니다.

jieun = person('지은','여')
print(jieun.greeting_message())
#안녕하세요, 지은입니다.
```

---

## 클래스 ✔️

    # 클래스 정의

    class MyClass:
        pass

    # 인스턴스 생성
    my_instance = MyClass()
    # 메서드 호출
    my_instance.my_method()
    # 속성
    my_instance.my_attribute

---

## 인스턴스 ✔️

인스턴스가 개인적으로 가지고 있는 속성

각 인스턴스들의 고유한 변수

- 생성자 메서드
  인스턴스 객체가 생성될때 자동으로 호출되는 메서드

---

### 클래스와 인스턴스

- 클래스: 객체들의 분류
- 인스턴스: 하나하나의 실체/예

파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스

- 객체 비교하기

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True False

a = [1, 2, 3]
b = a

print(a == b , a is b) # True  True
```

---

나중에 추가 작성 할것 🥹 이해가 안되어소
