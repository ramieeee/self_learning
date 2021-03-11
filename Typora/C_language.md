목차

[toc]

---

# 1. C 언어 함수

## 1) main 함수

진입점 함수라고도 불림. 해당 함수로 인해서 컴퓨터가 소스코드의 시작점을 인식함

```c
#includ <stdio.h>
int main(void) //진입점 함수
{
    printf("hello!");
    return 0;  // 프로그램을 정상적으로 마칠 때 return 0;이 사용 됨
}
```

* int: 출력 형태
* main: 함수 이름
* void: 입력 형태

* 서식문자(conversion specifier): 출력의 형태를 지정하는 용도

```c
// 숫자 출력을 위해서
#includ <stdio.h>
int main(void)
{
    printf("%d", 1234); // %d는 뒤의 1234를 호출해와 출력한다
    return 0;
}

// 출력값: 1234
```



## 2) printf 함수

### a. 특수문자

문자열 안에 큰 따옴표는 아래와 같이 표현함. 이를 특수문자라고 하는데 종류는 아래와 같다.

```c
int main(void)
{
    printf("강아지가 짖는다. \"멍! 멍!\"");
}
```

| 특수문자 |               의미                |
| :------: | :-------------------------------: |
|    \a    |              경고음               |
|    \b    |       백스페이스(backspace)       |
|    \f    | 폼 피드(form feed). 프린터 출력용 |
|    \n    |          개 행(new line)          |
|    \r    |   캐리지 리턴(carriage return)    |
|    \t    |              수평 탭              |
|    \v    |      수직 탭. 프린터 출력용       |
|   \ '    |         작은 따옴표 출력          |
|   \ "    |          큰 따옴표 출력           |
|    \?    |                                   |
|    \\    |           역슬래쉬 출력           |



### b. 서식문자

출력할 때 숫자를 특정 서식으로 출력하게 하는 문자(예: %d, %f, %x 등)

| 서식문자 | 출력 대상(자료형) |            출력 형태            |
| :------: | :---------------: | :-----------------------------: |
|    %d    | char, short, int  |      부호 있는 10진수 정수      |
|   %ld    |       long        |      부호 있는 10진수 정수      |
|   %lld   |     long long     |      부호 있는 10진수 정수      |
|    %u    |   unsigned int    |      부호 없는 10진수 정수      |
|    %o    |   unsigned int    |      부호 없는 8진수 정수       |
|  %x, %X  |   unsigned int    |      부호 없는 16진수 정수      |
|    %f    |   float, double   |  10진수 방식의 부동소수점 실수  |
|   %Lf    |    long double    |  10진수 방식의 부동소수점 실수  |
|  %e, %E  |   float, double   | e 또는 E 방식의 부동소수점 실수 |
|  %g, %G  |   float, double   | 값에 따라 %f와 %e 사이에서 선택 |
|    %c    | char, short, int  |       값에 대응하는 문자        |
|    %s    |       char*       |             문자열              |
|    %p    |       void*       |        포인터의 주소 값         |



* 정수 출력을 위한 서식 문자들: %d, %u, %o, %x

* 서식문자 %o와 %x 사이에 문자 #을 넣어 정보를 더 정확하게 전달할 수 있음

```c
int main(void)
{
    int num1 = 7, num2 = 13;
    printf("%o %#o \n", num1, num1); // 값: 7 07
    printf("%x %#x \n", num2, num2); // 값: d 0xd
}
```



* 실수의 출력을 위한 서식 문자들: %f, %e, %g
* %g는 소수점 이하의 자릿수가 늘어나면 e 표기법으로 출력함.

```c
#include <stdio.h>

int main(void)
{
    double d1 = 1.23e-3;  // 0.00123
    double d2 = 1.23e-4;  // 0.000123
    double d3 = 1.23e-5;  // 0.0000123
    double d4 = 1.23e-6;  // 0.00000123

    printf("%g \n", d1);  // %f 스타일 출력. 값: 0.00123
    printf("%g \n", d2);  // %f 스타일 출력. 값: 0.000123
    printf("%g \n", d3);  // %e 스타일 출력. 값: 1.23e-005
    printf("%g \n", d4);  // %e 스타일 출력. 값: 1.23e-006
    return 0;
}
```



* %s를 이용한 문자열의 출력이 가능



### c. 필드 폭 지정

* %8d : 필드 폭을 8칸 확보하고, 오른쪽 정렬해서 출력을 진행
* %-8d : 필드 폭을 8칸 확보하고, 왼쪽 정렬해서 출력을 진행

```c
#include <stdio.h>

int main(void)
{
    printf("%-8s %3s %5s \n", "이  름", "전공학과", "학년");
    printf("%-8s %3s %5d \n", "연람희", "영어학과", 4);
    return 0;
}
```



## 3) scanf 함수

데이터 값을 입력받아 저장하는 함수. (파이썬의 input)

```c
#include <stdio.h>

int main(void)
{
	int result;
	int num1, num2;

	printf("정수 one: ");
	scanf("%d", &num1); // 사용자 입력 값을 num1에 저장
	printf("정수 two: ");
	scanf("%d", &num2); // 사용자 입력 값을 num2에 저장

	result = num1 + num2;
	printf("%d", result);

    // 서식문자는 출력과 같이 입력도 같은 의미로 사용된다.
    int num1, num2, num3;
	printf("세 개의 정수 입력: ");
	scanf("%d, %o, %x", &num1, &num2, &num3);
    
    // 실수는 double과 long double의 형태로 입력받는다.
    int num1, num2;
    scanf("%lf %Lf", &num1, num2);  // %lf는 double, %Lf는 long double 자료형
    
	return 0;
}
```

* 실수의 입력은 e 표기법을 사용해도 무관 



## 4) 변수

값을 저장할 수 있는 메모리 공간에 붙은 이름, 혹은 메모리 공간 자체

```c
#include <stdio.h>

int main(void)
{
    int num; // num이라는 이름의 변수 선언
    num = 20;
    printf("%d", num);
}

// int: 정수의 저장이 가능한 메모리 공간을 할당
// num: 그리고 그 메모리 공간의 이름을 num이라 함.
```

```c
int num1, num2; // 두개의 변수 선언
int num3=30, num4=40; // 두개의 변수 선언 및 초기화
```

* 변수를 선언만 하고 초기화하지 않으면 쓰레기 값이 저장된다(아무런 의미가 없는 값)
* 변수 선언과 동시에 0으로 초기화한 다음, 이후에 의미있는 값을 저장하기도 함.

```c
int num1=0, num2=0;
```



*보통 변수 선언은 중괄호를 시작할때 지정되어야 컴파일 에러가 나지 않게 조절할 수 있음.

```c
#include <stdio.h>

int main(void)
{
    int num1;
    int num2;
    num1 = 1;
    num2 = 2;
    printf("%d and %d", num1, num2);
}

```



# 2. 연산

## 1) 증가, 감소 연산자

변수에 저장된 값을 1 증가 및 감소시키는 경우에 사용되는 연산자

* ++num: 값을 1 증가 후, 속한 문장의 나머지를 진행(선 증가, 후 연산) 예) val = ++num;
* num++: 속한 문장을 먼저 진행한 후, 값을 1 증가(선 연산, 후 증가 예) val = num++;
* --num: 값을 1 감소 후, 혹한 문장의 나머지를 진행(선 감소, 후 연산) 예) val= --num;
* num++: 속한 문장을 먼저 진행한 후, 값을 1 감소(선 연산, 후 감소) 예) val = num--;

```c
#include <stdio.h>

int main(void)
{
    int num1 = 1;
    int num2 = 1;
    printf("%d \n", ++num1); // 값 2 출력
    printf("%d \n", num2++); // 값 1 출력
    printf("%d", num2); // 값 2 출력
}
```



## 2) 관계 연산자(<, >, ==, !=, <=, >=)

대소와 동등의 관계를 따지는 연산자. 비교 연산자라고도 함.

* 조건을 만족하면 값 1(True)을, 만족하지 않으면 0(False)을 반환.

```c
#include <stdio.h>

int main(void)
{
    int num1 = 10;
    int num2 = 12;
    
    int result1, result2;

    result1 = (num1 != num2);
    result2 = (num1 > num2);

    printf("%d \n", result1); // 값: 1
    printf("%d \n", result2); // 값: 0
}
```

​	*C언어는 0이 아닌 모든 값을 참으로 간주한다



## 3) 논리 연산자(&&, ||, !)

* &&: 예) a && b, a와 b 모두 '참'이면 연산 결과로 '참'을 반환(논리 AND)
* ||: 예) a || b, a 혹은 b 둘 중 하나라도 '참'이면 연산 결과로 '참'을 반환(논리 OR)
* !: 예)!a, a가 '참'이면 '거짓', a가 '거짓'이면 '참'을 반환(논리 NOT)

 

## 4) 콤마 연산자(,)

둘 이상의 변수를 동시에 선언하거나, 둘 이상의 문장을 한 행에 삽입하는 경우에 사용. 또는 구분을 목적으로 주로 사용



# 3. 데이터 표현 방식의 이해

## 1) 10진수, 8진수, 16진수

C언어는 10진수 이외에 8진수, 16진수의 데이터 표현도 허용함.

```c
int num1 = 10; // 특별한 선언이 없으면 10진수의 표현
int num2 = 0xA; // 0x로 시작하면 16진수로 인식
int num3 = 012; // 0으로 시작하면 8진수로 인식
```

```c
#include <stdio.h>

int main(void)
{
	int num1 = 0xa7, num2 = 0x43;
	int num3 = 032, num4 = 024;

	printf("0xA7의 10진수 정수 값: %d \n", num1);  // 167
	printf("0x42의 10진수 정수 값: %d \n", num2);  // 67
	printf(" 032의 10진수 정수 값: %d \n", num3);  // 26
	printf(" 024의 10진수 정수 값: %d \n", num4);  // 20

	printf("%d - %d = %d \n", num1, num2, num1 - num2);  // 167 - 67 = 100
	printf("%d + %d = %d \n", num3, num4, num3 + num4);  // 26 + 20 = 46
	return 0;
}
```

​	

## 2) 정수의 표현 방식

정수의 가장 왼쪽에 존재하는 비트는 부호비트

* 맨 왼쪽 부호가 0이면 양수, 1이면 음수. (해당 비트를 MSB라고 함. Most Significant Bit의 약자로 가장 중요한 비트라는 뜻.)
* 그리고 나머지 비트들은 데이터의 크기를 나타냄.

예) 00000001

위의 예로, 나머지 일곱 비트가 0000001 이므로 크기는 1임. 만약 MSB가 0이고 데이터가 0000101이면 +5 이다.

* 양의 정수 -> 음의 정수: 0과 1을 바꾸고 1을 더해줌.

예) 01101110 -> 10010010: 10진수 값은 110

* 음의 정수 -> 양의 정수: 1을 빼고 0과 1을 바꿈.

예) 10010011 -> 01101101: 10진수 값은 -99



## 3) 비트 연산자

### a. & 연산자: 비트단위 AND

* num1 & num2: 비트 단위로 AND 연산
* 두 개의 피트가 모두 1일 때 1을 반환하는 연산.

```c
0 & 0 // 0을 반환
0 & 1 // 0을 반환
1 & 0 // 0을 반환
1 & 1 // 1을 반환
```

예) & 연산

```c
#include <stdio.h>

int main(void)
{
	int num1 = 15;  // 00000000 00000000 00000000 00001111
	int num2 = 20;  // 00000000 00000000 00000000 00010100
	int num3 = num1 & num2;  // num1과 num2의 비트단위 & 연산

	printf("AND 연산의 결과: %d \n", num3); // 값: 4
	return 0;
}
```

```c
00000000 00000000 00000000 00001111  // 값: 15
00000000 00000000 00000000 00010100  // 값: 20
----------------------------------------------
00000000 00000000 00000000 00000100  // 값: 4
```


### b. | 연산자: 비트단위 OR

* num1 | num2: 비트 단위로 OR 연산
* 두 개의 비트중 하나라도 1이면 1을 반환하는 연산. 

```c
0 | 0  // 0을 반환
0 | 1  // 1을 반환
1 | 0  // 1을 반환
1 | 1  // 1을 반환
```

예)

```c
#include <stdio.h>

int main(void)
{
	int num1 = 15;  // 00000000 00000000 00000000 00001111
	int num2 = 20;  // 00000000 00000000 00000000 00010100
	int num3 = num1 | num2;  // num1과 num2의 비트단위 | 연산

	printf("OR 연산의 결과: %d \n", num3);  // 값: 31
	return 0;
}
```

```c
00000000 00000000 00000000 00001111  // 값: 15
00000000 00000000 00000000 00010100  // 값: 20
----------------------------------------------
00000000 00000000 00000000 00011111  // 값: 31
```



### c. ^ 연산자: 비트단위 XOR

* num1 ^ num2: 비트 단위로 XOR 연산
* 두 개의 비트가 서로 다른 경우에 1을 반환하는 연산

```c
0 ^ 0  // 0을 반환
0 ^ 1  // 1을 반환
1 ^ 0  // 1을 반환
1 ^ 1  // 0을 반환
```

예)

```c
#include <stdio.h>

int main(void)
{
	int num1 = 15;  // 00000000 00000000 00000000 00001111
	int num2 = 20;  // 00000000 00000000 00000000 00010100
	int num3 = num1 ^ num2;  // num1과 num2의 비트단위 ^ 연산

	printf("XOR 연산의 결과: %d \n", num3);  // 값: 31
	return 0;
}
```

```c
00000000 00000000 00000000 00001111  // 값: 15
00000000 00000000 00000000 00010100  // 값: 20
----------------------------------------------
00000000 00000000 00000000 00011011  // 값: 27
```



### d. ~ 연산자: 비트단위 NOT

* ~num;  : 단항 연산자로서 피연산자의 모든 비트를 반전시킴(num은 변화 없음. 반전 결과만 반환)/

*MSB도 반전되어 부호마저 바뀜.

```c
~0  // 1을 반환
~1  // 0을 반환
```

예)

```c
#include <stdio.h>

int main(void)
{
	int num1 = 15;  // 00000000 00000000 00000000 00001111;
	int num2 = ~num1;
	printf("NOT 연잔의 결과: %d\n", num2);  // 값: -16 (11111111 11111111 11111111 11110000)
	return 0;
}

// -16이란 값은 11111111 11111111 11111111 11110000 에 2의 보수를 취하면 00000000 00000000 00000000 00010000(+16)이 나오므로 -16이란것을 알 수 있음.
```



### e. <<연산자: 비트의 왼쪽 이동(Shift)

* num<<2;  : 피연산자의 비트 열을 왼족으로 이동(num은 변화 없음, 두 칸 왼쪽 이동 결과만 반환)
* num1 << num2: num1의 비트 열을 num2칸씩 왼쪽으로 이동시킨 결과를 반환
* 8 << 2: 정수 8의 비트 열을 2칸씩 왼족으로 이동시킨 결과를 반환

예)

```c
# include <stdio.h>

int main(void)
{
	int num = 15;  // 00000000 00000000 0000000 00001111
	
	int result1 = num << 1;  // num의 비트 열을 왼쪽으로 1칸씩 이동
	int result2 = num << 2;  // num의 비트 열을 왼쪽으로 2칸씩 이동
	int result3 = num << 3;  // num의 비트 열을 왼쪽으로 3칸씩 이동

	printf("1칸 이동 결과: %d \n", result1);  // 값: 30
	printf("2칸 이동 결과: %d \n", result2);  // 값: 60
	printf("3칸 이동 결과: %d \n", result3);  // 값: 120
	return 0;
}
```

```c
00000000 00000000 00000000 00011110  // 10진수 값: 30
00000000 00000000 00000000 00111100  // 10진수 값: 60
00000000 00000000 00000000 01111000  // 10진수 값: 120
```

*비트 열을 왼쪽으로 1칸씩 이동시킬 때마다 정수의 값은 두 배가 된다.

*비트 열을 오른쪽으로 1칸씩 이동시킬 때마다 정수의 값은 2로 나누어진다.

* 곱셈과 나눗셈 연산은 비트의 이동 연산으로 대체할 수 있다.



### f. >>연산자: 비트의 오른쪽 이동(Shift)

* num>>2;  : 피연산자의 비트 열을 오른쪽으로 이동(num은 변화 없음, 두 칸 오른쪽으로 이동 결과만 반환)
* num1 >> num2: num2의 크기만큼 num1의 비트 열이 오른쪽으로 이동.
* MSB가 0이라면(양수라면) 이동으로 인해 밀려나는 오른쪽의 비트들은 소멸되고 왼쪽의 빈 자리는 0으로 채워짐.
* MSB가 -라면(음수라면) CPU에 따라 결과가 달라짐.

```c
#include <stdio.h>
int main(void)
{
	int num = -16;  // 11111111 11111111 11111111 11110000
	printf("2칸 오른쪽 이동의 결과: %d\n", num >> 2);  // 값: -4
	printf("3칸 오른쪽 이동의 결과: %d\n", num >> 3);  // 값: -2
	return 0;
}

// 값이 마이너스(-)일 경우 CPU가 부호비트를 유지함.(비트열이 오른쪽으로 밀려도 왼쪽에 새로 생성되는 비트들이 1로 채워짐)
```



# 4. 상수와 기본 자료형

## 1) 자료형

데이터를 표현하는 기준. 변수, 상수 모두 자료형에 근거함.

* 정수형 자료형: char, short, int, long, long long
* 실수형 사료형: float, double, long double

| 자료형 |   자료형    |     크기     |                        값의 표현 범위                        |
| :----: | :---------: | :----------: | :----------------------------------------------------------: |
| 정수형 |    char     |   1바이트    |                      -128이상 +127이하                       |
| 정수형 |    short    |   2바이트    |                   -32,768이상 +32,767이하                    |
| 정수형 |     int     |   4바이트    |            -2,147,483,648이상 +2,147,483,647이하             |
| 정수형 |    long     |   4바이트    |              -2,147,483,648이상 +2,147,483,647               |
| 정수형 |  longlong   |   8바이트    | -9,223,372,036,854,775,808이상 +9,223,372,036,854,775,807이하 |
| 실수형 |    float    |   4바이트    |            +-3.4 x 10^-37이상 +-3.4 x 10^+38이하             |
| 실수형 |   double    |   8바이트    |           +-1.7 x 10^-307이상 +- 1.7 x 10^+308이하           |
| 실수형 | long double | 8바이트 이상 |                    double 이상의 표현범위                    |

* 다양한 자료형이 필요한 이유는 메모리를 효율적으로 사용하기 위함.

예) 5천개의 정수들을 저장할 때, short형으로 저장하게 된다면, 5천 x 2바이트 = 1만 바이트가 소모됨. 하지만 int 형으로 표현해 저장한다면 이의 두배가 소모됨.

* <b>sizeof 연산자를 이용하여 자료형의 크기를 확인할 수 있음</b>

```c
#include <stdio.h>

int main(void)
{
    int num = 20;
    int sz1 = sizeof(num);
    int sz2 = sizeof(int);

    printf("%d \n", sz1); // 값: 4
    printf("%d \n", sz2); // 값: 4
    return 0;
}
```

**sizeof는 함수가 아니라 연산자이다.

```c
// 변수, 자료형 크기 비교
#include <stdio.h>

int main(void)
{
	char ch = 9;
	int inum = 1052;
	double dnum = 3.1415;
	printf("변수 ch의 크기: %d\n", sizeof(ch));  // 값: 1
	printf("변수 inum의 크기: %d\n", sizeof(inum));  // 값: 4
	printf("변수 dnum의 크기: %d\n", sizeof(dnum));  // 값: 8

	printf("char의 크기: %d\n", sizeof(char));  // 값: 1
	printf("int의 크기: %d\n", sizeof(int));  // 값: 4
	printf("long의 크기: %d\n", sizeof(long));  // 값: 4
	printf("long long의 크기: %d\n", sizeof(long long));  // 값: 8
	printf("float의 크기: %d\n", sizeof(float));  // 값: 4
	printf("double의 크기: %d\n", sizeof(double));  // 값: 8
	return 0;
}
```



## 2) 자료형의 선택

### a. 정수 자료형의 선택

* 일반적으로 CPU가 처리하기에 가장 적합한 크기의 정수 자료형을 int(4바이트)로 정의함. 따라서 연산의 속도가 다른 자료형의 연산속도에 비해 동일하거다 더 빠름. <u>연산의 횟수가 빈번한 경우에는 저장되는 값의 크기가 작더라도 int형 변수를 선언하는것이 좋음</u>
* 데이터의 양이 많아서 연산속도보다 데이터의 크기를 줄일 때 char 혹은 short 자료형이 유용함.(예: MP3, 음성, 영상 테이터)

```c
#include <stdio.h>

int main(void)
{
	char num1 = 1, num2 = 2, result1 = 0;
	short num3 = 300, num4 = 400, result2 = 0;

	printf("size of num1 & num2: %d, %d \n", sizeof(num1), sizeof(num2));  // 값: 1, 1
	printf("size of num3 & num4: %d, %d \n", sizeof(num3), sizeof(num4));  // 값: 2, 2

	printf("size of char add: %d \n", sizeof(num1 + num2));  // 값: 4
	printf("size of short add: %d \n", sizeof(num3 + num4));  // 값: 4

	result1 = num1 + num2;
	result2 = num3 + num4;

	printf("size of result1 & result2: %d, %d \n", sizeof(result1), sizeof(result2));  // 값: 1, 2
	return 0;
}
```



### b. 실수 자료형의 선택

* 실수 자료형의 선택은 정밀도가 가장 중요함. (float나 double 모두 표현할 수 있는 값의 범위가 크기 때문)
* 오차도 데이터 표현에 사용되는 바이트의 수가 커지면 줄어듦.

| 실수 자료형 | 소수점 이하 정밀도 | 바이트 수 |
| :---------: | :----------------: | :-------: |
|    float    |       6자리        |     4     |
|   double    |       15자리       |     8     |
| long double |       18자리       |    12     |

* 정수 자료형에서 int를 보편적으로 선택하듯이, 실수 자료형에서도 double을 보편적으로 사용함.(float보다 정밀하며 long double보다 바이트 수가 적기 때문)

```c
#include <stdio.h>

int main(void)
{
	double rad;
	double area;
	printf("원의 반지름 입력: ");  // 2.4 입력
	scanf("%lf", &rad);  // double형 데이터를 출력할때는 %f를 사용하지만, double형 데이터를 입력 받을때는 %lf 사용

	area = rad * rad * 3.1415;
	printf("원의 넓이: %f \n", area);  // 값: 18.095040
	return 0;
}
```



### c. unsigned 선언

* 정수 자료형의 이름에 한해 unsigned 선언을 추가하면 0 이상의 값만 표현하는 자료형이 됨(-128 이상 +127 이하였던 표현 범위가 0이상 +255 이하가 됨)
* 정수 자료형 앞에 signed 선언을 추가할 수 있음. 그러나 대부분 자료형이 이미 signed 의미를 포함하고 있어 생략함.(char는 예외일 수 있음)



## 3) 문자의 표현방식과 문자를 위한 자료형

* 숫자를 이용해 문자를 표현하도록 하려면 숫자->문자 연결(mapping)이 되어야 함.
* 아스키(ASCII) 코드로 문자를 표현할 수 있음.

예)

| 아스키 코드 | 아스키 코드 값 |
| ----------- | -------------- |
| A           | 65             |
| B           | 66             |
| C           | 67             |
| '           | 96             |
| ~           | 126            |

```c
#include <stdio.h>

int main(void)
{
	char ch1 = 'A', ch2 = 65;
	int ch3 = 'Z', ch4 = 90;
	
	// 아스키 코드는 문자를 작은 따옴표로 감싸서 표현함
	printf("%c %d \n", ch1, ch1);
	printf("%c %d \n", ch2, ch2);
	printf("%c %d \n", ch3, ch3);
	printf("%c %d \n", ch4, ch4);  // %c는 문자의 형태로 데이터를 출력(입력)하라는 명령
	return 0;
}
```

* <b>char 자료형은 문자를 저장할때 사용된다. 그래서 이름도 char(acter)이다.</b> 연산은 int, 문자는 char를 사용함.

 

## 4) 상수에 대한 이해

상수란, 변경이 불가능한 데이터를 말함.

literal(리터럴) 상수: 변수와 달리 할당된 메모리 공간에 이름이 없다는 뜻.

예)

```c
int main(void)
{
    int num = 30 + 40;  // 30과 40은 상수. 메모리 공간이 없으므로 리터럴 상수이다.
}
```

이때 30과 40은 CPU의 메모리 공간에 상수의 형태로 저장되어 우선 연산 되어진다. 그리고 연산된 70이라는 값이 num 변수에 입력되어진다.

* 정수형 상수의 표현을 위한 접미사(대소문자 구분 없음)

| 접미사 |       자료형       |           사용의 예            |
| :----: | :----------------: | :----------------------------: |
|   U    |    unsigned int    |     unsigned int n = 1025U     |
|   L    |        long        |         long n = 2467L         |
|   UL   |   unsigned long    |    unsigned long n = 2456UL    |
|   LL   |     long long      |      long long n = 5768LL      |
|  ULL   | unsigned long long | unsigned long long n = 8979ULL |

| 접미사 |   자료형    | 사용의 예              |
| :----: | :---------: | ---------------------- |
|   F    |    float    | float f = 3.15F        |
|   L    | long double | long double f = 5.789L |

* 이름을 지니는 심볼릭(Symbolic) 상수: const 키워드를 사용하여 변수 선언 가능.

```c
// 심볼릭 상수의 예
int main(void)
{
	int num = 10;
    const int MAX = 100;  // MAX는 상수. 따라서 값의 변경 불가
    const int PI = 3.1415;  // PI는 상수. 따라서 값의 변경 불가
    const int * ptr = &num;  // 포인터 변수를 대상으로도 const 선언 가능
    int * const ptr2 = &num;  // 포인터 변수 이름 앞에도 위치 가능. (포인터 변수 ptr2는 상수가 됨)
    
    *ptr = 30;  // 컴파일 에러 발생
    num = 20;  // 컴파일 성공
}

// 상수는 변수 선언과 동시에 초기화를 해야함.
```



## 5) 자료형의 변환

char형이 int형으로 바뀌거나 int형이 double형으로 바뀌는 것. 자료형 변환에는 두 종류가 있음.

* 자동 형 변환(묵시적 형 변환)
* 강제 형 변환(명시적 형 변환)



### a. 대입연산의 전달 과정에서 발생하는 자동 형 변환

```c
double num1 = 245; // int형 정수 245를 double형으로 자동 형 변환. 값: 245.000000

int num2 = 3.1415; // double형 실수 3.1415를 int형으로 자동 형 변환. 값: 3
```

*변수 num2와 같이 자료형 변환이 발생하면 소수부의 손실이 발생함.

* 바이트 크기가 큰 정수를 바이트 크기가 작은 정수로 형 변환하는 경우 상위 바이트를 단순히 소멸시킴. 이로 인해 부호가 바뀔 수 있음.

```c
// 만약 int num1을 char ch로 바꾸게 된다면, '상위 바이트의 손실'로 값이 변하게 됨.

int main(void)
{
	int num1 = 129;  // 129의 비트 열은 00000000 00000000 00000000 10000001
	char ch = num1;
	printf("%d", ch); // 10000001 -> 01111111 = -(1+2+4+8+16+32+64) = -127
}
```



### b. 정수의 승격(Integral Promotion)에 의한 자동 형 변환

 CPU가 처리하기에 가장 적합한 자료형으로 변환할 때.

```c
int main(void)
{
    short num1 = 15, num2 = 25;
    short num3 = num1 + num2;  // num1과 num2가 int형으로 형 변환
}
```



### c. 피연산자의 자료형 불일치로 발생하는 자동 형 변환

```c
double num1 = 5.15 + 19;  // 값: 24.15
```

* 이때 5.15가 정수로 변환된다면 소수부 손실이 발생됨. 따라서 19가 실수로 변환됨
* 자동 형 변환은 데이터의 손실을 최소화하는 방향으로 진행

*int -> long -> long lon -> float -> double -> long double



### d. 명시적 형 변환: 강제로 일으키는 형 변환

```c
int main(void)
{
	int num1 = 3, num2 = 4;
	double divResult;
	divResult = (double)num1 / num2;  // 괄호 안의 double을 우선 연산하여 실수로 num1과 num2를 변환함.
	printf("나눗셈 결과: %f \n", divResult);
	return 0;
}
```

*파이썬에서 float(num1 / num2)와 같은 개념.



# 5. 반복문

## 1) while 반복문

```c
int main(void)
{
    int num = 0;

    while(num < 3)
    {
        printf("Hello world! \n");
        num++;
    }
    return 0;
}
```

* while 반복문의 대상이 한 문장이라면 중괄호는 생략 가능

```c
int main(void)
{
    int i = 0;
    while(i < 3)
    	printf("Hello world \n", i++);
	
    /* 혹은
    while(i < 3)
        printf("Hello world \n"), i++;
    */
}
```

* 무한루프

```c
while(1)  // 1은 참을 의미하며 파이썬의 while True: 와 같음
{
    printf("무한루프");
}
```

* while문의 중첩



## 2) do -while문

* 반복조건을 뒤에서부터 검사함
* 반복 조건을 만족하지 못하더라도 반복영역을 최소한 한번 실행하는 구조

```c
#include <stdio.h>

int main(void)
{
	int num = 3;

	do
	{
		printf("Hello world!\n");
		num++;
	} while (num < 3);
}
```



## 3) for 반복문

반복문의 필수 요소인 초기식, 조건식, 증감식이 하나로 묶여 있는 반복문

```c
int main(void)
{
 	int num;
    for(num = 0; num < 3; num++)  // for(초기식; 조건식; 증감식)
        printf("Hello"); // 반복의 대상이 한 줄이므로 중괄호 생략.
}
```

```c
for (int num = 0; num<3; num++) // 바로 for문에서 num 변수 선언도 가능
```

* 초기식: 반복 시작에 앞서 한 번 실행
* 조건식: 매 반복의 시작과 함께 실행. 그 결과를 기반으로 반복 유무를 결정
* 증감식: 매 반복실행 후 마지막에 연산

* 아래와 같이 for문도 조건이 충족될 때까지 반복을 걸 수 있음.

```c
int main(void)
{
	double total = 0.0;
	double input = 0.0;

	int num = 0;

	for (; input >= 0.0; )  // 초기식, 증감식 삭제 가능 => for(num = 0; input >= 0.0; num++)과 같은 문장
	{
		total += input;
		printf("실수 입력(minus to quit): ");
		scanf("%lf", &input);
		num++;
	}
	printf("평균: %f \n", total / (num - 1));
	return 0;
}
```

```c
for( ; ; )  // for 문의 조건식이 비워지면 무조건 '참'으로 인식되어 무한루프 형성
{
    ...
}
```



# 6. 조건적 실행, 흐름의 분기(if)

```c
for(num = 1; num < 100; num++)  // 이렇게 중괄호를 생략할 수 있으나, 중괄호를 사용하는 편이 코드 읽기에 도움이 됨
    if(num % 3 == 0 || num % 4 == 0)
        printf("3 또는 4의 배수: %d \n", num);
```

## 1) if -else문

* 항상 if와 함께 사용되어야 함.
* 모두 if 조건문을 걸어버리면 항상 다른 조건문도 읽어내야해서 효율성 떨어짐. else 문을 넣으면 건너 뛰기 때문에 효율이 좋아짐



## 2) else if문

* 파이썬의 elif문
* if -else 조건이 다양할때 사용.
* else if 조건이 만족되면 마지막 else까지도 건너뜀.



## 3) 조건 연산자: 피 연산자가 세 개인 "삼 항 연산자"

* 조건 ? num1 : num2;  형태로 조건을 걸 수 있음

```c
int main(void)
{
    int num, abs;
    printf("정수 입력: ");
    scanf("%d", &num);
    
    abs = num>0 ? num : num*(-1);  // 앞의 조건이 참이면 num, 거짓이면 num*(-1)을 선택하게됨.
    printf("절대값: %d \n", abs);
    return 0;
}
```



## 4) break, continue

* break: 해당 조건을 만족하면 가장 가까운 반복 조건 탈출.
* continue: 해당 조건을 만족하면 이후는 생략하고 다시 반복문의 조건검사 위치로 이동.



## 5) switch문

* if...else if...else와 유사함. 때로는 대체도 가능
* 하지만 if...else if...else에 비해 사용 영역이 제한적

예 1)

```c
int main(void)
{
    int num;

    printf("1-3 정수 입력: ");
    scanf("%d", &num);

    switch (num)  // 입력하는 인자(num)가 1이면 case 1의 영역 실행.
    {
    case 1:
        printf("1은 one");
        break;  // break가 없다면 case2, case3, default까지 모두 실행되어짐. 반드시 break를 통해 switch 문을 탈출해야함.

    case 2:
        printf("2는 two");
        break;

    case 3:
        printf("3은 three");
        break;

    default:  // default는 생략 가능. else문과 같은 역할
        printf("out of range");   
    }
    return 0;
}
```

예 2)

```c
int main(void)
{
    char sel;
    printf("M 오전, A 오후, E 저녁\n");
    printf("입력: ");
    scanf("%c", &sel);


    switch (sel)
    {
    case 'M':
    case 'm':
        printf("Morning\n");
        break;

    case 'A':
    case 'a':
        printf("Afternoon\n");
        break;

    case 'E':
    case 'e':
        printf("Evening\n");
        break;  // 불필요한 break문
    }
    return 0;
}
```



## 6) goto 문

* 프로그램의 흐름을 원하는 위치로 이동시킬 때 사용
* 프로그램의 흐름을 조정하기 때문에 <u>거의 사용하지 않는 명령문</u>

```c
int main(void)
{
    int sel;
    printf("입력: ");
    scanf("%d", &sel);

    if (sel == 1)
        goto one;
    else
        goto other;
    
one:
    printf("Hi there");
    goto end;

other:
    printf("Hello");
    goto end;

end:
    return 0;
}
```



# 7. 함수 정의 및 선언

## 1) 함수 정의

```c
// 두 정수의 덧셈 함수 정의할 시
int add (int num1, int num2)
{
    int result = num1 + num2;
    return result;
}
```

함수 사용의 예)

```c
#include <stdio.h>

int add(int num1, int num2)
{
	return num1 + num2;
}

int main(void)
{
	int result;
	result = add(3, 4);

	printf("%d", result);
	return 0;
}
```



## 2) 전달인자나 반환 값의 존재 여부에 따른 함수 정의

```c
#include <stdio.h>

int add(int num1, int num2)  // 인자전달 O, 반환 값 O
{
	return num1 + num2;
}

void ShowAddResult(int num)  // 인자전달 O, 반환 값 X
{
	printf("덧셈결과 출력: %d \n", num);
}

int ReadNum(void)  // 인자전달 X, 반환 값 O
{
	int num;
	scanf("%d", &num);
	return num;
}

void HowToUseThisProg(void)  // 인자전달 X, 반환 값 X
{
	printf("두 개의 정수를 입력하시면 덧셈결과가 출력됩니다. \n");
	printf("정수를 입력하세요: ");
}

int main(void)
{
	int result, num1, num2;
	HowToUseThisProg();

	num1 = ReadNum();
	num2 = ReadNum();

	result = add(num1, num2);
	ShowAddResult(result);
	return 0;
}
```



* 반환형이 void로 선언되어있는 함수에서도 <b>return;</b> 을 사용할 수 있음.(값의 반환 없이 그냥 함수를 빠져나오는 의미)

* 다른 함수가 main함수보다 뒤에 오더라도 함수 선언을 우선 하여 순서를 바꿀 수 있음

```c
int function(int n);  // 함수 우선 선언.

int main(void)  // main 함수
{
    int num = 2;
    function(num);
    return 0;
}

int function(int n)  // 우선 선언 되었던 function 함수의 정의
{
    n++;
    return 0;
}
```

* 함수의 선언은 두가지 방법으로 할 수 있음

```c
int add(int num1, int num2);
int add(int, int);
```



## 3) 변수의 존재 기간

### a. 전역변수

* 프로그램의 실행부터 종료까지 메모리 공간에 할당되는 변수
* 프로그램 전체 영역 어디서든 접근이 가능
* 전역변수와 동일한 지역변수가 선언되면 전역변수가 가리워지고 지역변수로의 접근이 이뤄짐
* 가급적 전역변수와 지역변수는 각각 다른 이름으로 정해야 혼란을 피할 수 있음

```c
#include <stdio.h>

void add(int val);
int num;  // 전역변수는 기본 0으로 초기화

int main(void)
{
	printf("num: %d \n", num);  // 값: 0
	add(3);
	printf("num: %d \n", num);  // 값: 3
	num++;
	printf("num: %d \n", num);  // 값: 4
	return 0;
}

void add(int val)
{
	num += val;
}
```



### b. 지역변수(local variable)

* 지역변수를 자동변수라고도 부름. 자동으로 소멸되기 때문
* 지역: 중괄호에 의해 형성되는 영역.
* 중괄호 내에 형성되는 변수는 모두 지역변수. 따라서 지역이 다르면 변수 이름이 같아도 문제 없음.
* 반복문 및 조건문에도 지역변수 선언 가능

```c
int main(void)
{
    int cnt;
    for(cnt = 0; cnt < 3; cnt++)
    {
        int num = 0;
        num++;  // 중괄호 안의 지역변수
        printf("%d번째 반복, 지역변수 num은 %d \n", cnt+1, num);
    }
    
    if(cnt = 3)
    {
        int num = 7;
        num++;  // 중괄호 안의 지역변수
        printf("if 문 내에 존재하는 지역변수 num은 %d, \n", num);
    }
    
    return 0;
}
```

* 함수를 정의할 때 선언하는 매개변수 또한 지역변수의 일종. 선언된 함수 내에서만 접근이 가능하며, 선언된 함수가 반환을 하면 지역변수와 마찬가지로 소멸



### c. static 변수

* 지역변수 및 전역변수에 모두 static 선언 추가 가능
* 선언된 함수 내에서만 접근 가능(지역변수 특성)
* static 변수를 선언하면 딱 1회 초기화되고 프로그램 종료까지 메모리 공간에 존재 (전역변수 특성) 
* 전역변수보다 접근성이 낮아져 안정적임



### d. register 변수

* CPU 내 <b>레지스터</b> 메모리 공간에 저장될 확률을 높임.
* register 변수 선언을 해도 컴파일러에 따라 CPU 레지스터 메모리 공간 저장 여부를 컴퓨터가 자체적으로 판단함.

```c
int function(void)
{
    register int num = 3;
    ...
}
```



## 4) 재귀함수

```c
#include <stdio.h>
  // 재귀함수 예
void recursive(int num)
{
    if (num <= 0)  // 탈출 조건
        return;  // 재귀의 탈출
    printf("Recursive call %d \n", num);
    recursive(num-1);
}

int main(void)
{
    recursive(3);
    return 0;
}
```

```c
#include <stdio.h>
  // factorial 값 구하는 재귀함수
int factorial(int n)
{
	if (n == 0)
		return 1;
	else
		return n * factorial(n - 1);
}

int main(void)
{
	int fac;
	printf("factorial을 구할 정수 입력: ");
	scanf("%d", &fac);
	
	printf("%d! = %d", fac, factorial(fac));
	return 0;
```



# 8. 배열

* 한번에 많은 변수를 선언할 수 있음

## 1) 1차원 배열

* 이름, 자료형, 길이정보가 필요. 예) int oneDimArr[4]
* 배열 선언과 동시에 초기화 가능

```c
int arr1[5] = {1, 2, 3, 4, 5}; // 순차적으로 1, 2, 3, 4, 5로 초기화

// 혹은 아래와 같이 리스트 길이 생략 가능
int arr2[] = {1, 2, 3, 4, 5, 6, 7};

// 
int arr3[5] = {1, 2}; // 3, 4, 5번째 인덱스는 0으로 채워짐
```



* 리스트 길이 확인

```c
int main(void)
{
	int arr1[5] = { 1, 2 };

	printf("%d", sizeof(arr1) / sizeof(int));	
	return 0;	
}

// 혹은

int main(void)
{
	int arr1[5] = { 1, 2 };
	int ar1Len, i;

	ar1Len = sizeof(arr1) / sizeof(int);

	for (i = 0; i < ar1Len; i++)
		printf("%d ", arr1[i]);

	return 0;
}
```



## 2) 문자열 배열


* 문자열 리스트 저장

```c
char str[14] = "Good morning!";  // 이 리스트에는 끝에 \0(null)이라는 특수문자(escape sequence)가 자동 삽입됨
// null 문자의 아스키 코드 값은 0임.

srt[12] = ?  // 인덱스 변환도 가능
```

* 문자열 입력받기

```c
int main(void)
{
	char str[50];
	int idx = 0;
	
	printf("문자열 입력: ");
	scanf("%s", str);  // 문자열 입력은 &문자 제외
	printf("입력 받은 문자열: %s \n", str);  // 입력받은 모든 문자열의 끝에는 null(\0) 문자가 자동으로 삽입됨

	return 0;
}
```



# 9. 포인터



## 1) 포인터변수

* 메모리의 주소 값을 저장하기 위한 변수

예) 세 변수 char 'A', char 'B', int 7(각각 1, 1, 4 바이트)는 메모리 공간에 할당됨(0x12ff74, ox12ff75, ...ox12ff79 ). 메모리 주소값 또한 정수이므로 저장이 가능함. 이의 저장을 위해 마련된 변수가 포인터 변수

```c
int main(void)
{
    int num = 7;
    int * pnum = &num;  // 포인터 변수 pnum 선언 및 num의 주소 값을 포인터 변수 pnum에 저장
}
```

* 포인터 형(type) 별 변수 선언

```c
int * pnum1;  // int형 포인터 변수 선언
double * pnum2;  // double형 포인터 변수 선언
unsigned int * pnum3;  // unsigned int형 포인터 변수 선언
```



## 2) &연산자

* 주소 연산자. 뒤에 있는 변수의 주소값을 불러옴
* 연산자의 피 연산자는 변수여야함.(상수는 피연산자가 될 수 없음

```c
int main(void)
{
    int a = 10;
    printf("%p", &a);  // 값: 00EFFEC4. %p는 포인터 주소값을 출력하는 서식문자
    return 0;
}
```



## 3) *연산자

* 포인터 변수 주소값에 있는 데이터
* 포인터가 가리키는 메모리 공간에 접근할 때 사용.

```c
int main(void)
{
    int num = 10;
    int * pnum = &num;
    *pnum = 20;
    printf("%d", *pnum);  // pnum이 가리키는 변수(num)를 부호 있는 정수로 출력. 값: 20
}
```



## 4) Null 포인터

* 포인터 초기화에 아무 값을 주지 않는 것

```c
int main(void)
{
    int * ptr1 = 0;  // Null과 같은 의미
    int * ptr2 = NULL;  // Null은 사실상 0을 의미
}
```



## 5) 포인터와 배열의 관계

* 배열의 이름은 포인터임. 아래 실행 결과를 보면 int형 배열요소간 주소 값의 차는 4바이트인것을 알 수 있음.

```c
int main(void)

{
	int arr[3] = { 0, 1, 2 };
	printf("배열의 이름 %p \n", arr);  // 00A6F764 (배열의 이름은 배열의 시작 주소 값을 의미)
	printf("첫 번째 요소: %p \n", &arr[0]);  // 00A6F764
	printf("두 번째 요소: %p \n", &arr[1]);  // 00A6F768
	printf("세 번째 요소: %p \n", &arr[2]);  // 00A6F76C

	return 0;
}
```



## 6) 포인터 연산

* 포인터를 대상으로 n의 크기만큼 값을 증가 및 감소 시 n x sizeof(타입)의 크기만큼 주소 증감소

```c
int main(void)

{
	int arr[3] = { 11, 22, 33 };
	int* ptr = arr;
	printf("%d %d %d \n", *ptr, *(ptr + 1), *(ptr + 2));  // 값: 11 22 33. 4바이트씩 증가하였기 때문에 1차원 배열된 다음 인덱스 값이 출력됨
	
	printf("%d ", *ptr); ptr++;  // 11
	printf("%d ", *ptr); ptr++;  // 22
	printf("%d ", *ptr); ptr--;  // 33
	printf("%d ", *ptr); ptr--;  // 22
	printf("%d ", *ptr); printf("\n"); // 11
    
    // 아래 네 출력 모두 값이 11 22 33으로 똑같음
    printf("%d %d %d \n", *(ptr + 0), *(ptr + 1), *(ptr + 2));
    printf("%d %d %d \n", ptr[0], ptr[1], ptr[2]);
    printf("%d %d %d \n", *(arr + 0), *(arr + 1), *(arr + 2));
    printf("%d %d %d \n", arr[0], arr[1], arr[2]);
    
	return 0;
}
```

* 위의 결과로 볼때 <b>arr[i] == *(arr + i)</b> 임을 알 수 있음



## 7) 상수 형태의 문자열을 가리키는 포인터

```c
int main(void)
{
	char str1[] = "My string";  // 문자열
	char* str2 = "Your string";  // 상수 형태의 문자열
	printf("%s %s \n", str1, str2);  // 값: My string Your string

	str2 = "Our String";  // str2는 상수형태의 문자열 포인터이기 때문에 문자 하나하나 내용 변경이 불가능
	printf("%s %s \n", str1, str2);  // 값: My string Our String
	return 0;
}
```



## 8) 포인터 배열

* 포인터 변수로 이뤄졌으며 주소 값의 저장이 가능한 배열

```c
int * arr1[20];  // 길이가 20인 int형 포인터 배열
double * arr2[30];  // 길이가 30인 double형 포인터 배열
```

예)

```c
int main(void)
{
	int num1 = 10, num2 = 20, num3 = 30;
	int* arr[3] = { &num1, &num2, &num3 };
	
	printf("%d \n", *arr[0]);
	printf("%d \n", *arr[1]);
	printf("%d \n", *arr[2]);
	return 0;
}
```



## 9) 포인터 문자열 배열

```c
int main(void)
{
	char* strarr[3] = { "Simple", "String", "Array" };
	printf("%s \n", strarr[0]);
	printf("%s \n", strarr[1]);
	printf("%s \n", strarr[2]);
	return 0;
}
```



# 10. 포인터와 함수

* 함수의 매개변수는 배열의 형태로 전달받을 수 없음. 그래서 배열의 주소값을 인자로 전달하여야 함.

```c
void ShowArayElem(int* param, int len)  // 배열 파라미터를 포인터 배열로 전달
{
	int i;
	for (i = 0; i < len; i++)
		printf("%d ", param[i]);
	printf("\n");
}

int main(void)
{
	int arr1[3] = { 1, 2, 3 };
	int arr2[5] = { 4, 5, 6, 7, 8 };
	ShowArayElem(arr1, sizeof(arr1) / sizeof(int));
	ShowArayElem(arr2, sizeof(arr2) / sizeof(int));
	return 0;
}
```

* 배열의 값의 변경 또한 가능

```c
void ShowArayElem(int* param, int len)  // int * param 대신 int param[] 선언 가능. 단, 매개변수일때만 가능
{
	int i;
	for (i = 0; i < len; i++)
		printf("%d ", param[i]);
	printf("\n");
}

void AddArayElem(int* param, int len, int add)
{
	int i;
	for (i = 0; i < len; i++)
		param[i] += add;
}

int main(void)
{
	int arr[3] = { 1, 2, 3 };
	AddArayElem(arr, sizeof(arr) / sizeof(int), 1);  // arr 인덱스 값을 각각 1씩 증가시킴
	ShowArayElem(arr, sizeof(arr) / sizeof(int));  // 값: 2 3 4

	AddArayElem(arr, sizeof(arr) / sizeof(int), 2);  // arr 인덱스 값을 각각 2씩 증가시킴
	ShowArayElem(arr, sizeof(arr) / sizeof(int));  // 값: 4 5 6

	AddArayElem(arr, sizeof(arr) / sizeof(int), 3);  // arr 인덱스 값을 각각 3씩 증가시킴
	ShowArayElem(arr, sizeof(arr) / sizeof(int));  // 7 8 9
    return 0;
}
```



## 1) Call-by-value & Call-by-reference

* 함수의 호출 방식을 의미

### a. Call-by-value

* 함수를 호출할 때 단순히 값을 전달하는 형태의 함수호출. 예) 대부분의 함수가 Call-by-value.

### b. Call-by-reference

* 메모리의 접근에 사용되는 주소 값을 전달하는 형태의 함수호출. 예) void ShowArayElem(int * param, int len)과 같은 함수

```c
void Swap(int* ptr1, int* ptr2)
{
	int temp = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = temp;
}

int main(void)
{
	int num1 = 10;
	int num2 = 20;
	printf("num1 num2: %d %d \n", num1, num2);

	Swap(&num1, &num2);  // num1과 num2의 주소값에 접근하여 바꾸므로 num1과 num2의 값이 Swap 함수로 인해 바뀜
	printf("num1 num2: %d %d \n", num1, num2);
	return 0;
}
```



