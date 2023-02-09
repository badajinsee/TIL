# 🍰 workbench

## 🫧 My sql 실행 & 종료

---

```
# 터미널 입력
mysql.server start

# 터미널 출력
Starting MySQL
. SUCCESS!

==========================

# 터미널 입력
mysql.server stop

# 터미널 출력
Shutting down MySQL
. SUCCESS!
```

## 🫧 실습 데이터 베이스 추가

---

1. My sql 접속하기
2. Administration → Data Import/Restore
3. Import from Self-Contained File 체크  
   → . 클릭
   → 다운로드 받은 sample_db.sql 파일 선택
   → Start Import

## 🫧 쿼리(Query) 실행

---

1. 데이터베이스 선택 **_(classcicmodels)_**
2. query 에디터 클릭하기 (⚡️)
3. 쿼리문 입력하기

```
SELECT * FROM customer;
```

4. 쿼리 실행
5. 출력확인
