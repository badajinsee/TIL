![](https://velog.velcdn.com/images/badajinsee/post/83e486ed-ca47-48c0-a7fc-1c0bff6b087c/image.png)

본인이 실습한 내용 기반으로 작성

# django application

독립적으로 작동하는 기능 단위 모듈 (MTV 패턴에 해당하는 파일 및 폴더를 담당 )
앱은 블로그를 만든다고 치면.. 게시글, 댓글, 카테고리 회원관리 등을 말한다.

### MTV 패턴이란 ?

**MVC는 디자인 패턴 중 하나로 구성 요소를 Model, View, Contriller로 구분한다 **

각각의 구성요소가 다른 요소들에게 영향을 미치지 않는다
시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게
유지보수 할 수 있는 애플리케이션을 만들기 위해

**MTV 패턴은 장고의 디자인 패턴이다 **
명칭이 다를뿐 MVC와 동일하다

**Model **

> DB에 저장되는 데이터를 의미

**Template **

> 유저에게 보여지는 화면

**View**

> 템플릿으로 렌더링하며 응답

![](https://velog.velcdn.com/images/badajinsee/post/984c3561-fea2-4c30-93c6-42c4593f56b2/image.png)

데이터 흐름에 따른 코드를 작성하는게 좋은데

> URLS > VIEW > Template 순으로 작성

```
URLS       path('articles/', views.index),

View      	def index(request):
				return render(request,'articles/index.html')

Template.   articles/templates/articles/index.html

```

---

## ✔️ 앱 생성

- ~~실습할때 서버를 끄고 난후 앱을 생성해야 생겼다 .. 먼가 내가 잘못한걸지도 ..?ㅎ~~

> python manage.py startapp articles

- 앱의 이름은 복수형으로 지정하는것을 권장 한다.

## ✔️ 앱 등록

- settings.py에서 작성한다 !

```
작성순서가 있는데

1. 먼저 Local app 작성
2. 3rd party app (설치를 통해 추가하는 앱)
3. 기본 django app

순으로 작성하기

# settings.py

INSTALLED_APPS = [
	'articles',
    ......,
    .......,
    ]
```

- 앱을 생성하고 등록해야 한다 **반대의 경우 생성 불가능 ~!**

---

## 🔎 프로젝트 구조

- settings.py

프로젝트의 모든 설정을 관리

- urls.py

URL과 이에 해당하는 적절한 views를 연결

## 🔎 앱 구조

- admin.py

관리자용 페이지 설정

- models.py

DB와 관련된 Model을 정의

- Views.py

HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환

---

### URLS

```
from articles import views

urlpatterns = [
	path('articles/', views.index),
    ]
```

- http://128.0.0.1:8000/ **_articles/_** 로 요청이 왔을때, views 모듈의 index 뷰 함수 호출

### View

```
def index(request):
	return render(request, 'articles/index.html')

```

### Template

1. articles 앱 폴더안에 templates 폴더 작성
   ( 주의 : 오타 나지 않도록 작성할것)

2. templates 폴더 안에 템플릿 페이지 작성

_View에 만들기 전에 Template를 만들고 가는게 편함_

---

#### render 함수

```
render(request, template_name, context)
```

- request : 응답을 생성하는 데 사용되는 요청 객체

- template_name : 탬플릿 이름의 경로

- context : 템플릿에서 사용할 데이터
