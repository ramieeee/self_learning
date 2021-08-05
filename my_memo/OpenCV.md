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
cv2.setMouseCallback("image",  draw_rectangle)

while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

## 5) 카메라 영상에 시간 출력

```python
import cv2
import time

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID) # 동영상 파일명 대신 카메라 번호 입력하면 카메라 입력을 캡처하여 출력 가능
if cam.isOpened() == False:  # 카메라 작동 안할 시
    print
    'Cannot open the Camera(%d)' %(CAMERA_ID)
    exit()

cv2.namedWindow('CAM_Window') # 창 이름 정의

while(True): # waitKey가 1000일때까지 무한 반복(계속 실행되는 상태)
    ret, frame = cam.read() # 영상 캡처
    now = time.localtime()
    str = "%d. %d. %d. %d:%d:%d" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) # 시간 정의

    cv2.putText(frame, str, (0, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 0)) # 텍스트(시간) 넣기

    cv2.imshow('CAM_Window', frame)
    if cv2.waitKey(1000) >= 0:
        break

    cam.release()
    cv2.destroyWindow('CAM_Window')
```

## 6) TrackBar 예제

* 범위 값을 조절하여 이미지의 변화 상태를 확인하기 위해 사용함

```python
import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('RGB track bar')
cv2.createTrackbar('Red color', 'RGB track bar', 0, 255, nothing) # 트랙바 생성
cv2.createTrackbar('Green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('Blue color', 'RGB trackbar', 0, 255, nothing)

cv2.setTrackbarPos('Red color', 'RGB track bar', 125)
cv2.setTrackbarPos('Green color', 'RGB track bar', 125)
cv2.setTrackbarPos('Blue color', 'RGB track bar', 125)

img = np.zeros((512, 512, 3), np.uint8)

while(1):
    redval = cv2.getTrackbarPos('Red color', 'RGB track bar')
    greenval = cv2.getTrackbarPos('Green color', 'RGB track bar')
    blueval = cv2.getTrackbarPos('Blue color', 'RGB track bar')

    cv2.rectangle(img, (0, 0), (512, 512), (blueval, greenval, redval), -1)
    cv2.imshow('RGB track bar', img)
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

## 7) 아날로그 시계 예제

```python
import cv2
import time
from math import *
import numpy as np

cv2.namedWindow('Clock')

img = np.zeros((512, 512, 3), np.uint8)
while (True):
    cv2.circle(img, (256, 256), 250, (125, 125, 125), -1)

    now = time.localtime()
    hour = now.tm_hour
    min = now.tm_min
    if hour > 12:
        hour -= 12

    Ang_Min = min * 6 # 분침이 0시부터 이루는 각
    Ang_Hour = hour * 30 + min * 0.5 # 시침이 0시부터 이루는 각

    if (hour == 12 or 1 <= hour <= 2): # 시침이 가리키는 좌표를 계산하여 중심으로부터 시침을 그림
        x_pos = int(150.0 * cos((90.0 - Ang_Hour) * 3.141592 / 180))
        y_pos = int(150.0 * sin((90.0 - Ang_Hour) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 - y_pos), (0, 255, 0), 6)
    elif (3 <= hour <= 5):
        x_pos = int(150.0 * cos((Ang_Hour - 90.0) * 3.141592 / 180))
        y_pos = int(150.0 * cos((Ang_Hour - 90.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 + y_pos), (0, 255, 0), 6)
    elif (6 <= hour <= 8):
        x_pos = int(150.0 * cos((Ang_Hour - 180.0) * 3.141592 / 180))
        y_pos = int(150.0 * cos((Ang_Hour - 180.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 + y_pos), (0, 255, 0), 6)
    elif (9 <= hour <= 11):
        x_pos = int(150.0 * cos((Ang_Hour - 270.0) * 3.141592 / 180))
        y_pos = int(150.0 * cos((Ang_Hour - 270.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 - y_pos), (0, 255, 0), 6)


    if (min == 0 or 1 <= hour <= 14): # 분침이 가리키는 좌표를 계산하고 분침을 그림
        x_pos = int(200.0 * cos((90.0 - Ang_Min) * 3.141592 / 180))
        y_pos = int(200.0 * sin((90.0 - Ang_Min) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 - y_pos), (0, 255, 0), 6)
    elif (15 <= hour <= 29):
        x_pos = int(200.0 * cos((Ang_Min - 90.0) * 3.141592 / 180))
        y_pos = int(200.0 * sin((Ang_Min - 90.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 + y_pos), (255, 0, 0), 1)
    elif (30 <= hour <= 44):
        x_pos = int(200.0 * sin((Ang_Min - 180.0) * 3.141592 / 180))
        y_pos = int(200.0 * cos((Ang_Min - 180.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 + y_pos), (255, 0, 0), 1)
    elif (45 <= hour <= 59):
        x_pos = int(200.0 * cos((Ang_Min - 270.0) * 3.141592 / 180))
        y_pos = int(200.0 * sin((Ang_Min - 270.0) * 3.141592 / 180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 - y_pos), (255, 0, 0), 1)

    cv2.imshow('Clock', img)
    if cv2.waitKey(10) >= 0:
        break

cv2.destroyWindow('Clock')
```

## 8) 자유 낙하 운동

```python
import cv2
from math import *
import numpy as np

cv2.namedWindow('Free Fall')

width = 512
height = 960
img = np.zeros((height,width,3), np.uint8)

time = ypos = 0
while True:
    if ypos + 30 < height: # 공의 위치 검토
        cv2.circle(img, (256, 30 + ypos), 10, (255, 0, 0), -1)
        time += 1
        ypos = int((9.8 * time ** 2) / 2) # 시간이 증가함에 따라 위치 계산
        print(time, ':', ypos)
    cv2.imshow('Clock', img)
    if cv2.waitKey(100) >= 0:
        break

cv2.destroyWindow('Free Fall')
```

## 9) 포물선 운동

```python
import cv2
from math import *
import numpy as np

init_Vel = float(input("초기 속도를 입력하세요: "))
init_Ang = float(input("초기 각도를 입력하세요: "))
cv2.namedWindow('Parabolic Motion')

width = 960
height = 960
img = np.zeros((height,width,3), np.uint8)

time = xpos = ypos = 0
init_posx=30
init_posy=250
Vel_x = int(init_Vel * cos(init_Ang * pi / 180.0))
Vel_y = int(-1.0 * init_Vel * sin(init_Ang * pi / 180.0))

while True:
    if ypos + 30 < height:
        cv2.circle(img, (init_posx+xpos, init_posy+ypos), 10, (255, 0, 0), -1)
        time += 0.2
        Vel_y = int(Vel_y + 9.8 * time)

        xpos = int(xpos + Vel_x * time)
        ypos = ypos + int(Vel_y * time) + int((9.8 * time ** 2) / 2)
        print(time, ':', xpos, ypos)

    cv2.imshow('Parabolic Motion', img)
    
    if cv2.waitKey(100) >= 0:
        break

cv2.destryWindow('Parabolic Motion')
```

## 10) 피보나치 수열 그래픽

*  

