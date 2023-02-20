# 🫧 Subquery

단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법

- 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
- SELECT, FROM, WHERE. HAVING 절 등에서 다양한 맥락에서 사용

---

```SQL
한번에 가장 많은 돈을 소비한 고객번호 조회

SELECT customernumber, amount
FROM payments
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
)

주문한 적이 없는 고객 목록 조회

SELECT customername
FROM customers
WHERE customernumber NOT IN (
    SELECT DISTINCT customerNumber
    FROM orders
);

```

## EXISTS

> 쿼리 문에서 반환된 레코드의 존재 여부를 확인

```SQL
SELECT
    select list
FROM
    table
WHERE
    [NOT]EXISTS(subquery);
```

- subquery가 하나 이상의 행을 반환하며 EXISTS 연산자는
  true를 반환하고 그렇지 않으면 false를 반환
- 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인 하는데 사용

## CASE

> SQL 문에서 조건문을 구성

```SQL
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements

    [ELSE else-statements]
END CASE;
```

```SQL
SELECT ordernumber , status,
    CASE
        WHEN status = 'in process' THEN '주문중'
        WHEN status = 'shipped' THEN '발주완료'
        WHEN status = 'cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS details
FROM orders;
```
