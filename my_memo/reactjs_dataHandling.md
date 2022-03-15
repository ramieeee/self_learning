# map으로 배열 렌더링
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
      {items.map((item) => (
        <li>
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
          <li>
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