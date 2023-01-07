# 파일처리 🔎

open(file, moode='r', encoding=none)

- mode

| mode의 값 | 설명                                                           |
| --------- | -------------------------------------------------------------- |
| w         | 파일의 쓰기 모드로 연다                                        |
| r         | 파일의 읽기 모드로 연다                                        |
| a         | 쓰기 모드로 열고 파일이 존재하면 가장 끝부분에서 쓰기 시작한다 |
| b         | 바이너리 모드                                                  |
| f         | 텍스트 모드(기본값)                                            |

```python

a_file = open('test.txt', mode='w', encoading='utf-8')

a_file.write('나는 실패해본 적이 없다. \n')
a_file.write('1만 가지의 방법을 찾아냈을 뿐이다. \n')
a_file.write('-토마스 에디슨\n')

a_file.close
```

- with 구문을 사용하여 더 편리하게

---

with open 파일명 as 변수명:

```python

with open('mt.txt',encoading='utf-8') as f:
    for line in tf:
        print(line)

#  텍스트 파일에서 키워드를 검색한다

key = 'find'
with open('mt.txt', encoading='utf-8') as f:

    for i, line in enumerate(tf): #파일 한줄씩 읽는다
        # enumerate()힘수를 사용하면 인덱스 번호와 요소의 값 얻을수 있다.
        if line.find(key) >= 0 : # find()메서드 활용 특정 문자열이 0 부터 세어서 몇번째에 존재하는지 알수 있다. 발견 못하면 -1 반환
            print(i+1 ":", line)
```

## Json

---

자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식

            import json
            x =[1, 'simple', 'list']
            json. dumps(x)

            x = json.load(f)

```python

import json

# 딕셔너리형 데이터
data = {
    'no' : 5,
    'code' :('jas', 1, 19)
    'scr' : 'be quick'
}

# 파일에 쓴다
filename = 'test.json'
with open(filename, 'w')as fp:
    json.dump(data, fp) # json형으로 저장

# 파일 읽기
with open(filename, 'r') as fp:
    r = json.load(fp) # json 형으로 저장된 파일을 읽는다
    print('no=', r['no'])
    print('code=', r['code'])
    print('scr=', r['scr'])

    # no = 5
    # code = ['jas', 1, 19]
    # scr = be quick
```
