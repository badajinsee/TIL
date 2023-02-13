# 🫧 DISTINCT

- 조회 결과에서 중복된 레코드를 제거

```
SELECT DISTINCT
    select_list
FROM
    table_name;
```

- SELECT 키워드 바로 뒤에 적용

# 🫧 WHERE

- 조회 시 특정 검색 조건을 지정

```
SELECT
    select_list
FROM
    table_name;
WHERE
    search_condition;
```

- FROM clause 뒤에 위치
- 비교연산자 및 논리연산자(AND, OR, NOT등)를 사용하는 구문이 사용됨

```
* 필드 값이 아닐 경우

WHERE
    job != 'sales';

* 사이값일 경우

WHERE
    office BETWEEN 1 AND 4;

= WHERE office >= 1 AND office <=4 ; (동일)

* 여러가지 값일 경우

WHERE
    office IN (1,3,4);

WHERE
    office NOT IN (1,3,4) >> 포함되지 않는 경우

* ~로 끝나는 경우

WHERE
    lastName LIKE '%son';

WHERE
    phone LIKE '___4' ; >> 자리수가 정해져 있을 경우

```

- '%' = 0개 이상의 문자열과 일치 하는지 확인
- '\_' = 단일 문자와 일치 하는지 확인

# 🫧 lIMIT

- 조회하는 레코드 수를 제한

```
SELECT
    select_list
FROM
    table_name;
LIMIT [offset,] row_count;

LIMIT 3, 5 의 경우
4 5 6 7 8
```

- LIMIT 하나 또는 두개의 인자를 사용(0 또는 양의 정수)
- row_count는 조회할 최대 레코드 수를 지정
- ORDER BY 뒤

# 🫧 GROUP BY

- 레코드를 그룹화하여 요약본 생성 with 집계 함수

```
SELECT
    c1, c2, . . ., cn, aggregate_function(ci)
FROM
    table_name
GROUP BY
    c1, c2, ..., cn;
```

- FROM 및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화할 필드 목록을 작성 (order by 등)

## 🫧 HAVING

---

- GROUP BY와 함께 사용한다 GROUP BY가 없다면 WHERE 처럼 작동

```
SELECT
    country, AVG(credit)
FROM
    customers
GROUP BY
    country
HAVING
    AVG(credit) > 80000;
```

# 🫧 SELECT 실행순서

    FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY > LIMIT

1. 테이블에서 (FROM)
2. 특정 조건에 맞춰 (WHERE)
3. 그룹화 하고 (GROUP BY)
4. 만약 그룹중에서 조건이 있다면 맞추고 (HAVING)
5. 조회하여 (SELECT)
6. 정렬하고 (ORDER BY)
7. 특정 위치의 값을 가져온다 (LIMIT)

# 🫧 정렬 NULL

- NULL은 NULL이 아닌 값 앞에 위치
- NULL값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
