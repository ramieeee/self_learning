[toc]

# 1. 머신러닝 종류

* 지도학습: 문제에 대한 답을 가르쳐줌(스팸메일)
* 비지도학습: 답이 없고 답을 유추해냄

# 2. k-최근접 이웃 알고리즘(kNN)

* 가장 가까운 이웃 데이터 k개를 찾음.
* k는 그냥 자연수
* 더 많은 데이터가 있을수록 신뢰가 있기 때문에 머신러닝이라고 할 수 있음

# 3. 머신러닝 기본 수학

## 1) 선형대수학

* 일차함수를 사용함

$$
f(x_0,x_1...x_n)=a_0x_0+a_1x_1+...+a_nx_n+b
$$

* 위와 C:\Users\Ramie\codeit\test.py C:\Users\Ramie\codeit\test2.py같이 계수와 변수들을 x0, x2 로 사용함. 마지막 상수항은 b

## 2) 행렬과 벡터

### a. 행렬

* 행렬 = 메트릭스
* 직사각형 모양의 행과 열
* A 라는 행렬 안의 각각의 수를 원소라고 부름
* 주로 대문자 알파벳을 씀

### b. 벡터

* 행이 하나밖에 없거나 열이 하나밖에 없는 행렬
* 열이 하나면 열 벡터, 행이 하나면 행 벡터
* 열 벡터를 사용하는 경우가 훨씬 많음.
* 백터의 차원은 원소 개수로 얘기함. 열백터의 원소가 5개면 5차원의 열 벡터
* 주로 소문자 알파벳을 씀

$$
a_1 =a의 첫번째원소
$$

# 4. numpy 행렬 사용

```python
import numpy as np

A = np.array([
    [1, -1, 2],
    [2, 3, 6]
])

B = np.array([[ 0, 1],
              [ 1, 4],
              [ 5, 2]])

C = np.random.rand(3, 5)  # 0 - 1 범위의 랜덤 숫자로 3행 5열을 채워줌

D = np.zeros((2, 4))  # 0으로 행렬을 채우려면 괄호를 하나 더 추가 해야함

print(A)
print(B)
print(C)
print(D)
```

# 5. 행렬 연산

## 1) 행렬 덧셈

* 같은 위치의 원소끼리 더함. 두 행렬의 차원이 같아야함

```python
import numpy as np

A = np.array([
    [1, 1],
    [2, 3]
])

B = np.array([
    [3, 2],
    [6, 2]
])

print(A + B)
# [[4 3]
# [8 5]]
```

## 2) 행렬 곱셈

* 스칼라 곱(선형 대수에서는 행렬이 아닌 일반 수를 스칼라 라고 함)

```python
import numpy as np

i = 5

A = np.array([
    [1, 4],
    [2, 3]
])

print(i * A) # 각 원소에 i(5)를 곱해주면 됨
# [[ 5 20]
#  [10 15]]
```

## 3) 두 행렬의 곱

### a. 내적곱

* A의 열 수와 B의 행 수가 같아야 함(원소 개수가 같아야함)
* A = m x n 행렬, B = n x p 행렬일때 AB = m x p 행렬이 나옴
* 교차 법칙 성립 X (AB != BA)

$$
\begin{matrix}
A =\begin{bmatrix}
1 & 3 & 1\\
2 & 2 & 1
\end{bmatrix}
\\
\\
B =\begin{bmatrix}
5 & 6\\
4 & 2\\
3 & 1
\end{bmatrix}
\end{matrix}
$$

$$
\begin{matrix}
AB &=&\begin{bmatrix}
1 \times 5 + 3 \times 4 + 1 \times 3 & 1 \times 6 + 3 \times 2 + 1 \times 1\\
2 \times 5 + 2 \times 4 + 1 + 3 & 2 \times 6 + 2 \times 2 + 1 \times 1
\end{bmatrix}
\\
\\
AB &=&\begin{bmatrix}
20 & 13\\
21 & 17
\end{bmatrix}
\end{matrix}
$$

### b. 요소별 곱하기(Element-wise Multiplication)

* 행렬 덧셈 연산과 거의 똑같은 성질을 갖음(행렬의 수가 같을 때)
* 곱셈 표기를 동그라미(o)를 써서 표현(A o B)

### c. 행렬의 곱 메소드, dot

```python
import numpy as np

A = np.array([
    [1, 3, 1],
    [2, 2, 8],
    [5, 6, 3]
])

B = np.random.rand(3, 3)

print(np.dot(A, B))
# 혹은 print(A @ B)를 해도 dot 메소드와 같이 행렬 곱셈을 해줌
```

## 4) 일반 연산처럼 사용 가능

```python
import numpy as np

A = np.array([
    [1, 3, 1],
    [2, 2, 8],
    [5, 6, 3]
])

B = np.random.rand(3, 3)

print(A @ B + (A + 2 * B)) # 일반 연산처럼 괄호 안 곱셈 먼저 계산
```

## 5) 특수 행렬들

### a. 전치 행렬(transposed matrix)

$$
A =\begin{bmatrix}
1 & 2 & 1\\
3 & 2 & 2
\end{bmatrix}
$$

* A가 A^T로 바뀌는 것. 첫번째 행이 첫번째 열로 바뀜

$$
A^T =\begin{bmatrix}
1 & 3\\
2 & 2\\
1 & 2
\end{bmatrix}
$$

```python
import numpy as np

A = np.array([
    [1, -1, 2],
    [3, 2, 2],
    [4, 1, 2]
])

A_transpose = np.transpose(A) # 혹은 A_transpose = A.T
print(A_transpose)
```



### b. 단위 행렬(identity matrix)

* 항상 정사각형의 행렬임
* I(대문자 i)로 표현함
* 단위 행렬을 곱하면 기존 행렬은 그대로 유지됨

$$
I =\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

```python
import numpy as np

A = np.array([
    [1, -1, 2],
    [3, 2, 2],
    [4, 1, 2]
])

I = np.identity(3)
print(A @ I)
```



### c. 역행렬(inverse matrix)

* 행렬에 역행렬을 곱하면 단위행렬이 나옴
* 항상 정사각형이어야 함
* 모든 행렬에 역행렬이 있는것은 아님

```python
import numpy as np

A = np.array([
    [1, -1, 2],
    [3, 2, 2],
    [4, 1, 2]
])

A_inverse = np.linalg.pinv(A)
print(A_inverse)
print(A @ A_inverse)

# np. linalg.det(A) 를 실행하고 0이 나오면 역행렬이 존재하지 않고 0이 아니면 역행렬이 존재함
```

# 6. 선형대수학

* 일차식, 일차함수, 행렬, 벡터를 다루는 학문
* Ax = y
* a머신 러닝을 할 때는 데이터를 일차식에 사용하는 경우가 많음
* 행렬을 이용하면 정돈된 형태로 효율적인 계산을 할 수 있음

```
# 집값 = 크기 X a1 + 지하철 역 거리 X a2 + 층수 X a3
첫번째: 110 x a1 + 400 x a2 + 20 x a3
두번째: 100 x a1 + 1000 x a2 + 5 x a3
...
```

* 위의 데이터를 식으로 표현하면

$$
X =\begin{bmatrix}
110 & 400 & 20\\
100 & 1000 & 5\\
\cdots & \cdots & \cdots
\end{bmatrix}

\quad a =\begin{bmatrix}
a1\\
a2\\
a3
\end{bmatrix}
$$

* 모든 집 값 = Xa

# 7. 미분

## 1) 함수

* input을 가지고 계산을 해서 output을 내는 것
* y = 3x + 6 같은 것(y는 x에 대한 함수라고 읽음)
* f(x) = 3x + 6으로도 표현 가능
* 하나의 인풋에 대해 하나의 아웃풋만
* input이 여러개일수도 있고(다변수 함수) 차수도 2, 3차일 수 있음

## 2) 그래프

* 수학 식을 시각적으로 표현하는 방법
* x축 y축이 필요
* 1차함수: 직선
* 2차함수: 휘어진 아치 모양(y = x^2 - 2x + 1)
* 함수의 최소점을 볼 수 있음. 값이 어떻게 변하는지 시각적으로 표현 가능

## 3) 평균 변화율

* 기울기: x가 변화할 때, y는 얼마나 빠르게 변하는지 알려줌
* 1차함수: x가 1 증가할때 y가 2 증가하면 기울기는 2 (기울기: 2 / 1 = 2)
* 2차함수: 순간 변화율을 계산해야함. 순간 변화율을 계산하려면 평균 변화율을 알아야함

$$
f(b)-f(a) \over b-a
$$


$$
f(a+h)-f(a) \over h
$$


* 예를들어 위 식에서 x를 의미하는 a가 1이고(1, 0) b가 2(2, 1) 이면 y인 f(b), f(a)가 각각 1, 0이 되는 곡선이 있다면 세부 식은 아래와 같고 답은 1임

$$
1 - 0 \over 2 - 1
$$

## 4) 순간 변화율

* 범위를 극한으로 줄여서 기울기를 구하는 것

$$
\lim_{b \to 0} \frac {f(a+h)-f(a)}{h}
$$

* f(x) = x^2 - 2x + 1 이란 함수일때

$$
\displaylines{
&=& \lim_{b \to 0} \frac {[(2+h)^2-2 \times (2+h)+1]-[(2)^2-2 \times (2) + 1]}{h}
\\\\
&=& \lim_{h \to 0} \frac {h^2+2h}{h}
\\\\
&=& \lim_{h \to 0} h+2
\\\\
&=&2
}
$$

* h가 0에 무한대로 가깝기 때문에 0을 대입하면 값은 2임
* 여기에 x=1 을 대입하면 값은 0이 나옴(가장 바닥 부분이기 때문에)

## 5) 미분

* 만약 2차함수 식이 아래와 같다면

$$
\displaylines{
f(x)=x^2-2x+1\\
\\
\lim_{h \to 0} \frac {f(x+h)-f(x)}{h}
\\\\
=& \lim_{h \to 0} \frac {[(x+h)^2-2\times(x+h)+1]-[(x)^2-2\times(x)+1]}{h}
\\\\
=& \lim_{h \to 0} \frac {x^2+2xh+h^2-2x-2h+1-x^2+2x-1}{h}
\\\\
=& \lim_{h \to 0} \frac {2xh+h^2-2h}{h}
\\\\
=& \lim_{h \to 0} 2x+h-2
\\\\
=& 2x-2
}
$$

* x값만 대입하면 원하는 곳의 순간 기울기를 구할 수 있음
* 함수로도 표현 가능한데 아래와 같이 f프라임 이라고 말함

$$
f\prime(x)
$$

* 위의 식에 대입하면

$$
\displaylines{
f\prime(x)=2x-2
\\f\prime(x)는 기존 함수 f(x)의 미분이다
}
$$

* 다른 방식으로 미분 식을 쓸 수 있음

$$
\frac{d}{dx}f(x)
$$

* 차수의 숫자를 상수와 곱하고 차수를 -1 해줌

$$
\displaylines{
f(x)=x^2-2x+1일때
\\\\
x^2의\space 2를\space 앞으로\space 가져오고\space -1해줘서\space 2x가\space 되고\\
2x의\space 차수\space 1을\space -2와\space 곱하고\space x^{1-0}은\space x^0이니까\space 1이되어\space -2가\space 됨.\\
상수항은\space 날려버림
\\\\
\frac{d}{dx}f(x)=2x-2
}
$$

