# nodejs

# 모듈 불러오기

- require 함수로 불러올 수 있음

```javascript
// index.js에서 math.js의 sum 함수를 불러오기
const math = require("./math");

console.log(math.sum(1, 2)); // 3
```

# 파일시스템 모듈

- fs.readFile: 비동기로 동작
- fs.readFileSync: 동기로 동작

```javascript
const fs = require("fs");
const data = fs.readFileSync("./data.txt", "utf-8");

console.log(data); // data.txt에 있는 내용이 출력됨
```

```javascript
const fs = require("fs");

const data2 = fs.readFile("./data.txt", "utf8", (err, data) => {
  console.log(data); // 파라미터의 콜백으로 비동기 함수 실행
});
```
