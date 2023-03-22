어려워졌어 나 어쩜 좋아 나 어쩜 좋아 나 어쩜 좋아 나 어쩜 좋아 

# template sysyem 

> 데이터 표현을 제어하면서, 표현과 관련된 로직을 담당 

---

## template launguage
> template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템 

- variable 

	{{ variable }}

- filters 

	{{ name | filter }}

- tags 

	{ % tag % }
    
- comments 

	그냥 주석 
    
---
### 템플릿 상속 

페이지 공통요소 포함, 하위 템플릿 재정의 할 수 있는 공간 정의

1. base html 생성  

2. 하위 템플릿 상속 tag 사용하기 

		{ % extends 'base.html' % } 
 자식이 부모 확장한다는것** 반 드 시 최상단에 적을것**
        
3. 블록 정의하기 

		{% block content %} {% endblock content %}
 content 위에 적어서 style로 나타낼수 있음 
 
		{% block style %} {% endblock style %}
 ----
 
## Form element

> 사용자로부터 할당된 데이터 서버로 전송 

|action|method|
|------|------|
|입력 데이터 전송 url 지정| 데이터 request methods(GET,POST) 지정|

---
## Input  element 

> 데이터 입력 받을수 있는 요소 (type에 따라 다양한 유형 입력 데이터 있음)

### name 

name 속성에 설정된 값을 통해 데이터 접근 할수 있음

```
html 

<form action="" method="GET">
	<input type ="text" name="message" id = "massage">
</form>
```

#### query string parameters 

- Key = value 쌍으로 구성 기본 url 과는 물음표(?)로 구분됨 

- http://host:port/path?key=value&key=value 이런 식으로 

---

## 요청과 응답 

first 와 sec 두개 작성

``` 
html

# 첫번째 html

<form action="/sec/" method="GET">
	<input type="text" name ="message">
 </form>
 
 # 두번째 view 
 
 def sec(request):
 	message = request.GET.get('message')
    context = {
    	'message' : message,
     }
     return render(request, 'sec.html', context)
     
 # 두번째 html
 
 <h1> {{ message }} </h1>
 
 ```