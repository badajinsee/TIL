# 🫧 DDL

- 데이터의 기본 구 및 형식 변경
- CREATE, DROP, ALTER

</BR>

# 🫧 CREATE

```SQL
CREATE TABLE table_name(
    column_1 data_type,
    column_2 data_type,
    ...,
    constraints
);


CREATE TABLE examples(
    examid INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examid)
);

SHOW COLUMNS FROM examples; > 테이블 구조 확인
```

- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건 작성

</BR>

## ✨ 대표적인 mysql DATA Types

---

- 숫자형 = INT, FLOAT , ...
- 문자형 = VARCHAR, TEXT, ...
- 날짜형 = DATE, DATETIME, ...

## ✨ 대표적인 mysql DATA CONSTRAINTS

---

- PRIMARY KEY = 해당 필드를 기본 키로 지정
- NOT NULL = 해당 필드에 NULL 값을 저장하지 못하도록 지정

---

### ✨ AUTO_INCREMENT

- 기본 키 필드에 사용
- 시작 값은 1 이며 데이터 입력 시 값을 생략하면 자동으로 1 씩 증가
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

# 🫧 DELETE TABLE_DROP

```SQL
DROP TABLE table_name;
```

# 🫧 Modifying TABLE \_ ALTER

```SQL
ALTER TABLE ADD > 필드 추가

ALTER TABLE MODIFY > 필드 속성 변경

ALTER TABLE CHANGE COLUMN > 필드 이름 변경

ALTER TABLE DROP COLUMN > 필드 삭제

```

```SQL
ALTER TABLE
    table_nmae
ADD
    new_column_name column_definition;

* 여러개 추가 할 때

ALTER TABLE
    examples
ADD
    country VARCHAR(100) NOT NULL,
ADD
    address VARCHAR(100) NOT NULL;
```

## ✨ Modify

```SQL
ALTER TABLE
    examples
MODIFY
    address VARCHAR(50) NOT NULL,
MODIFY
    firstName VARCHAR(50) NOT NULL;
```

## ✨ CHANGE COLUMN

```SQL
ALTER TABLE
    examples
CHANGE COLUMN
    country state VARCHAR(100) NOT NULL;
```

> country 필드 이름을 state로 변경

## ✨ ALTER DROP COLUMN

```SQL
ALTER TABLE
    table_name
DROP COLUMN
    column_name;

ALTER TABLE
    examples
DROP COLUMN
    address;

ALTER TABLE
    examples
DROP COLUMN
    state,
DROP COLUMN
    age;

```
