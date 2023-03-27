# Django_model

> DB 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공한다

1. 먼저 app 폴더를 만든다 ( 이름 : articles )

2. app 폴더 내에 models.py 폴더에 작성한다

```
# models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
    content = models.TextField()
```

| id  | title | content |
| --- | ----- | ------- |
| ..  | ..    | ..      |
| ..  | ..    | ..      |

- id 필드는 자동으로 생성된다

- Article은 원하는대로 지으면 된다

- (models.Model)은 Model 이라는 부모 클래스를 상속 받아 작성하는것 이다

- title, content는 클래스 변수명이다. 테이블 각 필드 이름이다.

- CharField, TextField 의 경우는 데이터 타입이다

  [데이터타입 링크](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

- ( ) 안에는 필드옵션을 넣는다 , 제약조건 설정이다.

  [제약조건 링크](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

# Migrations

> model 클래스의 변경사항(필드생성, 추가 수정 등)을 DB에 최종 반영하는 방법

---

1. model class 기반으로 설계도 작성

> python manage.py makemigrations

2. 만들어진 설계도를 DB에 전달하여 반영

> python manage.py migrate

3. DB 내에 생성 된 테이블을 확인한다 !

### 이미 생성된 테이블에 필드 추가할때는 ?

1. models.py에 추가로 작성해준다.

2. **_python manage.py makemigrations _**를 작성한다.

- 기존 테이블이 존재해서 필드 추가할때 기본 값 설정이 필요하다
- 날짜의 경우는 djnago가 제안하는 기본값을 사용하는것이 좋다
- 그 외에는 defalt 값을 설정해서 해준다

ex

```
# models.py

category = models.CharField(max_length=20, default="")

```

3. **_python manage.py migrate_** 작업을 반 드 시 해준다 !
   까먹는다 자주

---

### 데이터 타입

- CharField() : 길이의 제한이 있는 문자열을 넣을때 사용한다 .
  max_length 는 필수 인자이다.

- TextField() : 글자의 수가 많을때 사용한다.

- DateTimeField() : 날짜와 시간을 넣을때 사용

      - datetime 제약조건

         - auto_now : 데이터가 저장될 때마다 자동으로 현재 날짜 시간 저장
         - auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜 시간을 저장

  ***

## Admin site

### Automatic admin interface

> djnango 추가 설치 및 설정 없이 자동으로 관리자 인터페이스 제공

1. admin 계정 생성

> python manage.py createsuperuser

- 이메일 선택사항이라서 입력하지 않고 진행해도 된다
- 비밀번호 생성시 터미널에 출력되지 않는다 입력을 그냥 이어간다.

2. DB에 생성된 admin 계정을 확인한다.

3. admin.py에 모델 클래스를 등록해 준다.

```
from .models imoort Article

admin.site.register(Aricle)
```

---

> python manage.py showmigrations

- migrations 파일들이 migrate 됐는지 여부 확인
- [ x ] 표시가 있으면 migrate 완료

> python manage.py sqlmigrate articles 0001

- 해당 migrations 파일이 SQL 문으로 어떻게 해석 되어 DB에 전달되는지 확인
