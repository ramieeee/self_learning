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
