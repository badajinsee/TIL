# ๐ซง SQL

- ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ ๋ณด๋ฅผ ์ ์ฅํ๊ณ  ์ฒ๋ฆฌํ๊ธฐ ์ํ ํ๋ก๊ทธ๋๋ฐ
- ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค์์ ๋ํ

## ๐ซง SQL Syntax

---

- SQL ์ธ์ด๋ฅผ ๊ตฌ์ฑํ๋ ๊ฐ์ฅ ๊ธฐ๋ณธ์ ์ธ ์ฝ๋

```SQL
SELECT column_name FROM table_name;

- ๋์๋ฌธ์๋ฅผ ๊ตฌ๋ถํ์ง ์์ > ํ์ง๋ง ๋๋ฌธ์๋ก ์์ฑํ๋๊ฒ์ ๊ถ์ฅ
- SQL Statements์ ๋์๋ ์ธ๋ฏธ์ฝ๋ก (;)์ด ํ์ > Statemen์ ๊ตฌ๋ถํ๋ ๋ฐฉ๋ฒ
```

- ์ ์ฝ๋๋ SELECT Statement๋ผ ๋ถ๋ฆ

</br>

### SQL Statements ์ ํ

---

- DDL - ๋ฐ์ดํฐ ์ ์ > ๊ตฌ์กฐ๋ฅผ ์ ์
- DQL - ๋ฐ์ดํฐ ๊ฒ์ > read
- DML - ๋ฐ์ดํฐ ์กฐ์ > create, update, delete
- DCL - ๋ฐ์ดํฐ ์ ์ด > ์ปจํธ๋กค(๊ถํ, ๊ณ์ )

| ์ ํ | ์ญํ                                    | SQL ํค์๋                     |
| ---- | -------------------------------------- | ------------------------------ |
| DDL  | ๋ฐ์ดํฐ์ ๊ธฐ๋ณธ ๊ตฌ์กฐ ๋ฐ ํ์ ๋ณ๊ฒฝ        | CREATE, DROP, ALTER            |
| DQL  | ๋ฐ์ดํฐ ๊ฒ์                            | SELECT                         |
| DML  | ๋ฐ์ดํฐ ์กฐ์(์ถ๊ฐ, ์์ , ์ญ์ )          | INSERT, UPDATE, DELETE         |
| DCL  | ๋ฐ์ดํฐ ๋ฐ ์์์ ๋ํ ์ฌ์ฉ์ ๊ถํ ์ ์ด | COMMIT, ROLLBACK, GRANT,REVOKE |

---

## ๐ซง DQL (Querying data)

- SQL Statement = ํ์ด๋ธ์์ ๋ฐ์ดํฐ๋ฅผ ์กฐํ

</br>

### SELECT Syntax

---

```SQL
SELECT
    slect_list
FROM
    table_name;
```

### ๋ณ์นญ ์ง์ 

---

```SQL
SELECT
    select_list AS name
FROM
    table_name;
```

## ๊ธฐ๋ณธ์ ์ธ ์ฌ์น์ฐ์ฐ ๊ฐ๋ฅ

---

```SQL
SELECT
    a * b  AS ์ด์ก
FROM
    C;
```

</br>

### ORDER BY Syntax

---

```SQL
SELECT
    slect_list
FROM
    table_name;
ORDER BY
    column1 [ASC|DESC],
    column2 [ASC|DESC],
    ...;

```

- FROM clause ๋ฐ๋ก ๋ค
- ASC : ์ค๋ฆ์ฐจ์ (๊ธฐ๋ณธ ๊ฐ)
- DESC : ๋ด๋ฆผ์ฐจ์
