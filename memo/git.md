목차

{:toc}

# 1. git

* 버전 관리 프로그램
* 지난 과정 확인 가능
* 이전 버전으로 돌아갈 수 있음



## 1) repository(레포지토리)

* 저장소 개념(커밋이 저장되는 곳)
* 프로젝트 디렉토리(폴더)를 버전별로 저장해놓음



## 2) commit(커밋)

* 프로젝트 디렉토리의 특정 모습을 하나의 버전으로 남기는 행위와 결과물



## 3) GUI 환경 git

* sourcetree

# 2. git 사용하기

* git 커맨드에 대한 자세한 정보를 알려면 git help 인자 커맨드 입력. 예) git help add -> add에 대한 커맨드 매뉴얼 출력



## 1) 레포지토리 만들기

* 프로젝트 디렉토리에서 <b>git init</b> 실행 (비어있는 레포지토리 생성됨)



## 2) 커밋 하기

### a. 커밋 사용자 등록

* 첫 커밋을 하기 전에 꼭 git에게 누가 커밋했는지 알려줄 것
* <b>git config user.name "이름" 예) git config user.name "ramie"</b>
* <b>git config user.email "이메일" 예) git config user.email "rambotty@gmail.com"</b>
* add: 수정된 파일의 모습을 커밋에 포함도리 것이라고 지정하는것 예) git add calculator.py
* git status: staging area에 어떤 파일이 commit될 준비가 되었는지 확인 가능
* 디렉토리를 git add 해주면 디렉토리 내에 있는 모든 파일들도 자동으로 add됨
* git add .: 점(.)은 현 디렉토리 모두를 선택하여 add함

### b. 커밋 메세지

* <b>commit -m: m 옵션으로 git commit과 함께 커밋 메세지를 남김 예) git commit -m "message"</b>

* -m옵션 없이 커밋 메세지를 남길 수 있음: 긴 메세지 작성 가능

* 커밋 메세지의 제목과 상세 설명 사이에는 한 줄을 비울 것

* 커밋 메세지의 제목 뒤에 온점(.)을 붙이지 말 것

* 커밋 제목 첫 알파벳은 대문자로 할 것

* 커밋 메세지의 제목은 명령조로 작성(Fix it / ~~Fixed it~~ / ~~Fixes it~~)

  

### c. 커밋 흐름

* working directory -> (git add files) -> staging area(or index) -> (git commit -m "message") -> repository

### d. 커밋 가이드라인

* 커밋 하나에는 하나의 이슈를 해결한 내용만 적용할 것
* 에러가 발생하지 않는 상태에서 커밋할 것



## 3)  git reset

### a. staging area 파일 제거

* staging area에서 파일을 제거하기 위해서 입력하는 커맨드 예) git reset filename

### b. HEAD 변경

* HEAD: 어떤 커밋 하나를 가리킴(주로 가장 최근에 한 커밋). Head가 가리키는 커밋에 따라 워킹 디렉토리가 바뀔 수 있음
* git reset은 과거 커밋으로 아예 돌아가고 싶을때 입력. 예) <b>git reset --soft</b> 커밋아이디4자리 -> 해당 커밋으로 현재 워킹 디렉토리 또한 모두 바뀜

| git reset [옵션] eea5 | working directory  |    staging area    |       repository        |
| :-------------------: | :----------------: | :----------------: | :---------------------: |
|        --soft         |      안 바뀜       |      안 바뀜       | HEAD가 eeat 커밋 가리킴 |
|        --mixed        |      안 바뀜       | eea5 커밋처럼 바뀜 | HEAD가 eeat 커밋 가리킴 |
|        --hard         | eea5 커밋처럼 바뀜 | eea5 커밋처럼 바뀜 | HEAD가 eeat 커밋 가리킴 |

### c. git reset 커밋 아이디 대체 커맨드

* git -reset --mixed HEAD^: HEAD가 가리키는 커밋 바로 이전 커밋으로 mixed reset
* 햣 git reset --soft HEAD~2: 현 HEAD의 2단계 이전 커밋으로 soft reset



## 4) aliasing

* git config alias.원하는커맨드 '실제 커맨드'



## 4) 커밋 히스토리

* git log 커맨드: 가장 아래 커밋이 가장 오래된 커밋.
* 커밋 아이디: 커밋 해시라고도 불림예)3867832a404f8eaaca0345c210d4f1d3a7b9d2bd
* git log --pretty: 커밋 히스토리를 깔끔하게 정리함
* git show 커밋아이디: 커밋아이디는 앞 4자리만 쳐도 문제없음. 예) git show 3867

### a. 히스토리 다양하게 보는 방법

* 현재 브랜치와 다른 브랜치도 보려면 --all 옵션 추가, --graph옵션 또한 추가하면 입체적으로 나타냄

예) git log --pretty=oneline --all --graph



## 5) 최신 커밋 수정

* git commit --amend 커맨드로 가장 최신 커밋 1개를 수정된 커밋으로 덮어씌울 수 있음

예) git add -> git commit --amend 후 저장 종료



## 6) 커밋 차이 보기

* git diff 이전커밋아이디 이후커밋아이디



## 7) 커밋에 tag 달기

* 태그 달기: git tag [태그이름] [커밋 아이디]
* git tag: 태그 목록을 보여주는 커맨드
* git show [태그이름]: 해당 태그 커밋을 보여줌



## 8) git reflog

* git reflog는 reference log로, HEAD 가 가리켰던 커밋들을 모두 출력해줌



## 9) git rebase

* 커밋을 재배치하다 라는 의미
* premium 브랜치와 test 브랜치 2개 중 git rebase test를 하면 브랜치가 더 깔끔하게 정리 됨

예) git rebase test (test 브랜치로 베이스를 옮기라는 뜻) 커맨드 후에 conflict 해결 후 git rebase --continue



## 10) git stash

### a. 임시저장용

* working directory에서 작업하던 내용을 깃이 따로 보관 (작업 중 다른 브랜치로 이동할때)
* git stash list 커맨드로 임시저장 내용 확인 가능
* 최근 커밋 이후로 작업했던 내용은 모두 스택에 옮겨지고 working directory 내부는 다시 최근 커밋의 상태로 초기화
* git stash apply: 스택에 옮겨진 가작 최근의 작업 내용을 다시 불러옴

### b. 잘못된 브랜치에서 작업하고 있을때

* 우선 git stash로 스택에 작업내용 저장 후 올바른 브랜치로 가서 git stash apply [stash 아이디]로 불러오기 실행

### c. stash 지우기

* git stash drop [stash 아이디]
* 주로 복구 후 바로 스태시 내용 삭제함.

### d. git stash pop

* git stash apply 후 git stash drop을 동시에 진행



## 11) git cherry-pick

* 자신이 원하는 작업이 들어있는 커밋들만 가져와서 현재 브랜치에 추가
* git cherry-pick [커밋아이디] -> conflict 해결 -> 커밋 진행

# 3. git hub

* 깃허브 레포지토리: 원격 레포지토리 혹은 리모트 레포지토리라고 함(내 컴퓨터 레포지토리는 로컬 레포지토리라고 함)
* git remote add origin https://github.com/ramieeee/[레포지토리이름].git
* git push -u origin master: 로컬 -> 리모트로 올릴때 처음 입력 커맨드



## 1) git push

* 로컬 레포지토리 -> 리모트 레포지토리에 보내려면 git push 커맨드를 통해 깃허브 업데이트를 해줘야함



## 2) git pull

* 리모트 레포지토리 -> 로컬 레포지토리로 가져오려면 git pull 커맨드로 업데이트 해야함
* git pull은 git fetch 후 자동으로 merge해주는 기능임



## 3) git clone

* 깃허브 프로젝트의 레포지토리를 그대로 복제
* git clone 주소. 예) git clone https://github.com/numpy/numpy.git



# 4. 브랜치

* 하나의 코드 관리 흐름
* git branch 커맨드를 통해 모든 브랜치 리스트 확인 가능



## 1) 마스터 브랜치

* 레포지토리를 만들고 커밋을 하면 자동으로 생기는 기본 브랜치 (git status를 통해 확인 가능)



## 2) 브랜치 나누기(만들기) & 삭제

* git branch [브랜치 이름]: 브랜치 만들기
* git checkout [가고싶은 브랜치 이름]: 브랜치 이동
* git checkout -b [브랜치 이름]: 브랜치 만듦과 동시에 이동
* git branch -d [브랜치이름]: 브랜치 삭제



## 3) 브랜치 merge 하기

### a. merge

* 다른 브랜치에서 했던 작업을 그대로 가져오는 것
* git merge [다른브랜치 이름]: 현재 있는 브랜치에 다른 브랜치를 합치겠다는 뜻. 예) git checkout premium으로 이동 후 git merge master 커맨드 입력

### b. merge conflict

* 두개의 비슷한 코드가 있을 때 git에서 어떤 것을 반영할지 사용자에게 물어보는 과정. (머지를 하다가 충돌하는 과정)
* 해결방안: conflict가 발생한 파일 검토 및 수정 후 git add, git commit 실행.
* 여러 파일들이 한번에 merge conflict를 발생시킬땐 하나 해결 후 git add [파일이름]을 통해 차근차근 staging area로 등록 후 커밋하면 됨.



### c. merge 취소하기

* git merge --abort: merge 취소. merge를 시도하기 이전 상태로 돌아옴



# 5. git 협업하기



## 1) git push 전 git pull하는 경우

* merge가 필요한 경우가 많음



## 2) git fetch

* 리모트에서 가져온 브랜치의 내용을 머지하기 전에 점검할 때 사용
* 리모트에 있는 브랜치 내용과 나의 고드를 비교하여 검토 시 사용
* git fetch 커맨드 후에 git diff [로컬브랜치] [리모트브랜치]로 비교.  예) git diff premium origin/premium



## 3) git blame

* 어떤 파일의 특정 코드를 누가 작성했는지 찾아내기 위한 커맨드
* git blame [파일 이름]



## 4) git revert 커밋

* 최신 커밋을 되돌리고 다시 커밋함
* git revert [커밋아이디]를 하고 커밋 메세지 작성 후 git push하면 바로 이전 단계로 커밋이 리모트로 푸쉬됨
* git reset을 하게되면 리모트보다 이전 단계의 커밋을 가지고 있으므로 푸쉬할 시 오류가 발생함. 그래서 revert 커밋으로 한단계 더 업데이트하여 커밋, 푸쉬를 하는것임
* 여러개의 커밋으로 한번에 revert도 가능 예) git revert facd..eeat (여기서 facd 커밋은 포함되지 않음)