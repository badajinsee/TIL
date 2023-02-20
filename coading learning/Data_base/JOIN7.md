# 🫧 JOIN

둘 이상의 테이블에서 데이터를 검색하는 방법

---

## INNER JOIN

> 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
> (교집합)

```SQL
SELECT
    select_list
FROM
    table1
INNER JOIN table2
    ON table1.fk = table2.pk;
```

- FROM 절 이후 메인 테이블 지정 (table1)
- INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정(table2)

## LEFT JOIN

> 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환 (교집합 + 왼쪽테이블)

```SQL
SELECT
    select_list
FROM
    table1
LEFT JOIN table2
    ON table1.fk = table2.pk;
```

- 왼쪽은 무조건 표시되고, 매치되는 레코드가 없으면 NULL 표시
- 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가
  일치할 경우, 해당 왼쪽 레코드를 여러 번 표시

## RIGHT JOIN

> 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드를 반환 (교집합 + 오른쪽 테이블)

```SQL
SELECT
    select_list
FROM
    table1
RIGHT JOIN table2
    ON table1.fk = table2.pk;
```
