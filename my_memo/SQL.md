[toc]

# 1. 데이터베이스

* table: 표 형식으로 저장된 데이터 집합
* row: 개체 하나를 나타내는 단위(가로 줄 혹은 행). 혹은 레코드라고도 함
* column: 열. 각 개체가 가지는 하나의 속성.

# 2. DBMS

* DataBase Management System. 데이터베이스 관리 프로그램
* DBMS를 통해서 DB를 관리할 수 있음(테이블을 관리, 조회, 삭제, 추가할 수 있음)
* DBMS의 종류가 MySQL, MariaDB, Oracle 등이 있음
* 데이터베이스 구축은 DBMS를 선택하는것에서부터 시작됨.
* SQL: Structured Query Language

# 3. DBMS 구성요소

* client(클라이언트 프로그램): 사용자가 server에 접속해서 원하는 DB 관련 작업을 할 수 있도록 SQL을 입력할 수 있는 화면 등을 제공하는 프로그램
* server(서버 프로그램): client로부터 SQL문 등을 전달받아 데이터베이스 관련 작업을 직접 처리하는 프로그램
* 결국 DBMS를 사용한다는 것은 실행되고 있는 서버에 클라이언트를 이용하여 접속 후 원하는 명령을 내린다는 뜻

# 4. MySQL 데이터베이스 만들기

* 데이터베이스를 schema 라고도 부름

```mysql
CREATE DATABASE ramie_main
```

## 1) Primary Key

* 기본키 라고 함.
* id 라는 column이 맨 앞에 생기는데, 테이블에서 하나의 raw를 고유하게 식별할 수 있도록 해주는 컬럼.
* 가장 처음에 DB를 만들 때 설정해주는것

### a. Natural Key

* 어떤 개체가 갖고있는 속성을 나타내는 컬럼이 기본키가 됐을 때 이를 Natural Key라고 함.

### b. Surrogate Key

* 어떤 속성을 직접적으로 나타내는 컬럼은 아니지만 primary key로 쓰기 위해 추가한 컬럼
* 보통 1부터 시작해서 1씩 증가하는 정수값을 가짐

## 2) NN (not null)

* 특정 컬럼에서 값이 존재하지 않는 상태를 나타내는 키워드
* 해당 컬럼에 null이 있으면 안된다는 뜻(예: 게시판의 번호)
* primary key는 반드시 nn이 되어야함.

## 3) Auto Increment

* row가 새로 추가될때마다 자동으로 primary key 값이 1씩 증가하게하는 기능. 명령어를 통해 2, 3 등 증가값 변경 가능

# 5. 명령어

* 문장의 끝은 항상 세미콜론
* 예약어(내장된 키워드) 들은 대문자로 쓰는것이 관례. 예) SELECT, WHERE 등
* 선택

```mysql
SELECT * FROM ramie_main.member WHERE age NOT BETWEEN 30 AND 39;
# ramie_main DB의 member 테이블 전체 중 나이가 30-39세가 아닌 영역 선택

SELECT email, age, address FROM ramie_main.member;
# 특정 컬럼만 조회 가능

SELECT * FROM ramie_main.member WHERE email = 'taehos@hanmail.net';
# 원하는 row만 선택
```

* 선언(USE)

```mysql
USE ramie_main;  # 처음부터 이 DB를 쓰겠다고 선언
SELECT * FROM member;  # DB 선언 후 테이블명만 명령어 입력 가능
```

* LIKE

```mysql
SELECT * FROM ramie_main.member WHERE address LIKE '서울%';
# address 컬럼에서 '서울'로 시작하고 뒤에 임의의 문자가 들어간 것 조회
```

* 같지 않음

```mysql
# 같이 않음은 <>와 != 모두로 표현할 수 있음.
SELECT * FROM ramie_main.member WHERE gender <> 'f'; # 성이 f가 아닌 row 조회
SELECT * FROM ramie_main.member WHERE gender != 'f'; # 성이 f가 아닌 row 조회
```

* IN

```mysql
SELECT * FROM ramie_main.member WHERE age IN (20, 30); # 나이 20과 30만 조회
```

* 한 글자를 의미하는 _

```mysql
SELECT * FROM ramie_mail.member WHERE email LIKE 'c__@%'; # 이메일 cxx@* 조회
```

# 6. SQL 함수

* 연도, 월, 일 추출

```mysql
SELECT * FROM ramie_main.member WHERE YEAR(birthday) = '1992';
SELECT * FROM ramie_main.member WHERE MONTH(sign_up_day) IN (1, 5, 8); # 가입월 조회

# 각 달의 15-31일에 가입했던 회원들 조회
SELECT * FROM ramie_main.member WHERE DAYOFMONTH(sign_up_day) BETWEEN 15 AND 31
```

* 날짜 간의 차 구하기: DATEDIFF(''날짜 a', '날짜 b') 는 날짜 a, -날짜 b 를 리턴해줌

```mysql
SELECT id, sign_up_day, CURDATE(), DATEDIFF(sign_up_day, CURDATE()) FROM ramie_main.member;
# id, sign_up_day, 오늘날짜, DATEDIFF 컬럽 4개가 리턴

SELECT id, sign_up_day, DATEDIFF(sign_up_day, '2019-01-01') FROM ramie_main.member;
# id, sign_up_day, DATEDIFF 컬럼 3개가 리턴됨
```

* 날짜 더하기 빼기 DATE_ADD(), DATE_SUB()

```mysql
SELECT id, DATE_ADD(sign_up_day, INTERVAL 300 DAY) FROM ramie_main.member;
# 가입날짜 300일 이후를 계산 후 리턴

SELECT id, DATE_SUB(sign_up_day, INTERVAL 250 DAY) FROM ramie_main.member;
# 가입날짜 250일 이전 날짜를 리턴
```

* UNIX Timestamp 값: 시간을 별도로 나타냄(예: 2018-12-31 23:54:12)

```mysql
SELECT sign_up_day, UNIX_TIMESTAMP(sign_up_day) FROM ramie_main.member;
# UNIX_TIMESTAMP 함수만 쓰면 초단위로 계산한 값이 리턴됨. 그래서 아래와 같이 써야함

SELECT sign_up_day, FROM_UNIXTIME(UNIX_TIMESTAMP(sign_up_day)) FROM ramie_main.member;
```

# 7. 여러 조건

```mysql
SELECT * FROM ramie_main.member
WHERE gender = 'm'
	AND address LIKE '서울%'
	AND age BETWEEN 25 and 29;
# 성별 남, 서울 살고 나이는 25-29세 필터링한 값을 조회
```

* OR 조건: 조건 중 하나라도 만족하는 값이 있으면 리턴

```mysql
SELECT * FROM ramie_main.member
WHERE MONTH(sign_up_day) BETWEEN 3 AND 5  # 조건 1
	OR MONTH(sign_up_day) BETWEEN 9 AND 11;  # 조건 2

# AND, OR 조건 섞어 사용하기(괄호를 사용하는것이 좋음)
SELECT * FROM ramie_main.member
WHERE (gender = 'm' AND height >= 180)
	OR (gender = 'f' AND height >= 170);
```

* MySQL에선 0 외의 값은 모두 TRUE이기 때문에 주의해야함
* AND가 OR보다 연산 순위가 높음. 괄호로 우선 순위를 정하는게 좋음
* 특수문자는 escaping(\)을 사용
* 대소문자 구분

```mysql
SELECT * FROM ramie_main.member WHERE email LIKE BINARY '%M%';
# Binary(0과 1처럼)를 넣어 대문자 M을 구분하여 조회
```

# 8. 정렬

* 정렬을 할때 NULL이 가장 처음에 정렬됨
* 오름/내림차순 정렬

```mysql
SELECT * FROM ramie_main.member
ORDER BY height ASC; # 키별로 오름차순 정렬(ascending)

SELECT * FROM ramie_main.member
ORDER BY height DESC; # 키별로 내림차순 정렬(descending)
```

```mysql
SELECT * FROM ramie_main.member
WHERE gender = 'm'
	AND weight >= 70
ORDER BY height ASC;  # 조건 where는 order by 이전에 나옴
```

* 다중 정렬

```mysql
SELECT sign_up_day, email FROM ramie_main.member
ORDER BY YEAR(sign_up_day) DESC, email ASC;
# 가입날짜가 먼저 내림차순, 후에 이메일 오름차순 정렬
```

## 1) CAST 함수

* text는 int와 다르게 문자 하나 하나를 비교하기 때문에 유의해야함. (숫자로 된 문자열이라면 20, 112 두개 중 112가 우선 정렬됨)
* 이런 문제를 해결하기 위해 CAST를 써서 type을 바꿀 수 있음

```mysql
SELECT * FROM ramie_main.member ORDER BY CAST(data_col AS signed) ASC;
# data_col 이라는 컬럼이 INT일때와 같은 결과가 나옴
```

* 숫자에 소수점이 포함되어 있다면 signed 대신 decimal을 적고 사용

```mysql
SELECT * FROM ramie_main.member ORDER BY CAST(data_col AS decimal) ASC;
```

# 9. 데이터 일부 추리기(LIMIT)

```mysql
SELECT * FROM ramie_main.member ORDER BY sign_up_day DESC
LIMIT 10;
# 가입날 처음부터 10번째 row까지 조회

SELECT * FROM ramie_main.member ORDER BY sign_up_day DESC
LIMIT 3, 2;
# 가입날 기준 4번째 row 부터 2줄 조회(0부터 시작하기 때문에 3번째가 아니라 4번째임)
```

* 페이지네이션(pagination): 각 페이지마다 1 - 10, 11 - 20 같은 페이지를 보여주는 것. 데이터 추리기로 표현한다고 생각하면 됨
* MySQL 문법상 가장 맨 뒤에 써야함

# 10. 데이터 특성 구하기

* 개수 구하기 COUNT ()

```mysql
SELECT COUNT(email) FROM ramie_main.member;
# email 컬럼에서 NULL을 제외한 값이 있는 row의 개수를 조회함

SELECT COUNT(*) FROM ramie_main.member;
# asterisk가 있으면 모든 row 수를 출력해줌
```

* 가장 큰/작은 값 구하기 MAX(), MIN()

```mysql
SELECT MAX(height), MIN(weight) FROM ramie_main.member;
# 키가 가장 큰사람, 몸무게가 가장 적은 사람 조회
```

* 평균 값 AVG()

```mysql
SELECT AVG(height) FROM ramie_main.member;
# NULL이 있는 row는 제외하고 평균값을 구함
```

* 합계 SUM()

```mysql
SELECT SUM(age) FROM ramie_main.member;
```

* 표준편차 STD()

```mysql
SELECT STD(age) FROM ramie_main.member;
```

* 절대값 ABS()
* 제곱근 SQRT()
* 올림 CEIL()

```mysql
SELECT CEIL(height) FROM ramie_main.member;
```

* 내림 FLOOR()
* 반올림 ROUND()

# 11. NULL 다루기

* NULL이 있는 목록 조회

```mysql
SELECT * FROM ramie_main.member WHERE address IS NULL;
# 혹은 IS NOT NULL로 NULL 제외 조회 가능
```

```mysql
SELECT * FROM ramie_main.member
WHERE address IS NULL
	OR height IS NULL
	OR weight IS NULL;
# NULL이 있는 컬럼들 모두 조회 가능
```

* NULL을 다른 형식으로 조회 COALESCE()

```mysql
SELECT
	COALESCE(address, '---')  # address 컬럼의 NULL은 ---로 출력
	COALESCE(weight, '###')
	COALESCE(height, '***')
FROM ramie_main.member;
```

* NULL은 비교 대상이 아님. WHERE height = NULL 이 아니라 WHERE height IS NULL 이어야함

# 12. 이상한 값 제외시키기

* 예를들어 입력되는 나이값이 -10, 200 이런식이라면 아래처럼 예외처리를 해줘야함

```mysql
SELECT AVG(age) FROM ramie_main.member WHERE age BETWEEN 5 AND 100;
```

# 13. 컬럼끼리 계산

```mysql
SELECT height, weight, weight / ((height/100) * (height/100)) FROM ramie_main.member;
# 이런식으로 컬럼을 바로 계산할 수 있음. 
```

* 하나라도 NULL 이 있으면 계산 값도 NULL임

# 14. 컬럼에 alias(별칭) 붙이기

* AS를 붙이면 됨

```mysql
SELECT
	height AS 키,
	weight AS 몸무게,
	ROUND(weight / ((height/100) * (height/100))) AS BMI
FROM ramie_main.member;
```

* 붙이기 CONCAT()

```mysql
SELECT
	email,
	CONCAT(height, 'cm', ', ', weight, 'kg') AS '키, 몸무게', # 컬럼 2개 row를 하나로 붙임
	ROUND(weight / ((height/100) * (height/100))) AS BMI
FROM ramie_main.member;
```

# 15. 컬럼 값 변환



