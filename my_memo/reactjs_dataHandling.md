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