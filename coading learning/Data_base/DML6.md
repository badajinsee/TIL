# π«§ DML

λ°μ΄ν° μ‘°μ (μΆκ°, μμ , μ­μ )

---

## INSERT

> νμ΄λΈ λ μ½λ μ½μ

```SQL
INSERT INTO table_name (c1, c2, ...)
VALUES(v1, v2, ...);
```

```SQL
μλ₯Όλ€μ΄

INSERT INTO
    article(title, content, createdAt)
VALUES
    ('hello', 'world', 'CUTDATE()');

* CURDATE() = νμ¬ λ μ§ λ°ν
```

## UPDATE

> νμ΄λΈ λ μ½λ μμ 

```SQL
UPDATE table_name
SET column_name = expression,
[WHERE
    CONDITION];

SET μ  λ€μμ μμ ν  νλμ μ κ°μ μ§μ νλ€.
WHERE μ μμ μμ  ν  λ μ½λλ₯Ό μ§μ νλ μ‘°κ±΄ μμ±
```

```SQL
μλ₯Όλ€μ΄

UPDATE
    articles
SET
    content = REPLACE(content, 'content', 'TEST');

* REPLACE = μ§μ λ λ¬Έμμ΄ λ³κ²½
```

## DELETE

> νμ΄λΈ λ μ½λ μ­μ 

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
