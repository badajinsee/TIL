# π«§ DDL

- λ°μ΄ν°μ κΈ°λ³Έ κ΅¬ λ° νμ λ³κ²½
- CREATE, DROP, ALTER

</BR>

# π«§ CREATE

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

SHOW COLUMNS FROM examples; > νμ΄λΈ κ΅¬μ‘° νμΈ
```

- κ° νλμ μ μ©ν  λ°μ΄ν° νμ μμ±
- νμ΄λΈ λ° νλμ λν μ μ½μ‘°κ±΄ μμ±

</BR>

## β¨ λνμ μΈ mysql DATA Types

---

- μ«μν = INT, FLOAT , ...
- λ¬Έμν = VARCHAR, TEXT, ...
- λ μ§ν = DATE, DATETIME, ...

## β¨ λνμ μΈ mysql DATA CONSTRAINTS

---

- PRIMARY KEY = ν΄λΉ νλλ₯Ό κΈ°λ³Έ ν€λ‘ μ§μ 
- NOT NULL = ν΄λΉ νλμ NULL κ°μ μ μ₯νμ§ λͺ»νλλ‘ μ§μ 

---

### β¨ AUTO_INCREMENT

- κΈ°λ³Έ ν€ νλμ μ¬μ©
- μμ κ°μ 1 μ΄λ©° λ°μ΄ν° μλ ₯ μ κ°μ μλ΅νλ©΄ μλμΌλ‘ 1 μ© μ¦κ°
- μ΄λ―Έ μ¬μ©ν κ°μ μ¬μ¬μ©νμ§ μμ
- κΈ°λ³Έμ μΌλ‘ NOT NULL μ μ½ μ‘°κ±΄μ ν¬ν¨

# π«§ DELETE TABLE_DROP

```SQL
DROP TABLE table_name;
```

# π«§ Modifying TABLE \_ ALTER

```SQL
ALTER TABLE ADD > νλ μΆκ°

ALTER TABLE MODIFY > νλ μμ± λ³κ²½

ALTER TABLE CHANGE COLUMN > νλ μ΄λ¦ λ³κ²½

ALTER TABLE DROP COLUMN > νλ μ­μ 

```

```SQL
ALTER TABLE
    table_nmae
ADD
    new_column_name column_definition;

* μ¬λ¬κ° μΆκ° ν  λ

ALTER TABLE
    examples
ADD
    country VARCHAR(100) NOT NULL,
ADD
    address VARCHAR(100) NOT NULL;
```

## β¨ Modify

```SQL
ALTER TABLE
    examples
MODIFY
    address VARCHAR(50) NOT NULL,
MODIFY
    firstName VARCHAR(50) NOT NULL;
```

## β¨ CHANGE COLUMN

```SQL
ALTER TABLE
    examples
CHANGE COLUMN
    country state VARCHAR(100) NOT NULL;
```

> country νλ μ΄λ¦μ stateλ‘ λ³κ²½

## β¨ ALTER DROP COLUMN

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
