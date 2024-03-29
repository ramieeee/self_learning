목차

{:toc}

# 1. UNIX Commands

## 1) 커맨드 종류

* clear: command 창 정리
* date: 시간 날짜 출력
* cal: 달력 출력



## 2) 이전 커맨드 확인

* 방향키 위, 아래 혹은 history 커맨드
* history 커맨드: !번호를 입력하면 이전 커맨드 다시 실행



## 3) sudo

* 관리자 권한이라는 뜻. 우분투에서 sudo apt update는 관리자 권한으로 업데이트 하라는 뜻. 예) crack-attack이라는 게임을 설치하려면 sudo apt install crack-attack, 삭제하려면 sudo apt remove crack-attack을 치면 됨



# 2. Command를 내 마음대로



## 1) 인자

* cal 6 2030: 2030년 달력 전부 출력 (2030을 인자라고 함. 영어로는 argument)



## 2) 옵션

* cal -y: 하이푼 뒤에 문자를 쓰는것을 옵션이라고 함. 커맨드의 구체적인 동작 방식 지정.
* 하이푼을 기준으로 인자와 옵션을 나눔.
* 옵션중 뒤에 어떤 값을 한 칸 띄우고 적는 것들이 있음(예: cal -B 2). B옵션은 before의 줄임말. "2" 처럼 이런 것을 옵션의 값이라고 하거나옵션의 인자라고 함.
* 옵션 중복 가능. 예) cal -B 2 -A 2
* 옵션 값이 없어도 되는 옵션이 있음. 예) -j를 cal -j로 사용 가능
* 하이푼 뒤에 여러 옵션 사용 가능. 예) cal -B 2 -jA 3



## 3) 공식 메뉴얼

* 궁금한 커맨드를 인자로 주면 됨. 예) man cal



# 3. directory



## 1) 현 디렉토리 확인

* 틸드(Tilde): 물결표시 "~"는 영어로 틸드이며 현재 사용자의 홈 디렉토리
* pwd: print the name of working directory. 예) /home/rambot
* 루트(최상위) 디렉토리에서 하위 디렉토리로 뻗어나감.
* 디렉토리는 부모(상위) 디렉토리, 자식(하위)디렉토리로 불림.



## 2) 디렉토리 변경

* cd커맨드 사용 (change directory) 예) cd /home/rambot/Pictures



### a. 절대경로

* 루트 디렉토리를 기준으로 어떤 팡리이나 디렉토리가 가지고 잇는 고유한 경로 예) /Users/jw/Pictures

### b. 상대경로

* 나의 현재 위치를 기준으로 나타낸 경로 예) ./Pictures
* 점 "."은 현재위지, 점점 ".."은 상위 디렉토리를 의미

### c. cd 커맨드 고급 사용법

* root 디렉토리로 이동: cd /
* home 디렉토리로 이동: cd ~
* 바로 이전 디렉토리로 이동: cd -



## 3)  디렉토리 내부 확인

* ls커맨드로 확인 가능
* ls -l: long listing 커맨드로, 자세한 정보 옵션임
* ls -a: 숨겨진 파일돌 모두 표시
* ls -l .profile과 같이 인자를 주면 파일에 대한 내용을 알려줌
* ls -l -d Pictures와 같이 -d를 쓰면 폴더 자체의 정보를 출력



## 4) 디렉토리 & 파일 만들기

* mkdir 인자: "인자" 이름으로 디렉토리 만들어짐
* touch 인자: "인자" 이름으로 파일 만들어짐
* 공백이 있으면 디렉토리를 2개 만들게됨.(인자를 2개로 인식)
* 공백이 있는 디렉토리를 만드려면 mkdir 'hello world'로 해야함



## 5) 디렉토리 파일 옮기기 & 이름 변경

* mv 커맨드: 옮기는 명령. 예) mv test 
* test 파일 이름 변경: 예) mv test sample (test 파일 이름을 sample로 변경함. 디렉토리 또한 동일하게 이름 변경 가능)



## 6) 디렉토리 파일 복사-붙여넣기

* cp(copy and paste) 커맨드: 예) cp first second(first를 second라는 이름으로 복사)
* -i 옵션: 파일을 붙여넣기 할때 덮어쓰기가 기본으로 됨. 그것을 방지하는것이 -i 옵션. 예) cp -i ~/.viminfo second
* -r 옵션: 디렉토리를 옮길때 사용. 



## 7) 디렉토리와 파일 삭제

* rm 커맨드: 예) rm first
* -r 옵션: 디렉토리 삭제를 할때 사용 예) rm -r directory



# 4. 파일 내용 출력



## 1) 내용 출력

* cat 커맨드: concatenate(이어붙이다) 예) cat sample
* cat 커맨드를 2개 붙여서 사용 가능 예) cat sample1 sample2
* 내용이 길면 less 커맨드 사용 가능 예) less sample1 (처음으로 이동: g, 마지막으로 이동: G, 다음 파일로 이동: :n, 이전 파일로 이동: :p)
* less 커맨드는 인자 두개를 주면 파일을 하나씩 출력 



## 2) 파일 내용 간단히 출력

### a. head 커맨드

* head 인자를 하면 기본적으로 처음 10줄 출력. 줄 수를 늘리고 싶다면 head -n 20 file처럼 사용.

### b. tail 커맨드

* 예) tail -20 file



# 5. Tap 이름 자동 완성

* cd 커맨드 뒤에 디렉토리&파일 첫 letter를 쓰고 탭을 누르면 자동완성.
* Document와 Download 두 디렉토리가 잇을때 cd D + 탭 2번을 누르면 보기가 주어짐



# 6. 텍스트 에디터, vim

* CLI 환경에서 사용하는 텍스트 에디터
* 모드가 여러개 있으며 다른 모드로 가려면 항상 일반 모드를 거쳐서 가야함
* vim을 치면 실행됨



## 1) 일반 모드

* 커서 이동 (h, j, k, l로 이동 가능). 멀리 이동하고싶을 시 이동하고싶은 칸 수를 입력하고 이동 예)5 + k
* 0: 커서가 있는 줄 맨 앞으로 이동
* $: 커서가 있는 줄 맨 뒤로 이동
* gg: 파일의 맨 처음으로 이동
* G: 파일의 맨 마지막으로 이동
* p: 텍스트 붙여넣기
* x: char 삭제
* dd: 문장 삭제
* u: 작업 취소
* ctrl + r: 작업 앞으로 돌리기

| 이동 위치                | 단축키      |
| ------------------------ | ----------- |
| 일반 모드 -> 입력모드    | a i o A I O |
| 일반 모드 -> 비주얼 모드 | v V         |
| 일반 모드 -> 명령 모드   | : /         |
| 다른 모드 -> 일반 모드   | esc         |



## 2) 입력 모드

* 텍스트 입력만 가능
* 대문자 i를 누르면 첫 줄로 이동하면서 입력모드로 바뀜
* 대문자 a를 누르면 마지막줄로 이동하면서 입력모드로 바뀜
* o를 누르면 줄을 하나 생성함

## 3) 비주얼 모드

* 텍스트 블록 지정: 방향키
* 줄단위 블록 지정: 대문자 V로 비주얼 모드 진입
* 삭제: 블록 지정 후 x
* 텍스트 복사(y, yank): 블록 지정 후 y.
* 붙여넣기 p or P: 소문자 p는 커서 다음칸, 대문자 P는 커서 이전 칸에 붙여넣기
* 잘라내기는 d 혹은 x로 지운 후 붙여넣기(p)를 하면 됨

## 4) 명령 모드

* 특정 텍스트 검색(슬래시 "/" 로 검색): 예) /like (like를 검색함) 다음으로 이동은 n, 이전은 N을 누르면 됨
* 저장은 w(write)
* J: 현재행과 아래행 결합
* 끄기 위해서 q를 눌러야함
* 저장 후 종료는 :wq
* 저장하지 않고 종료는 :q!
* :1,2 co 3       1-2행을 3행 다음으로 복사
* :1,2 m 10      1-2행을 10행 뒤로 이동
* 텍스트 치환(s, substitute) 예) :s/like/love -> like를 love로 바꿈(모든줄의 )
* 모든줄의 텍스트 치환(%): 각 줄의 첫번째 모든 단어를 치환. g(global) 옵션을 주면 모든 단어를 바꾸게 됨. 예) :%s/like/love/g
* 원하는 것만 바꾸고 싶을땐 c(confirm) 옵션 사용. :%s/like/love/gc.
* :noh     검색 하이라이트 지우기
