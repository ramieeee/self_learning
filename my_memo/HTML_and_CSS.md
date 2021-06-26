목차

[toc]

---

# 1. HTML

HTML 태그(HTML 요소): HTML은 항상 시작태그와 종료 태그가 함께 있음.

예: <html></html>, <b></b> 등



## 1). 태그별 내용

```html
<!DOCTYPE html> <!-- 웹 브라우저가 HTML 버전을 알려주는 역할 -->
<html>
    <head> <!-- head 태그에 타이틀, 스타일, 글꼴 등이 들어감 -->
        <meta charset="utf-8"> <!-- 한글이 깨지지 않게 해주는 태그 -->
        <title>My Website</title> <!-- 웹사이트 제목 -->  
        <link href="css/styles.css" rel="stylesheet"> <!-- CSS파일을 읽게해주는 경로 지정 -->  
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> <!-- 글꼴 지정 -->  
        
        <style> /* CSS가 HTML에 적용된 예. style태그 안에 CSS 코드가 쓰임. CSS 경로설정이 없을 경우 사용 */
            h1 {
                text-align: center;
            }
            
            a {
                text-decoration: none;
                color: black;
            }
        </style>
    </head>

    <body> <!-- body 태그에 내용이 들어감 -->
        <div class="contents"> <!-- 내용을 묶어주는 태그 -->
            <h1>우라!</h1> <!-- 가장 큰 머리말 -->
            <h2>우라!</h2> <!-- 두 번째로 큰 머리말 -->
            <p>HTML이다!</p> <!-- paragraph -->
            <a href="https://instagram.com">Instagram Site</a> <!-- a태그(링크 태그) -->
            <img src="../images/my_photo" height=300> <!-- 이미지 -->
        </div>
    </body>
</html>
```

- b 태그: 굵게
- strong 태그: 강하게. b태그와 성격이 비슷함.
- i 태그: 기울여서(italic)
- em 태그: 강조. 이탈릭과 비슷함
- span 태그: inline 속성. div와 다르게 p 문단 안에 글도 따로 CSS 스타일링 가능하게 함.
- ol, ul 태그와 list

```html
<ol> <!-- ordered list(1,2,3 혹은 a,b,c 등으로 순서가 정해짐) -->
    <li>number1</li>
	<li>number2</li>
</ol>

<ul> <!-- unordered list(순서 없이 점으로 표시) -->
	<li>number1</li>
	<li>number2</li>
</ul>
```

* list 스타일링

```css
ul {
    padding: 30px;
}

li {
    list-style: none; /* ul의 앞에 점을 없애줌 */
    list-style-type: square;
}
```

*a 태그: 새 창을 열어 링크로 가고싶을때 target="_blank" 활용

*<a> 태그 색은 부모 태그 설정에 상속되지 않음. 그래서 따로 설정해야함 (예: .div1 a { color: inherit; } )

*a 태그에서 href="경로 설정을 할 수 있음.html"

# 2. CSS

## 1) 기본 문법

```css
h1 { 				   /* 스타일링 하고싶은 요소 */
    font-size: 50px;    /* 속성과 속성값 */
    text-align: center;
}
```

*CSS는 HTML코드 내에서 작성도 가능함.



## 2) 속성

- 폰트 크기: 주로 px가 많이 쓰임. (font-size: 60px;)

- 텍스트 정렬: text-align: left, center, right;로 정렬 가능

- 텍스트 색: 글에 색을 입히고 싶을때 색을 표현하는 방식. (color: lime, hotpink; 등)

- 여백: margin속성으로. 픽셀(px)단위로 여백을 줌. (margin-bottom: 80px;, margin-left: 30px; 등)

- 폰트 강조: font-weight: bold;로 표현 가능

- 폰트 사이즈: px는 절대적인 값이지만 rem은 상대적인 값임. Rem은 html 폰트의 2배. Html태그의 font-size에만 영향을 받음
  	em은 자신의 font-size를 기준으로 2배임. Font-size를 정해주지 않으면 상위 요소에서 상속받은 값을 기준으로 함.
  	%가 쓰일 경우, 상위 요소의 폰트 사이즈에서 %로 계산함.

  ​	(예: 상위 요소가 20px이고 하위 요소에 font-size: 180%;를 한다면 20px x 1.8 = 36px가 됨)
  ​	%가 margin이나 padding 단위로 사용될 경우 상위 요소의 width를 기준으로 계산됨. (top이나 bottom도 모두 width를 기준으로 계	산)



## 3) CSS 파일 따로 쓰기

* CSS 코드를 따로 작성/저장 및 관리하는게 더 편리.
* 헤드 부분에 <link href="CSS_파일_경로" rel="stylesheet"> 작성. rel은 relationship의 약자. Stylesheet은 rel의 타입



## 4) 폰트 종류

### a. Serif

* Times New Roman, 궁서체

### b. Sans-serif

* Arial, 굴림체

### c. Monospace

* Courier, Courier New

### d. Cursive

* Comic Sans MS, Monotype Corsiva

### e. Fantasy

* Impact, Haettenschweiler

```css
/* 폰트 적용 예: 처음 요소의 폰트가 없을 시 2차, 3차로 폰트를 찾아 적용 */
* {
    font-family: "Times new roman", Times, Serif;
}

/* 폰트를 다운받아 사용 시 */
@font-face {
    src: url("폰트_경로.otf");
    font-family: "폰트_이름_지정";
}

.div1 p {
    font-family: "지정된_폰트이름";
}
```



## 5) Display 속성

### a. inline display

* 다른 요소들과 같은 줄에 머무르려 하는 성향이 있음
* 가로 길이는 필요한 만큼만 차지하려는 성향
* inline display는 가로 세로 길이가 auto라고 생각하면 됨. 설정하지 못함. 그래서 inline-block을 하면 같은 줄에 머무르려는 inline 속성과 block의 가로세로 길이 설정이 가능해짐

### b. block display

* 새로운 줄에 가려고 하는 성향
* 가로 길이를 최대한 많이 차지하려고 하는 성향
* 예: <div>, <h1 - 6>, <p>, <nav>, <ul>, <li>

### c. display 종류

* 종류에는 inline, block, inline-block, flex, list-item, none 등이 있고 주로 inline과 block이 많이 사용됨.

### d. baseline

* 기본적으로 텍스트는 baseline에  맞추어 있음
* img 또한 baseline이  있음(img의 가장 밑 부분이 baseline임.)



## 6) 포지셔닝

모든 요소는 기본적으로 position: static;으로 되어 있음 (static position: 본래  있어야 할 위치에 있는 포지션)



### a. relative position

* relative는 상대적인 것을  의미함. 예를들어 <b> 혹은  <span>요소에 position: relative; 하고 margin을 주면 혼자만 따로 움직임.

### b. fixed position

* 브라우저를 기준으로 포지션 해줌(스크롤을 해도 똑같은 자리에  고정되어있음)
* position: fixed;를 하게  되면 본래 있던 문장에서 제외되고 문장은 다시 다른 문장으로 채워짐
* 네비게이션 바 등에서 많이 쓰임

### c. absolute position

* 가장 가까운 포지셔닝이 된  조상(Ancestor) 요소가 기준이 됨.



## 7) float, clear

### a. float

* 사진 등이 글에 둘러 쌓인 레이아웃 혹은 그리드 배열을  위한 목적

### b. clear

* float가 없도록 하는 속성.

  예) grid 배열이 float 속성으로  인해 테두리 속성을 인식하지 못하고 글도 오른쪽으로 나열이 될 때,

  clearfix div를 grid  div 바로 아래에 작성 후 clear: left;를 하게 되면 보더 인식이 됨.(세로 길이가 설정이 됨)



## 8) 반응형 웹 (responsil web design)

브라우저의 사이즈에 맞춰서 레이아웃이 바뀌는 것

```css
/* width가 750px를 넘어간다면 h1의 폰트가 바뀌게 됨 */
h1 {
    font-size: 15px;
}

@media (min-width: 750px) {	/* media quarry라고 읽음 */
    h1 {
        font-size: 20px;
    }
}
```

* 반응형 그리드 사이즈

  Extra Small (<  576px): 모바일

  Small (≥ 576px): 모바일

  Medium (≥ 768px): 타블릿

  Large (≥ 992px): 데스크탑

  Extra Large (≥  1200px): 와이드 데스크탑

# 3. 기타

## 1) 이미지

- <img src="사진 원본 주소" width="300">로 사용. (width, height 퍼센티지로 조절 가능)
- 이미지는 기본적으로 inline 요소이기 때문에 가운데 정렬을 위해서 block 요소로 바꾸는 방법이 있음.

```css
/* 이미지 가운데 정렬 예 */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
```



## 2) 클래스, ID

- 예를들어 <p> 태그가 여러개일때 한 개만 style을 부여하고 싶다면 class로 지정해줌.

```html
<p class="클래스_이름">내용<p>
```



* id는 클래스와 성질이 같으나 단 하나만 쓰일 수 있음. 중복 불가능
* 클래스는 ".", id는 "#"으로 CSS에 지정하여 스타일링 가능

```css
/* 클래스 */
.div_container {
    width: 100%;
    height: 400px;
}

/* id */
#navbar {
    background-color: #eeeeee;
}
```



## 3) DIV 태그

* 묶어주고 싶은 태그, 요소들을 div 태그로 묶어줌



## 4) 마우스 오버

```css
h1 {
    color: orange;
}

/* 마우스를 올려 놓으면 색이 초록으로 변하게 적용 */
h1:hover {
    color: green;
}
```



# 4. 선택자 정리

## 1) 직속자식

```css
/* "div1" 클래스를 가지고 있는 요소의 직속 자식중 모든 i 태그 */
.div > i {
    color: white;
}
```



## 2) 복수선택

```css
.navbar, .footer {
    background-color: grey;
}
```



## 3) 가상클래스(n번 자식)

```css
/* .div1의 자식인 <p> 태그 중 3번째 */
.div1 p:nth-child(3) {
    color: blue;
}

/* .div1의 자식인 <p> 태그 중 첫번째 */
.div1 p:first-child {
    color: red;
}

/* .div1의 자식인 <p> 태그 중 마지막 */
.div1 p:last-child {
    color: blue;
}

/* .div1의 자식 중 마지막 자식이 아닌 <p> 태그 */
.div1 p:not(:last-child) {
    color: yellow;
}

/* .div1의 자식 중 첫 번째 자식이 아닌 <p> 태그 */
.div1 p:not(:first-child) {
    text-decoration: line-through;
}
```



# 5. Box model

안에서부터 내용->padding->border->margin 순으로 box가 이루어져있음



## 1) Padding

* padding 설정 방식은 top부터 시계방향으로 padding: 50px 30px 30px 10px; 이런식으로도 가능.
* 사방 값이 다 같으면 50px 이런식으로 한번만 써주면 됨
* 값을 두번 써주면 첫번째 값은 위-아래, 두번째 값은 오른쪽-왼쪽이 됨.



## 2) width, height

* min-width, max-width, min-height, max-height로 마진을 창의 사이즈와 상관없이 고정시킬 수 있음
* max-height 설정 시 overflow(글자 삐져나옴)가 발생할 수 있음



## 3) overflow

* overflow: hidden; , overflow: visible;로 오버플로우 조절 가능
* overflow: scroll;로 하면 오버플로우가 스크롤로 조절 가능.
* overflow: auto;도 scroll과 비슷한데 보통 오토를 많이 사용



## 4) border

* border 속성을 한줄에 다 쓰는 방법이 있음. 예:border: 2px solid #4d9fff;
* 실선(solid), 점선(dotted), 대시선(dashed) 등이 있음



## 5) 박스 꾸미기

* 모서리 둥글게: border-radius: 10px;
* 배경색: background-color: 색이름;   투명색: background-color: transparent;
* 그림자: box-shadow: 10px 15px 20px 30px grey;  (10px:가로 그림자, 15px:세로 그림자, 20px: 그림자 흐림 정도, 30px: 그림자 크기)



## 6) box-sizing

* box-sizing: border-box; 를 하게 되면, padding과 보더 사이즈를 계산하지 않아도, 내가 설정한 가로 세로 길이를 padding과 보더를 자동 계산함.
* 현재는 CSS 모든 요소에 box-sizing: border-box;를 붙여넣음



## 7) 배경 이미지

* background-image: url("이미지 경로"); 그리고 background-repeat: no-repeat; 
* background-size: cover; <-배경 이미지를 브라우저 및 박스 비율에 맞게 설정함
* background-position: center bottom; 이런식으로 하면 사이즈가 변할때 남길 부분을 설정함. (가로 center, 세로 bottom이 되게 됨)
* background-repeat

```css
/* 반복하지 않음 */
background-repeat: no-repeat;

/* 가로 방향으로만 반복 */
background-repeat: repeat-x;

/* 세로 방향으로만 반복 */
background-repeat: repeat-y;

/* 가로와 세로 모두 반복 */
background-repeat: repeat;

/* 반복할 수 있는 만큼 반복한 뒤, 남는 공간은 이미지 간의 여백으로 배분 */
background-repeat: space;

/* 반복할 수 있는 만큼 반복한 뒤, 남는 공간은 이미지 확대를 통해 배분 */
background-repeat: round;
```

* background-size

```css
/* 원래 이미지 사이즈대로 출력 */
background-size: auto;

/* 화면을 꽉 채우면서, 사진 비율을 유지 */
background-size: cover;

/* 가로, 세로 중 먼저 채워지는 쪽에 맞추어서 출력 */
background-size: contain;

/* 픽셀값 지정 (가로: 30px, 세로: 50px로 설정) */
background-size: 30px 50px;

/* 픽셀값 지정 (가로: 부모 요소 width의 60%, 세로: 부모 요소 height의 70%로 설정) */
background-size: 60%, 70%;
```



