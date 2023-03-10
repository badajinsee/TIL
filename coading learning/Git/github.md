# **원격저장소(github)🐙**

### Git은 버전을 관리한다.

### Github도 버전을 관리한다.

---

</br>

# **원격저장소 활용하기**

         - push : 로컬 저장소의 버전을 원격 저장소로 보낸다.
         - Pull : 원격저장소의 버전을 로컬 저장소로 가져온다.

---

- **초기 원격 저장소를 설정한다.**

       - New Repository 눌러서 저장소를 설정한다.
       - URL을 확인해준다.
       - 로컬 저장소에 원격 저장소 정보를 설정한다.

- **로컬저장소 ➡️ 원격저장소 push**

        git remote add <원격저장소(origin)> <url>
        : 깃아 원격저장소 추가해줘 Origin으로 Url 을

        git remote -v
        : 위 설정이 잘 되어 있는지 확인, 원격 저장소 정보 확인

        git remote rm <원격저장소(origin)>
        : 원격저장소 삭제


        git push <원격저장소(origin)> <브랜치(main)>
        : 원격저장소에 push

  ### _주의점 : push 할 때는 인증 정보가 필수적이여야 한다._

* Q&A

        수정 후는 어떻게 해야할까 ?
        ➡️ 수정 후 > git status(확인) > git add . > git commit -m '텍스트' > git push main
        (git init은 git 파일을 생성하는것 이기 때문에 안해도 된다.)

  </br>

- **원격저장소 ➡️ 로컬저장소 Pull**

        git pull <원격저장소(origin)> main
        : 원격저장소에 pull

---

- _push 실패_

1.  원격 저장소의 커밋을 원격저장소로 가져와서(pull)
2.  로컬에서 두커밋을 병합 (추가 커밋 발생)

- 동시에 같은 파일이 수정된 경우 merge conflict가 발생하나 이 부분은 브랜치 학습

3.  다시 GitHub으로 push

---

## **git clone**

협업 프로젝트, 외부 오픈소스 참여 Git 저장소를 GitHub에서 생성 후 시작

| **gitclone**                             | **다운로드(zip)**                         |
| ---------------------------------------- | ----------------------------------------- |
| git 저장소를 받아오는 것, 모든 버전 다운 | (가장최신버전 상태의) 파일만 다운 받는 것 |

</br>

---

## **gitignore**

버전관리와 상관없는 파일

            .gitignore : 파일 만들어서 적으면 깃 버전 관리가 x

_git ignore을 미리 만들어서 커밋하는 상황을 방지하자_

[⭐️이그노어 참조사이트](https://gitignore.io/)

---

[🪐git 초심자사이트](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)
[🌎git 책](https://git-scm.com/book/ko/v2/시작하기-버전-관리란%3F)
