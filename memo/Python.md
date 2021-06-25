목차

[toc]

---

# 1. Python 기초

## 1) 프로그래밍 용어

- 컴파일러: 고급언어를 머신코드로 전환

- 인터프리터: 실행을 시킴 

- GIT: 업데이트를 위한 프로그램	

- 플랫폼: 프로그램이 실행되는 하드/소프트웨어 환경

  예: 어플<-운영체제<-하드웨어(운영체제와 어플의 플렛폼)
  *플랫폼 의존성: 플랫폼마다 따로 만들어야함(iOS, Windows, 핸드폰, 랩탑 등.
  **크로스 플렛폼: 플렛폼 의존성을 낮추기 위해 만듦. 어댑터라고 생각하면 됨. 예) JVM(Java Virtual Machine

- 웹 어플리케이션: 어플처럼 웹에서 작동함. 예) 구글지도설치, 배포 필요없음. 하드웨어, OS, 브라우저가 플랫폼임
- Native 어플리케이션: 설치를 해야함. 설치 배포가 필요	
- Single page 어플리케이션: 클릭할때마다 페이지 변화 X. 예)페이스북, 지메일, 구글맵
- 하이브리드 어플리케이션: 예) 광고를 페이지 사이에 구멍을 내서 거기만 바꿈.
- Progressive web application: Singlepage application + hybrid web application



## 2) 파이썬 용어

- 변수(variable)	정보를 저장하고 쓸 수 있게 해주는 "이름표"

  예) 브랜드 = "나이키" 혹은 x = 500
  복잡한건 숨기고 주요 기능만 신경씀. 값 저장용.
  글로벌 변수와 로컬 변수가 있음

- 자료형: 숫자, 문자 등 여러가지 형태. 대표적으로 숫자, 문자, 참과 거짓을 나타내는 논리형.

  정수(integer), 소수(floating point)로 나뉨

- 문자열(string): "hello", "world", "2" 등 문자로 인식함

  예) print("1" + "1") 실행 시 11로 표기됨

- 함수(function): 변수가 값을 보관하는 역할이라면 함수는 명령을 보관하는 역할. 예) print("hello")에서 print





## 3) 함수

- print: 값을 출력하는 함수

- def(define): 함수를 만들어냄

- 파라미터(parameter): 함수에 넘겨주는 값.

- return: 값을 보여줌. 함수를 종료시킴.

- 형변환(type conversion): 값을 한 자료형에서 다른 자료형으로 바꿔줌.

  ​	예: int, str, float
  
- boolean(불 대수): True or False

  ![image-20210128195344006](Python(파이썬).assets/image-20210128195344006.png)

- type: 쓰는 값이 어떤 자료형인지 알려주는 함수

- syntactic sugar: 자주 쓰이는 표현을 더 간략하게 해줌.

  예: x += 1

- scope:

  로컬변수: 변수를 정의한 함수 내에서만 사용 가능

  글로벌 변수: 모든 곳에서 사용 가능

- 상수(constant): 절대 변하지 않는 변수(대문자로 표시)

  예: PI = 3.14

- range: 범위 설정

  ```python
  # 1개(stop)
  for i in range(10) # for i in range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  
  # 2개(start, stop)
  for i in range(3, 11) # for i in range(3, 4, 5, 6, 7, 8, 9, 10)
  
  # 3개(start, stop, step)
  for i in range(3, 16, 3) # for i in range(3, 6, 9, 12, 15)
  ```

- input(사용자 입력받기): input("이름을 입력하세요: ")

  *주의: input함수가 받는 값은 항상 문자열임.



## 4) while, if, for 

- while문: 조건을 달고 조건이 끝날때까지 반복함
- if문: 조건문 (elif와 else가 함께 쓰임)
- break문: while문에 if 조건을 달아 충족시킬 시 중단시킬 수 있음.
- continue문: if 조건을 달아 충족될 시 해당문을 건너뜀.
- for 반복문: while과 비슷한 반목문



## 5) list, dictionary

### a. 리스트(list)

변수에 값을 여러 개 저장하는법. 리스트를 구성하는 값들은 요소. 예) numbers = [2, 5, 6, 9, 10]   *2,5,6,9,10은 리스트의 요소.

- 인덱스(index): 인덱스는 요소의 위치임.

- 마이너스 인덱스(minus index): 요소들의 개수에 따라 다름. 요소가 6개면 인덱스의 범위는 -6 ~ 5까지 있음.

- 리스트 슬라이싱(list slicing): 통째로 리스트를 자름.

  *[0:4]이면 첫번째부터 세번째까지.

  *[2:] 이면 세번째부터 마지막  요소까지.

  *[:2] 이면 처음부터 첫번째  요소까지.

### b. 인덱스 함수

- len(값): 인덱스의 length를 보여줌.
- append(값): 리스트에 값을 추가함.
- delete(값): 리스트에서 값을 지움
- insert(삽입연산): 원하는 자리에 index 추가

```python
# 예시
example = [1, 2, 3, 4, 5]

print(len(example)) # 5
example.append(6) # example = [1, 2, 3, 4, 5, 6]
del example[0] # example = [2, 3, 4, 5]
example.insert(0, 10) # example = [10, 2, 3, 4, 5]
```



### c. 리스트 정렬 함수, 리스트 값 확인

```python
# 예시
example = [3, 2, 1, 4, 5]

sort = sorted(example) # sorted 함수
sort_reverse = sorted(example, reverse=True) # sorted reverse 함수
example.sort() # sort method
example.sort(reverse=True) # sort reverse method

print(2 in example) # 리스트 값 확인. 값은 True
print(2 not in example) # 리스트 값 확인. 값은 False

print(example.index(5)) # 인덱스 method. 값은 4(4번째 인덱스)
example.remove(5) # remove method. 인덱스 값 5를 없앰. example = [3, 2, 1, 4]
```



### d. 라이브러리

key-value가 하나의 pair가 됨.

*리스트와 달리 순서라는 개념이 없음

*사전의 key는 정수일 필요가 없음

- dictionary 활용

```python
# 예시
german_words = {
    "below": "unter"
    "now": "jetzt"
    "tired": "müde"
}

# 라이브러리에 for문 활용 예시
for key, value in german_words.items():
    print(key, value)
```



### e. 리스트 다루기

* 슬라이싱으로 문자열 뒤집어 출력하기

```python
s = "abcde"

print(s[::-1]) # 값: edcba
# s[시작:끝:점프]
# 시작이 끝보다 크면 점프를 -1로 역순 정렬하게 해야함.
# 끝을 비워 놓아야 마지막 값까지 출력이 됨
```



## 6) 파이썬 파일 읽기, 쓰기

### a. 파일 읽기

파일 읽기(txt 확장자)는 같은 폴더 위치에서만 읽을 수 있음.

파일을 읽게 되면 문장 끝에 \n이 끝에 기본적으로 들어가게됨.

다른 폴더에 있다면 경로를 지정해줘야함(예: with open("data/daily_turnover.txt", "r") as file:    <--여기서 r은 read의 약자로, 읽기형식임. 쓰는 개념은 "w"로 표기

만약 읽기 에러가 난다면(UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 1: illegal multibyte sequence), 이 코드로 다시 시도 필요 -> "r", encoding="UTF-8"

```python
# 예시
with open("my_german_note.txt", "r") as file:
    for line in file:
        print(line)
        
# 읽기 에러 시(UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 1: illegal multibyte sequence)
with open("my_german_note.txt", "r", encoding="UTF-8")

# strip: 문자열 앞뒤 화이트 스페이스 제거
with open("my_german_note.txt", "r") as file:
    for line in file:
        print(line.strip())

# split: 문자열을 파라미터를 기준으로 리스트로 출력
full_name: "yeon, ramhee"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name) # 값: ramhee Yeon
```



### b. 파일 쓰기

파일 읽기와 마찬가지로 open함수를 작성하고 "w"를 사용하여 쓰기.

"w" 대신 "a"를 쓰게 되면, apend라는 의미로 덧붙이기가 됨. 단순히 "w"만 쓰면 가장 최근에 쓴 값으로 덮어쓰기가 되나 "a"는 추가하는 개념.

```python
# 예시
with open("new_file.txt", "w") as file:
    file.write("Hello!\n")
    file.write("World!")
```
