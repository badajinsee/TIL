# λμλλ¦¬π―

ν€-κ° μμΌλ‘ μ΄λ€μ§ λͺ¨μ

    ν€ :λΆλ³ μλ£νλ§ κ°λ₯

    κ° : μ΄λ ν ννλ  κ΄κ³ μμ

    λ³κ²½ κ°λ₯νλ©°, λ°λ³΅ κ°λ₯ν¨

## λμλλ¦¬ μν

---

- keys() : keyλ‘ κ΅¬μ±λ κ²°κ³Ό

- value(): valueλ‘ κ΅¬μ±λ κ²°κ³Ό

- items(): (key, value)μ ννλ‘ κ΅¬μ±λ κ²°κ³Ό

```python
grages = {'john':80, 'eric': 90}
print(grades.keys())
print(grades.value())
print(grages.items())

# dict_keys(['john','eric'])
# dict_values([80, 90])
# dict_items([('john', 80),('eric', 90)])

# λμλλ¦¬ λ¦¬μ€νΈ μ΄κ±°
fruits = {'banana':300 , 'apple' : 200, 'mango':400}

list(fruits.keys())
['banana', 'apple', 'mango']

sorted(fruits.keys()) # μ λ ¬λ λͺ©λ‘μ λ¦¬μ€νΈ νμΌλ‘ μ»μ΄λΈλ€

#['apple', 'banana', 'mango']



# for κ΅¬λ¬Έκ³Ό ν¨κ»
fruits = {
    'λ°λλ':3000,
    'μ€λ μ§':2400,
    'λΈκΈ°':3500,
    'λ§κ³ ':4000
}

for name in fruits.keys():
    price = fruits[name]
    s = '{0}λ {1}μ μλλ€.'.format(name, price)
    print(s)

# λ°λλλ 3000μ μλλ€. λ±λ± μΆλ ₯

# λ€λ₯Έ λ°©λ²
    for name, price in fruits.items():
        s = '{0}λ {1}μ μλλ€.'.format(name,price)
    print(s)



```

- for ν€, κ° in λμλλ¦¬.items(): # ν€μ κ°μ μ΄μ©ν μ²λ¦¬

```python
# μλ¨μ΄μ μΆμ°νλ νμ

text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# λ¨μ΄ κ΅¬λΆ
text = text.replace(";","")
text = text.replace(",","")
text = text.replave(".","")
words = text.split()

counter = {} # λΉ λμλλ¦¬ μμ±
for w in words:
    ws = w.lower() # μλ¬Έμλ‘ λ³ν
    if ws in counter: # λμλλ¦¬μ μ΄λ―Έ ν€κ° μμΌλ©΄ κ°μ 1κ° μΆκ°
        counters[ws] += 1
    else:     # λμλλ¦¬μ ν€κ° μμΌλ©΄ κ°μ 1λ‘ λ°κΎΈκ³  ν€ λ±λ‘
        counters[ws] = 1

# κ²°κ³Ό νμ

for k,v in sorted(counter.items()):
    if v >= 3:
        print(k,v)

```
