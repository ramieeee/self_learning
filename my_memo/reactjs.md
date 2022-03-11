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

# props
* properties
* 컴포넌트에 지정한 속성들
* html 뿐만 아니라 컴포넌트에 속성 추가 가능
```javascript
// 예시. props의 색에 따라 다른 주사위를 display
// Dice 컴포넌트
import diceBlue01 from './assets/dice-blue-1.svg';
import diceBlue02 from './assets/dice-blue-2.svg';
import diceBlue03 from './assets/dice-blue-3.svg';
import diceBlue04 from './assets/dice-blue-4.svg';
import diceBlue05 from './assets/dice-blue-5.svg';
import diceBlue06 from './assets/dice-blue-6.svg';
import diceRed01 from './assets/dice-red-1.svg';
import diceRed02 from './assets/dice-red-2.svg';
import diceRed03 from './assets/dice-red-3.svg';
import diceRed04 from './assets/dice-red-4.svg';
import diceRed05 from './assets/dice-red-5.svg';
import diceRed06 from './assets/dice-red-6.svg';

const DICE_IMAGES = {
    blue: [diceBlue01, diceBlue02, diceBlue03, diceBlue04, diceBlue05, diceBlue06],
    red: [diceRed01, diceRed02, diceRed03, diceRed04, diceRed05, diceRed06]
}

function Dice({ color = "blue", num = 1 }) {
    const src = DICE_IMAGES[color][num - 1];
    const alt = `${color} ${num}` ;
    return <img src={src} alt={alt} />;
}
export default Dice;

// App 컴포넌트
import Dice from "./Dice";

function App() {
    return (
    <div>
        <Dice color="blue" num={5} />
    </div>
    )
}
export default App;

// index.js
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

* 예시2
```javascript
// App.js
import HandButton from "./HandButton";

function App() {
  const handleClick = (value) => console.log(value);
  return (
    <div>
      <HandButton value="rock" onClick={handleClick} />
      <HandButton value="scissors" onClick={handleClick} />
      <HandButton value="paper" onClick={handleClick} />
    </div>
  );
}
export default App;

// Handlcon.js
import rockImg from './assets/rock.svg';
import scissorImg from './assets/scissor.svg';
import paperImg from './assets/paper.svg';

const IMG = {
    rock: rockImg,
    scissors: scissorImg,
    paper: paperImg
}

function HandIcon({value = "rock"}) {
    const src = IMG[value];
    return <img src={src} alt={src} />;
}

export default HandIcon;

// HandButton.js
import HandIcon from "./HandIcon";

function HandButton({ value, onClick }) {
    const handleClick = () => onClick(value);
    return (
    <button onClick={handleClick}>
        <HandIcon value={value} />
    </button>
    );
}

export default HandButton;
```

# children
* 기본으로 존재하는 prop
* 컴포넌트의 자식들을 값으로 받는 prop
* JSX 문법으로 컴포넌트를 작성할 때 컴포넌트를 여는 태그와 닫는 태그의 형태로 작성. 안에 있는 코드가 children 값에 담김
```javascript
// Button.js
function Button({ children }) {
    return <button>{children}</button>;
}
export default Button;

// App.js
import Button from "./Button";
import Dice from "./Dice";

function App() {
  const handleClick = (value) => console.log(value);
  return (
    <div>
      <div>
          <Button>던지기</Button>
          <Button>처음부터</Button>
      </div>
      <Dice color="red" num={2} />
    </div>
  );
}
export default App;
```

* 예제2
```javascript
// Button.js
function Button({ children, onClick }) {
    return <button onClick={onClick}>{children}</button>;
}

export default Button;

// App.js
import Button from './Button';
import HandButton from './HandButton';

function App() {
  const handleButtonClick = (value) => console.log(value);
  const handleClearClick = () => console.log('처음부터');
  return (
    <div>
      <Button onClick={handleClearClick}>처음부터</Button>
      <HandButton value="rock" onClick={handleButtonClick} />
      <HandButton value="scissor" onClick={handleButtonClick} />
      <HandButton value="paper" onClick={handleButtonClick} />
    </div>
  );
}
export default App;
```

# state
* react의 변수같은 개념
* state가 바뀌면 react에서 새로 업데이트 해주는 개념
* html처럼 각각의 페이지를 만들 필요 없이 화면을 바꿔줌
* 배열의 형태로 값 리턴하기 때문에 배열의 형태로 destructuring. 첫번째 요소는 state 값(현재 변수의 값). 두번째 요소는 set 함수이며 파라미터로 전달하는 값으로 state가 변경됨
`const [num, setNum] = useState(1);`
* 일반적으로 두번째 요소는 state 요소의 이름과 같으며 앞에 set를 붙여줌
```javascript
// Button.js
function Button({ children, onClick }) {
    return <button onClick={onClick}>{children}</button>;
  }
  
  export default Button;

// App.js
import { useState } from 'react';
import Button from './Button';
import Dice from './Dice';

function random(n) {
    return Math.ceil(Math.random() * n);
}

function App() {
  const [num, setNum] = useState(1);

  const handleRollClick = () => {
      const nextNum = random(6);
      setNum(nextNum);
  }

  const handleClearClick =() => {
      setNum(1);
  }
  return (
    <div>
      <div>
          <Button onClick={handleRollClick}>던지기</Button>
          <Button onClick={handleClearClick}>처음부터</Button>
      </div>
      <Dice color="red" num={num} />
    </div>
  );
}

export default App;
```

# 참조형 state
* 배열 값을 가진 useState를 사용할 때 push같은 매소드를 사용한다면 주소를 참조하기 때문에 값에 변화가 없을 수 있음. 그래서 Spread문법(...)을 활용함
```javascript
const [gameHistory, setGameHistory] = useState([]);

const handleRollClick = () => {
  const nextNum = random(6);
  setGameHistory([...gameHistory, nextNum]); 
};
// gameHistory가 [1], [1, 2] 식으로 하나씩 쌓이게 됨

```

# input 핸들링
* input 태그로 값을 입력 받을 시 type, value, onChange 등의 prop을 입력받을 수 있음
```javascript
// const [bet, setBet] = useState(1);

// 값을 입력받을 시 1-9 사이의 숫자 정수만 입력받을 수 있도록 설정
const handleBetChange = (e) => {
  let num = Number(e.target.value); // input의 value를 참조함
  if (num > 9) num %= 10;
  if (num < 1) num = 1;
  num = Math.floor(num);
  setBet(num);
}

<input type="number" value={bet} min={1} max={9} onChange={handleBetChange}></input>
```

# 컴포넌트
* 부품
* 반복적인 일이 줄어듦
* 유지보수가 쉬움
* 일을 쉽게 나눌 수 있음. 일을 나누고 조립만 하면 됨

# 리액트의 랜더링
* state가 바뀔 때 새로 랜더링 함.
* DOM을 바로 변경하는게 아니라 virtualDOM에서 변경사항들을 모아두었다가 일감을 적당히 나눠서 적용함.
* state값을 변경하고 전체를 랜더링함. 이런 전체 랜더링 하는 문제를 해결하기 위해 virtual DOM을 사용함. 우선 virtual DOM tree를 사용함. 바뀌기 전의 virtualDOM과 바뀐 후의 virtualDOM을 서로 비교하게함
* 단순하고 깔끔해지는 코드

# 인라인 스타일
* 컴포넌트에 디자인 적용 방법
* html의 스타일 속성처럼 style속성 지정 가능.
* 객체형태로 스타일을 지정해줘야함
```javascript
// 객체
const baseButtonStyle = {
  padding: '14px 27px',
  border: 'solid 1px #7090ff',
  outline: 'none',
  color: '#7090ff',
  cursor: 'pointer',
  backgroundColor: 'rgba(0, 89, 255, 0.2)',
  borderRadius: '30px',
  fontSize: '17px',
}

const blueButtonStyle = {
  ...baseButtonStyle,  // spread 문법으로 모두 중복되지만 바뀔 값만 따로 설정 가능
  backgroundColor: 'rgba(0, 89, 255, 0.2)',
  border: 'solid 1px #7090ff',
  color: '#7090ff',
}

function Button({ children, onClick, color }) {
  const style = color === 'red' ? redButtonStyle : blueButtonStyle;
  return (
    <button style={style} onClick={onClick}>
      {children}
    </button>
  );
}

export default Button;
```
```javascript
import HandIcon from './HandIcon';
import handBackground from './assets/purple.svg';

const style = {
  width: '166px',
  height: '166px',
  border: 'none',
  outline: 'none',
  textAlign: 'center',
  cursor: 'pointer',
  backgroundColor: 'transparent',
  backgroundImage: `url(${handBackground})`,
  backgroundRepeat: 'no-repeat',
  backgroundPosition: 'center',
  backgroundSize: 'contain',
}

// 인라인 스타일을 적용해주세요
function HandButton({ value, onClick }) {
  const handleClick = () => onClick(value);
  return (
    <button style={style} onClick={handleClick}>
      <HandIcon value={value} />
    </button>
  );
}

export default HandButton;
```

# 자바스크립트 파일에서 CSS 파일 import 기능
* Create React App 이라는 프로그램이 설정
```javascript
import './index.css';
```

# 빌드하기
* JSX를 순수한 자바스크립트로 변환해야함. 프론트엔드에선 빌드라고 함
* 터미널에서 `npm run build` 입력 -> build 디렉토리 확인 -> `npx serve build` 로 로컬 환경에서 빌드된 환경 테스트 실행