# nextjs

# route

- 기본적으로 route를 위한 라이브러리가 필요 없고 pages 디렉토리 밑에 파일명이 route가 됨.
  만약 파일명이 pages/helloworld.tsx이면 localhost:3000/helloworld 하면 해당 파일로 접근

# dinamic pages

- [id].tsx 와 같이 페이지를 동적으로 동작하도록 설정 가능

# Server Side Rendering

- client에서는 이 함수를 못봄
- 해당 함수는 컴포넌트 바깥에 위치해야함
- 컴포넌트가 마운트 되기 전에 수행됨

```javascript
const TestPage = ({ data }) => {
  return (
    <>
      <h1>{data}</h1>
    </>
  );
};

export async function getServerSideProps() {
  // 해당 함수 내에 있는 코드들은 클라이언트에게 보여지지 않음
  const { events_categories } = await import("./data/data.json");

  return {
    props: {
      data: events_categories,
    },
  };
}
```
