# setting
* install node.js
* `npm init react-app <폴더 이름>`
* `npm run start`
* add react developer tool on google chrome

# render
* 화면에 그린다는 뜻
* argument는 html 태그를 사용(JSX 문법)

* 첫번째 argument 값을 활용해서 html 요소를 만들고 2번째 argument 값에 요소를 넣어줌
```javascript
import ReactDOM from 'react-dom';

ReactDOM.render(
  <hi>hello react!</hi>,
  document.getElementById('root')
);
```

# JSX
* javascript와 html을 섞어 쓸 수 있는 문법
* class 속성을 작성하려면 `className`을 써야함
* html의 for 속성은 `htmlFor`로 써야함
* 하나로 감싸진 태그를 사용해야함. 원하지 않을 시 fragment를 사용
```javascript
import ReactDOM from 'react-dom';

ReactDOM.render(
  <p className="hey">hello react!</p>,
  document.getElementById('root')
);

ReactDOM.render(
  <form>
    <label htmlFor="name">이름</label>
    <input id="name" type="text" onBlur="" onFocus="" onMousedown=""/>
  </form>
  document.getElementById('root')
);
```

* 하나로 감싸진 태그를 사용해야함. 원하지 않을 시 fragment를 사용. `<></>` 혹은 `<Fragment></Fragment>` 사용 가능
```javascript
import { Fragment } from 'react';

ReactDOM.render(
  <Fragment>
    <p className="hey">hello react!</p>,
  </Fragment>
    document.getElementById('root')
);
```

# JSX에서 자바스크립트 사용
* JSX는 실행될 때 javascript로 실행됨
```javascript
import { Fragment } from 'react';
import ReactDOM from 'react-dom';

const animal = "cat";
const cry = ' meow';
const cats = animal + cry;
const imageUrl = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/1024px-Cat_poster_1.jpg';

function handleClick() {
  alert('mwaaaaa');
}

ReactDOM.render(
  <>
    <p> My {cats.toUpperCase()} </p>
    <img src={imageUrl} alt="cat photo" height="100" />
    <button onClick={handleClick}>확인</button>
  </>,
  document.getElementById('root')
);
```

# 컴포넌트
* JSX의 html 부분을 변수에 저장해서 실행 가능
* 객체를 해석해서 html로 렌더링 해줌
* element를 함수로 작성하면 함수명을 가진 태그 작성 가능
```javascript
import ReactDOM from 'react-dom';

// 기본형
const element = <h1>hello there!</h1>;

ReactDOM.render(element, document.getElementById('root'));

// 함수명을 가진 태그를 리액트 컴포넌트라고 부름.
// JSX로 만든 react element를 return해줘야함
// 첫 글자는 대문자로 시작해야함
function Hello() {
    return <h1>hello there!</h1>;
}

const element = (
    <>
        <Hello />
        <Hello />
        <Hello />
    </>
);
ReactDOM.render(element, document.getElementById('root'));
```