[toc]

# 1. 설치

* python -m pip install --upgrade pip -> pip 업그레이드
* pip install opencv-python opencv-contrib-python 설치

# 2. OpenCV

## 1) 이미지 로드

* image 타이틀을 가지는 새로운 윈도우 생성한 후 image.PNG 파일을 출력

```python
import cv2

img = cv2.imread("image.PNG", 1) # 이미지 로드

cv2.namedWindow("image") # 창 이름을 image로 설정
cv2.imshow("image", img) # 로드한 이미지를 image라는 이름으로 출력
cv2.waitKey() # 파라미터에 숫자 입력. 해당 시간만큼 창이 열려있음
```

## 2) OpenCV 기본 자료형

* 객체 기반의 Mat 자료형. Matrix의 단어에서 따온 변수명으로 실제 행렬 연산에도 활용 가능
* Mat의 멤버 변수로 uchr* 타입의 data 포인터 변수가 있음. Matrix의 Data를 가리키는 포인터 변수
* 영상 데이터는 3가지 색상(RGB) 채널로 구성되어 있으며, RGB 채널의 빅셀별 데이터는 붉은색, 초록색, 파란색이 반복되면 저장된다
* Mat 자료형 외에도 numpy array를 통해 영상의 픽셀별 제어 가능

```python
import numpy as np
import cv2 as cv

img = cv.imread('image.PNG')

height = img.shape[0]
width = img.shape[1]

for y in range(0, height):
    img.itemset(y, int(width / 2), 0, 0)
    img.itemset(y, int(width / 2), 1, 0)
    img.itemset(y, int(width / 2), 2, 255)
for x in range(0, width):
    img.itemset(int(height / 2), x, 0, 255)
    img.itemset(int(height / 2), x, 1, 0)
    img.itemset(int(height / 2), x, 2, 0)

cv.imshow("win", img)
cv.waitKey(0)
```

## 3) 동영상 파일 활용

```python
import cv2

cap = cv2.VideoCapture("vtest.avi") # cap 변수에 비디오 파일 포인터 지정

while cap.isOpened(): # 비디오 파일이 열려 있을 동안 반복
    success, frame = cap.read() # read함수를 사용하여 화면을 가져옴
    if success:
        cv2.imshow("image", frame)

        key = cv2.waitKey(0) & 0xFF
        if(key == 27):
            break
        else:
            break

cap.release()
cv2.destroyAllWindows()
```

## 4) 마우스 이벤트 활용

* 마우스 버튼 클릭, 드래그 등 마우스 입력 장치 관련 이벤트가 발생할 경우 처리할 함수를 Callback 함수로 정의

```python
import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img, (x,y), (x+50, y+50), (255, 0, 0), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_rectangle)

while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

