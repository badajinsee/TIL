# variable routing

url 일부에 변수를 포함시키는 것을 나타낸다.

1. urls 작성하기
   ![](https://velog.velcdn.com/images/badajinsee/post/690c8ec5-9e41-4652-8665-930ee4049c48/image.png)

- <path\_ converter:variable_name> 형식으로 작성하기
- [path coverters](https://docs.djangoproject.com/ko/3.2/topics/http/urls/) 는 5가지 타입으로 지원해준다

2. views 작성하기
   ![](https://velog.velcdn.com/images/badajinsee/post/8e648ae3-2790-4a4e-92c2-2b78cdf3ba55/image.png)

3. templates 작성하기

- 까먹지 말것 **app폴더에 만들어야 한다** !!!!!

주소 입력을 해주면

![](https://velog.velcdn.com/images/badajinsee/post/c8fe7bac-6b30-473c-82c5-d2a3eaca49a9/image.png)
![](https://velog.velcdn.com/images/badajinsee/post/c14756e6-e908-445f-8244-6b195ab713ba/image.png)

이런 형식으로 나온당 ~!

---

# App URL mapping

- 각 앱에 URL을 정의하는것을 말한다
- 앱 두번째를 생성하였을때 URL 주소가 겹친다면 각자 app에서 url을 관리하는게 좋다

---

일단 앱 하나로만 해보자

1. 앱에 urls.py를 생성한다

   ![](https://velog.velcdn.com/images/badajinsee/post/51e942fe-80ae-4ef2-a56c-cefb66834cae/image.png)

2. 새로만든 앱에 있는 urls.py에 프로젝트 파일에 있는 urls.py에
   박스 부분을 복사를 해서 가져다 붙인다 (밑줄 부분 제외 !! )

   ![](https://velog.velcdn.com/images/badajinsee/post/448c0f43-0cce-4ac0-9b2c-0ded34d6ebe3/image.png)

3. 프로젝트에 있는 urls.py에 **include**를 사용해준다

   ![](https://velog.velcdn.com/images/badajinsee/post/d7b139a1-91a9-4213-a746-c53ae7888611/image.png)

### include() 란

> 다른 URL들을 참조할수 있도록 돕는 함수이다 !
> ( URL 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을
> 후속 처리를 위해 include된 URL로 전달한다)

자 그럼 프로젝트에 있는 urls.py와 app에 작성한 urls.py를 비교 해보자
![](https://velog.velcdn.com/images/badajinsee/post/9ce710d2-8032-45ac-89c4-275b2a6e44f3/image.png)

검색을 하게되면 이런식으로 경로를 다시 찾아갈수가 있다 !
![](https://velog.velcdn.com/images/badajinsee/post/8c801123-a024-4a5f-8e0f-04fa3b42850b/image.png)

---

## Naming url patterns

> url에 이름을 지정하는 것

1. urls.py 변수에 name='아무이름' 형식으로 작성한다

![](https://velog.velcdn.com/images/badajinsee/post/7b084cc5-7ce2-4517-a430-f8adea2b0ee8/image.png)

2. html 파일에 넣는다

### url 태그

> 주어진 url 패턴의 이름과 일치하는 절대 경로 주소를 반환
> {% url 'url-name' arg1 arg2 % }

![](https://velog.velcdn.com/images/badajinsee/post/bcc9f270-2901-404a-ad8f-72fc9aa68347/image.png)

나의 경우엔 아까 위의 두 태그를 했는데, detail은 숫자를 입력해야 하기 때문에 임시값으로 num=1 을 주었다 !!!

3. 결과

![](https://velog.velcdn.com/images/badajinsee/post/b56f89b5-b646-4bf2-95c0-00545156c859/image.png)

이런식으로 name 이라고 이름을 지정했기 때문에 링크가 출력된다

![](https://velog.velcdn.com/images/badajinsee/post/47381a1a-62e7-4dec-a25b-679f61d3d63c/image.png)

누르면 아까 num=1 이라고 했기때문에 이렇게 출력이 된다.

---

# URL Namespace

그치만 ! app이 두개라면 그리고 url의 이름이 같다면 ? 이름으로만으로 분류하기는 어려워진다

#### 그럴때는 app_name 속성을 지정해 주면 된다.

1. urls.py에 app_name 속성 지정 변경

![](https://velog.velcdn.com/images/badajinsee/post/85501167-9e25-46d6-96d0-0b09783d4eac/image.png)

2. url tag 변경

![](https://velog.velcdn.com/images/badajinsee/post/332ee64f-afab-497d-b3ee-5f8f02b5bc0f/image.png)
