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

cv2.destroyWindow('Parabolic Motion')
```

# 3. 컴퓨터 비전

* 레벨: 픽셀이 가질 수 있는 값의 범위
* 채널: 픽셀이 몇 개의 값으로 구성되는지를 의미
* 이진 영상: 흑백 2가지 레벨, 채널의 수는 1
* OpenCV에서는 threshold()함수로 영상 이진화를 수행할 수 있음

## 1) threshold(src, thresh, maxval, type, dst=None)

* src: 입력 행렬(다중 채널, 8비트 또는 32비트의 실수)
* thresh: 임계치
* maxval: 특정 방법(THRESH_BINARY, THRESH_BINARY_INV)을 사용할 때에 반환값의 최댓값
* type: 이진화 방법(THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO, THRESH,_TOZERO_INV, THRESH_MASK, THRESH_OTSU, THRESH_TRIANGLE)
* dst: 결과 행렬(입력 행렬과 동일한 크기와 채널의 수를 가짐)

## 2) 영상 밝기 조절

* 한 픽셀이 8비트로 표현될 때 영상이 전반적으로 밝게 보인다면 흰색(255)에 근접한 값을 가지는 픽셀의 비중이 높으며, 반대로 검은색(0)에 가까운 값을 가지는 픽셀의 비중이 낮은 것임

## 3) 명암비

* 밝은 영역과 어두운 영역의 밝기 차이를 의미

## 4) 히스토그램 분석

* 가로축: 데이터 값. (일반적으로 Bin 이라고 표현)
* 세로축: 해당 데이터 값의 발생 빈도. [0, w x h]의 값을 가질 수 있음
* OpenCV에서는 calcHist()를 활용하여 히스토그램 계산 가능

**calcHist([images], [channels], mask, [histSize], [ranges], hist=None, accumulate=None)**

* 입력 영상의 지정된 채널에서 특정 값 범위에 대하여 총 빈 개수가 histSize인 히스토그램을 계산함
* images: 히스토그램을 계산하기 위한 입력 영상
* channels: 입력 영상에 히스토그램을 계산하고자 하는 채널을 지정(그레이 영상은 [0], 컬러 영상은 B,G,R에 대하여 [0], [1], [2]를 사용)
* histSize: 총 빈 개수
* ranges: 가로축의 범위
* accumulate: 히스토그램을 누적하여 사용할지를 지정(True이면 초기화하지 않음)

```python
from matplotlib import pyplot as plt
import cv2
import numpy as np

ch1 = [0]
ch2 = [0]
ch3 = [0]
ranges1 = [0, 256]
ranges2 = [0, 128]
ranges3 = [128, 256]
histSize1 = [256]
histSize2 = [128]
histSize3 = [128]
hist1 = cv2.calcHist([img1], ch1, None, histSize1, ranges1)
hist2 = cv2.calcHist([img1], ch2, None, histSize2, ranges2)
hist3 = cv2.calcHist([img1], ch3, None, histSize3, ranges3)

bin_x1 = np.arange(256)
bin_x2 = np.arange(128)
bin_x3 = np.arange(128) +128
plt.title("Histogram")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.plot(bin_x1, hist1, color='b')
plt.bar(bin_x2, hist2[:,0], width=6, color='r')
plt.bar(bin_x3, hist3[:,0], width=6, color='g')
plt.grid(True, lw=1, ls='--', c='.75')
plt.xlim([0,255])
```
