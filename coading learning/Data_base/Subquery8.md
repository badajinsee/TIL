# ๐ซง Subquery

๋จ์ผ ์ฟผ๋ฆฌ๋ฌธ์ ์ฌ๋ฌ ํ์ด๋ธ์ ๋ฐ์ดํฐ๋ฅผ ๊ฒฐํฉํ๋ ๋ฐฉ๋ฒ

- ์กฐ๊ฑด์ ๋ฐ๋ผ ํ๋ ์ด์์ ํ์ด๋ธ์์ ๋ฐ์ดํฐ๋ฅผ ๊ฒ์ํ๋ ๋ฐ ์ฌ์ฉ
- SELECT, FROM, WHERE. HAVING ์  ๋ฑ์์ ๋ค์ํ ๋งฅ๋ฝ์์ ์ฌ์ฉ

---

```SQL
ํ๋ฒ์ ๊ฐ์ฅ ๋ง์ ๋์ ์๋นํ ๊ณ ๊ฐ๋ฒํธ ์กฐํ

SELECT customernumber, amount
FROM payments
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
)

์ฃผ๋ฌธํ ์ ์ด ์๋ ๊ณ ๊ฐ ๋ชฉ๋ก ์กฐํ

SELECT customername
FROM customers
WHERE customernumber NOT IN (
    SELECT DISTINCT customerNumber
    FROM orders
);

```

## EXISTS

> ์ฟผ๋ฆฌ ๋ฌธ์์ ๋ฐํ๋ ๋ ์ฝ๋์ ์กด์ฌ ์ฌ๋ถ๋ฅผ ํ์ธ

```SQL
SELECT
    select list
FROM
    table
WHERE
    [NOT]EXISTS(subquery);
```

- subquery๊ฐ ํ๋ ์ด์์ ํ์ ๋ฐํํ๋ฉฐ EXISTS ์ฐ์ฐ์๋
  true๋ฅผ ๋ฐํํ๊ณ  ๊ทธ๋ ์ง ์์ผ๋ฉด false๋ฅผ ๋ฐํ
- ์ฃผ๋ก WHERE ์ ์์ subquery์ ๋ฐํ ๊ฐ ์กด์ฌ ์ฌ๋ถ๋ฅผ ํ์ธ ํ๋๋ฐ ์ฌ์ฉ

## CASE

> SQL ๋ฌธ์์ ์กฐ๊ฑด๋ฌธ์ ๊ตฌ์ฑ

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
        WHEN status = 'in process' THEN '์ฃผ๋ฌธ์ค'
        WHEN status = 'shipped' THEN '๋ฐ์ฃผ์๋ฃ'
        WHEN status = 'cancelled' THEN '์ฃผ๋ฌธ์ทจ์'
        ELSE '๊ธฐํ์ฌ์ '
    END AS details
FROM orders;
```
