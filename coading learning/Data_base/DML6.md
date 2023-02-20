# 🫧 DML

데이터 조작 (추가, 수정, 삭제)

---

## INSERT

> 테이블 레코드 삽입

```SQL
INSERT INTO table_name (c1, c2, ...)
VALUES(v1, v2, ...);
```

```SQL
예를들어

INSERT INTO
    article(title, content, createdAt)
VALUES
    ('hello', 'world', 'CUTDATE()');

* CURDATE() = 현재 날짜 반환
```

## UPDATE

> 테이블 레코드 수정

```SQL
UPDATE table_name
SET column_name = expression,
[WHERE
    CONDITION];

SET 절 다음에 수정할 필드와 새 값을 지정한다.
WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
```

```SQL
예를들어

UPDATE
    articles
SET
    content = REPLACE(content, 'content', 'TEST');

* REPLACE = 지정된 문자열 변경
```

## DELETE

> 테이블 레코드 삭제

```SQL
DELETE FROM table_name
[WHERE
    CONDITION];
```

```SQL
DELETE FROM
    articles
ORDER BY
    createdAt DESC
LIMIT 2;
```
