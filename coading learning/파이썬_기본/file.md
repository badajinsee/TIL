# νμΌμ²λ¦¬ π

open(file, moode='r', encoding=none)

- mode

| modeμ κ° | μ€λͺ                                                           |
| --------- | -------------------------------------------------------------- |
| w         | νμΌμ μ°κΈ° λͺ¨λλ‘ μ°λ€                                        |
| r         | νμΌμ μ½κΈ° λͺ¨λλ‘ μ°λ€                                        |
| a         | μ°κΈ° λͺ¨λλ‘ μ΄κ³  νμΌμ΄ μ‘΄μ¬νλ©΄ κ°μ₯ λλΆλΆμμ μ°κΈ° μμνλ€ |
| b         | λ°μ΄λλ¦¬ λͺ¨λ                                                  |
| f         | νμ€νΈ λͺ¨λ(κΈ°λ³Έκ°)                                            |

```python

a_file = open('test.txt', mode='w', encoading='utf-8')

a_file.write('λλ μ€ν¨ν΄λ³Έ μ μ΄ μλ€. \n')
a_file.write('1λ§ κ°μ§μ λ°©λ²μ μ°Ύμλμ λΏμ΄λ€. \n')
a_file.write('-ν λ§μ€ μλμ¨\n')

a_file.close
```

- with κ΅¬λ¬Έμ μ¬μ©νμ¬ λ νΈλ¦¬νκ²

---

with open νμΌλͺ as λ³μλͺ:

```python

with open('mt.txt',encoading='utf-8') as f:
    for line in tf:
        print(line)

#  νμ€νΈ νμΌμμ ν€μλλ₯Ό κ²μνλ€

key = 'find'
with open('mt.txt', encoading='utf-8') as f:

    for i, line in enumerate(tf): #νμΌ νμ€μ© μ½λλ€
        # enumerate()νμλ₯Ό μ¬μ©νλ©΄ μΈλ±μ€ λ²νΈμ μμμ κ° μ»μμ μλ€.
        if line.find(key) >= 0 : # find()λ©μλ νμ© νΉμ  λ¬Έμμ΄μ΄ 0 λΆν° μΈμ΄μ λͺλ²μ§Έμ μ‘΄μ¬νλμ§ μμ μλ€. λ°κ²¬ λͺ»νλ©΄ -1 λ°ν
            print(i+1 ":", line)
```

## Json

---

μλ°μ€ν¬λ¦½νΈ κ°μ²΄ νκΈ°λ²μΌλ‘ κ°λ°νκ²½μμ λ§μ΄ νμ©λλ λ°μ΄ν° μμ

            import json
            x =[1, 'simple', 'list']
            json. dumps(x)

            x = json.load(f)

```python

import json

# λμλλ¦¬ν λ°μ΄ν°
data = {
    'no' : 5,
    'code' :('jas', 1, 19)
    'scr' : 'be quick'
}

# νμΌμ μ΄λ€
filename = 'test.json'
with open(filename, 'w')as fp:
    json.dump(data, fp) # jsonνμΌλ‘ μ μ₯

# νμΌ μ½κΈ°
with open(filename, 'r') as fp:
    r = json.load(fp) # json νμΌλ‘ μ μ₯λ νμΌμ μ½λλ€
    print('no=', r['no'])
    print('code=', r['code'])
    print('scr=', r['scr'])

    # no = 5
    # code = ['jas', 1, 19]
    # scr = be quick
```
