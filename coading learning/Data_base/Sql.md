# 🫧 SQL

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍
- 관계형 데이터베이스와의 대화

## 🫧 SQL Syntax

---

- SQL 언어를 구성하는 가장 기본적인 코드

```
SELECT column_name FROM table_name;

- 대소문자를 구분하지 않음 > 하지만 대문자로 작성하는것을 권장
- SQL Statements의 끝에는 세미콜론(;)이 필요 > Statemen을 구분하는 방법
```

- 위 코드는 SELECT Statement라 부름

</br>

### SQL Statements 유형

---

- DDL - 데이터 정의 > 구조를 정의
- DQL - 데이터 검색 > read
- DML - 데이터 조작 > create, update, delete
- DCL - 데이터 제어 > 컨트롤(권한, 계정)

| 유형 | 역할                                   | SQL 키워드                     |
| ---- | -------------------------------------- | ------------------------------ |
| DDL  | 데이터의 기본 구조 및 형식 변경        | CREATE, DROP, ALTER            |
| DQL  | 데이터 검색                            | SELECT                         |
| DML  | 데이터 조작(추가, 수정, 삭제)          | INSERT, UPDATE, DELETE         |
| DCL  | 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK, GRANT,REVOKE |

---

## 🫧 DQL (Querying data)

- SQL Statement = 테이블에서 데이터를 조회

</br>

### SELECT Syntax

---

```
SELECT
    slect_list
FROM
    table_name;
```

### 별칭 지정

---

```
SELECT
    select_list AS name
FROM
    table_name;
```

## 기본적인 사칙연산 가능

---

```
SELECT
    a * b  AS 총액
FROM
    C;
```

</br>

### ORDER BY Syntax

---

```
SELECT
    slect_list
FROM
    table_name;
ORDER BY
    column1 [ASC|DESC],
    column2 [ASC|DESC],
    ...;

```

- FROM clause 바로 뒤
- ASC : 오름차순 (기본 값)
- DESC : 내림차순
