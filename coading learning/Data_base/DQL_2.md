# ๐ซง DISTINCT

- ์กฐํ ๊ฒฐ๊ณผ์์ ์ค๋ณต๋ ๋ ์ฝ๋๋ฅผ ์ ๊ฑฐ

```SQL
SELECT DISTINCT
    select_list
FROM
    table_name;
```

- SELECT ํค์๋ ๋ฐ๋ก ๋ค์ ์ ์ฉ

# ๐ซง WHERE

- ์กฐํ ์ ํน์  ๊ฒ์ ์กฐ๊ฑด์ ์ง์ 

```SQL
SELECT
    select_list
FROM
    table_name;
WHERE
    search_condition;
```

- FROM clause ๋ค์ ์์น
- ๋น๊ต์ฐ์ฐ์ ๋ฐ ๋ผ๋ฆฌ์ฐ์ฐ์(AND, OR, NOT๋ฑ)๋ฅผ ์ฌ์ฉํ๋ ๊ตฌ๋ฌธ์ด ์ฌ์ฉ๋จ

```SQL
* ํ๋ ๊ฐ์ด ์๋ ๊ฒฝ์ฐ

WHERE
    job != 'sales';

* ์ฌ์ด๊ฐ์ผ ๊ฒฝ์ฐ

WHERE
    office BETWEEN 1 AND 4;

= WHERE office >= 1 AND office <=4 ; (๋์ผ)

* ์ฌ๋ฌ๊ฐ์ง ๊ฐ์ผ ๊ฒฝ์ฐ

WHERE
    office IN (1,3,4);

WHERE
    office NOT IN (1,3,4) >> ํฌํจ๋์ง ์๋ ๊ฒฝ์ฐ

* ~๋ก ๋๋๋ ๊ฒฝ์ฐ

WHERE
    lastName LIKE '%son';

WHERE
    phone LIKE '___4' ; >> ์๋ฆฌ์๊ฐ ์ ํด์ ธ ์์ ๊ฒฝ์ฐ

```

- '%' = 0๊ฐ ์ด์์ ๋ฌธ์์ด๊ณผ ์ผ์น ํ๋์ง ํ์ธ
- '\_' = ๋จ์ผ ๋ฌธ์์ ์ผ์น ํ๋์ง ํ์ธ

# ๐ซง lIMIT

- ์กฐํํ๋ ๋ ์ฝ๋ ์๋ฅผ ์ ํ

```SQL
SELECT
    select_list
FROM
    table_name;
LIMIT [offset,] row_count;

LIMIT 3, 5 ์ ๊ฒฝ์ฐ
4 5 6 7 8
```

- LIMIT ํ๋ ๋๋ ๋๊ฐ์ ์ธ์๋ฅผ ์ฌ์ฉ(0 ๋๋ ์์ ์ ์)
- row_count๋ ์กฐํํ  ์ต๋ ๋ ์ฝ๋ ์๋ฅผ ์ง์ 
- ORDER BY ๋ค

# ๐ซง GROUP BY

- ๋ ์ฝ๋๋ฅผ ๊ทธ๋ฃนํํ์ฌ ์์ฝ๋ณธ ์์ฑ with ์ง๊ณ ํจ์

```SQL
SELECT
    c1, c2, . . ., cn, aggregate_function(ci)
FROM
    table_name
GROUP BY
    c1, c2, ..., cn;
```

- FROM ๋ฐ WHERE ์  ๋ค์ ๋ฐฐ์น
- GROUP BY ์  ๋ค์ ๊ทธ๋ฃนํํ  ํ๋ ๋ชฉ๋ก์ ์์ฑ (order by ๋ฑ)

## ๐ซง HAVING

---

- GROUP BY์ ํจ๊ป ์ฌ์ฉํ๋ค GROUP BY๊ฐ ์๋ค๋ฉด WHERE ์ฒ๋ผ ์๋

```SQL
SELECT
    country, AVG(credit)
FROM
    customers
GROUP BY
    country
HAVING
    AVG(credit) > 80000;
```

# ๐ซง SELECT ์คํ์์

    FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY > LIMIT

1. ํ์ด๋ธ์์ (FROM)
2. ํน์  ์กฐ๊ฑด์ ๋ง์ถฐ (WHERE)
3. ๊ทธ๋ฃนํ ํ๊ณ  (GROUP BY)
4. ๋ง์ฝ ๊ทธ๋ฃน์ค์์ ์กฐ๊ฑด์ด ์๋ค๋ฉด ๋ง์ถ๊ณ  (HAVING)
5. ์กฐํํ์ฌ (SELECT)
6. ์ ๋ ฌํ๊ณ  (ORDER BY)
7. ํน์  ์์น์ ๊ฐ์ ๊ฐ์ ธ์จ๋ค (LIMIT)

# ๐ซง ์ ๋ ฌ NULL

- NULL์ NULL์ด ์๋ ๊ฐ ์์ ์์น
- NULL๊ฐ์ด ์กด์ฌํ  ๊ฒฝ์ฐ ์ค๋ฆ์ฐจ์ ์ ๋ ฌ ์ ๊ฒฐ๊ณผ์ NULL์ด ๋จผ์  ์ถ๋ ฅ
