# ✔️ **GIT**

GIT은 버전관리를 스냡샷으로 관리한다.

---

</br>

## **-CLI**

명령어 인터페이스

---

### - LS(List)

➡️ 현재 폴더 안에 있는 것

### - mkdir

➡️ 디렉토리 생성, 파일 만들기

### - cd

➡️ 하위 폴더

                cd.. ➡️ 상위 폴더
                cd.  ➡️ 현재 폴더

### - touch a. txt

➡️ 새로운 파일 생성

### - rm

            -rm a.txt
            ➡️ 새로운 파일 삭제

            -rm -r b
            ➡️ 디렉토리 삭제

## **git 기초 흐름**

---

➡️ 변경사항 추적, 여러명의 사용자들 간에 파일들의 작업 효율

</br>

## ✔️ **git 기본 명령어**

---

            1. 작업을 한다.
            2. 변경된 파일을 모은다.(add)
            3. 버전으로 남긴다. (commit)

- get init  
  ➡️ 깃 만들기

- ls al  
  ➡️ 숨긴 폴도 볼수 있음

- git add a. txt.md  
  ➡️ 특정 파일/폴더의 변경 사항 추가

              git add 후에 🔔

              git config --global user. email "이메일주소"
              git config --global user. name "sunjin"
              git config --global -l (알파벳 L)
              ➡️  config 정보 확인이 가능하다.

- git commit -m '<커밋메시지>'  
  ➡️ 커밋(버전기록)

- git status  
  ➡️ 상태확인 (working tree, staging area 까지 확인 가능)

- git log  
  ➡️ 버전 확인 (commit 끝나고 상태확인 할때)

              git log -1 : 최근 1개
              git log --oneline : 한줄로
              git log -2 --oneline : 최근 2개 한줄로

> 🛠 git 이라고 입력시에 명령어들이 나온다

## **파일 상태기록**

---

- nothing to commit, working tree commit clean  
   ➡️ _1통, 2통이 비어 있다는 뜻_

- changes not staged for commit (1통)  
  ➡️ _커밋된 적 있는 보고서 .txt 파일을 수정한 상태_

- changes to be committed (2통)  
  ➡️ _커밋됨, 변경사항들_  
  ➡️ _보고서, txt 만들고 add 함_

</br>

## **파일 관리 상태 라이프 사이클**

---

- Status로 확인할 수 있는 파일의 상태

- Tracked: 이전부터 버전으로 관리되고 있는 파일

        -Unmodified : git status에 나타나지 않음
        -Modified : Changes not staged for commit
        -staged : Changes to be committed

- Untracked : 버전으로 관리된 적 없는 파일 (파일을 새로 만든 경우)
