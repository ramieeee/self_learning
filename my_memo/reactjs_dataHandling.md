# map으로 배열 렌더링
* 배열 랜더링에선 반드시 key를 설정해줘야함 (예: item의 id)
* 아래 예시는 FoodList에서 items 객체(json)를 받고, FoodListItem에서 객체를 쪼개서 리턴해줌
```javascript
// FoodList.js
function FoodListItem({ item }) {
  const { imgUrl, title, calorie, content } = item;

  return (
    <div>
      <img src={imgUrl} alt={title} />
      <div>{title}</div>
      <div>{calorie}</div>
      <div>{content}</div>
    </div>
  );
}

function FoodList({ items }) {
  return (
    <ul>
      {items.map((item) => ( // 여기서 key prop으로 id 구별
        <li key={item.id}>
          <FoodListItem item={item} />
        </li>
        ))}
    </ul>
  );
}

export default FoodList;

// App.js
import FoodList from './FoodList';
import items from '../mock.json';

function App() {
  return (
    <div>
      <FoodList items={items} />
    </div>
  );
}

export default App;
```

# sort로 정렬 바꾸기
* sort()함수에 다른 function을 인자로 줄 수 있음
```javascript
import { useState } from 'react;
import ReviewList from './ReviewList';
import items from '../mock.json';

function App() {
    const [order, setOrder] = useState('createdAt');
    const sortedItems = items.sort((a, b) => b[order] - a[order]); // 역순 정렬 함수

    const handleNewsClick = () => setOrder('createdAt');
    const handleBestClick = () => setOrder('rating');

    return (
        <div>
            <div>
                <button onClick={handleNewestClick}>최신순</button>
                <button onClick={handleBestClick}>베스트순</button>
            </div>
            <ReviewList items={sortedItems} />
        </div>
    );
}
export default App;
```

# filter로 아이템 삭제하기
* 배열의 filter 메소드는 각 요소들마다 call back 함수를 실행해서 리턴값이 트루일 경우만 걸러내는 함수
* 예시 코드
```javascript
// 아래 코드의 실행 순서
// ReviewList.js
import './ReviewList.css';

function formatDate(value) {
  const date = new Date(value);
  return `${date.getFullYear()}. ${date.getMonth() + 1}. ${date.getDate()}`;
}

function ReviewListItem({ item, onDelete }) {
  const handleDeleteClick = () => {
    onDelete(item.id);
  };

  return (
    <div className="ReviewListItem">
      <img className="ReviewListItem-img" src={item.imgUrl} alt={item.title} />
      <div>
        <h1>{item.title}</h1>
        <p>{item.rating}</p>
        <p>{formatDate(item.createdAt)}</p>
        <p>{item.content}</p>
        <button onClick={handleDeleteClick}>삭제</button>
      </div>
    </div>
  );
}

function ReviewList({ items, onDelete }) {
  return (
    <ul>
      {items.map((item) => {
        return (
          <li key={item.id}>
            <ReviewListItem item={item} onDelete={onDelete} />
          </li>
        );
      })}
    </ul>
  );
}

export default ReviewList;

// App.js
import { useState } from 'react';
import ReviewList from './ReviewList';
import mockItems from '../mock.json';

function App() {
  const [order, setOrder] = useState('createdAt');
  const [items, setItems] = useState(mockItems);
  const sortedItems = items.sort((a, b) => b[order] - a[order]);

  const handleNewestClick = () => setOrder('createdAt');

  const handleBestClick = () => setOrder('rating');

  const handleDelete = (id) => {
    const nextItems = items.filter((item) => item.id !== id);
    setItems(nextItems);
  };

  return (
    <div>
      <div>
        <button onClick={handleNewestClick}>최신순</button>
        <button onClick={handleBestClick}>베스트순</button>
      </div>
      <ReviewList items={sortedItems} onDelete={handleDelete} />
    </div>
  );
}

export default App;
```

# 데이터 가져오기
* 네트워크 데이터
* fetch 함수 사용. `fetch('url');` request 실행 후 네트워크 탭에서 response 확인 가능
* paging prop: 데이터 추가로딩에 쓸 값
* reviews: 우리가 받아서 사용할 데이터. 배열
```javascript
export async function getReviews() { // async라서 비동기 함수
  const response = await fetch('https://learn.codeit.kr/api/film-reviews');
  const body = await response.json(); // 기다렸다가
}
```

# useEffect로 초기 데이터 가져오기
* 콜백 함수를 한번만 실행하기 해줌
```javascript
// App.js
import { useEffect, useState } from 'react';

// 아래 함수를 실행하면 App 함수 실행 -> handleLoad 실행 -> 다시 App 실행으로 무한루프를 돌게 됨
// 이런 경우를 위해 한번만 실행하는 useEffect 함수를 사용
const handleLoad = async () => {
  const { reviews } = await getReviews();
  setItems(reviews);
};

useEffect(() => {
  handleLoad();
}, []); // 배열은 dependency임
```

# 서버에서 정렬된 데이터 받아오기
* useEffect 함수의 파라미터
  - 콜백함수: 리액트가 비동기로 실행할 함수
  - 배열: dependency
* useEffect는 콜백 함수를 실행하는 것이 아니라 콜백함수를 예약해두었다가 랜더링이 끝나면 실행함.(디팬던시 리스트도 기억함)
* useEffect 호출 -> handleLoad 함수에서 스테이스 변경 -> 다시 랜더링 -> 콜백함수 예약(dependency list 기억) -> useEffect 호출 -> dependency list 비교
* 쿼리를 사용. url 뒤에 `?order=rating` 같이 활용해서 정렬할 수 있음. 예:`fetch(https://google.com/list?order=rating`)
```javascript
// 처음 한 번만 실행하기
useEffect (() => {
  , []});

// 값이 바뀔 때마다 실행하기
useEffect (() => {
  }, [dep1, dep2, dep3, ...]);
```

# 페이지네이션
* 렌더링하는데만 필요한 정보를 조금씩 나눠서 가져오는 것
* 유튜브의 댓글이 스크롤 할때마다 더 로드 되는 것

* 오프셋 페이지네이션: 상쇄하다. 지금까지 받아온 데이터의 갯수를 기준. 데이터가 추가되거나 삭제가 되면 누락 혹은 중복의 위험이 있음
* 커서 기반 페이지네이션: 데이터를 가리키는 값. 지금까지 받은 데이터를 표시하는 책갈피. 메모리 주소를 가리키는 포인터 같은 역할
```javascript
//offset request
// offset=지금까지 받은 데이터 갯수, limit=더 받아올 데이터 갯수
get https://example.com/posts?offset=20&limit=10

//cursor request
get https://example.com/posts?limit=10
```

# 데이터 더 불러오기
```javascript
// api.js
export async function getReviews({
  order = 'createdAt',
  offset = 0,
  limit = 6,
}) {
  const query = `order=${order}&offset=${offset}&limit=${limit}`;
  const response = await fetch(
    `https://learn.codeit.kr/api/film-reviews?${query}`
  );
  const body = await response.json();
  return body;
}

// App.js
import { useEffect, useState } from 'react';
import ReviewList from './ReviewList';
import { getReviews } from '../api';

const LIMIT = 6;

function App() {
  const [order, setOrder] = useState('createdAt');
  const [offset, setOffset] = useState(0);
  const [hasNext, setHasNext] = useState(false);
  const [items, setItems] = useState([]);
  const sortedItems = items.sort((a, b) => b[order] - a[order]);

  const handleNewestClick = () => setOrder('createdAt');

  const handleBestClick = () => setOrder('rating');

  const handleDelete = (id) => {
    const nextItems = items.filter((item) => item.id !== id);
    setItems(nextItems);
  };

  const handleLoad = async (options) => {
    const { paging, reviews } = await getReviews(options);
    if (options.offset === 0) {
      setItems(reviews);
    } else {
      setItems((prevItems) => [...prevItems, ...reviews]);
    }
    setOffset(options.offset + options.limit);
    setHasNext(paging.hasNext);
  };

  const handleLoadMore = async () => {
    await handleLoad({ order, offset, limit: LIMIT });
  };

  useEffect(() => {
    handleLoad({ order, offset: 0, limit: LIMIT });
  }, [order]);

  return (
    <div>
      <div>
        <button onClick={handleNewestClick}>최신순</button>
        <button onClick={handleBestClick}>베스트순</button>
      </div>
      <ReviewList items={sortedItems} onDelete={handleDelete} />
      {hasNext && <button onClick={handleLoadMore}>더 보기</button>}
    </div>
  );
}

export default App;
// 위 코드에서 <button disabled={!hasNext}...>더 보기</button> 으로 버튼을 숨기지 않고 비활성화 시킬 수 있음
```