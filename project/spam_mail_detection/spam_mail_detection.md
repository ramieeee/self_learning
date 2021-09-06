**스팸메일 필터링**

[toc]

# 1. 배경 연구

## 1) 메일 서버 구축

1. DNS 서버
2. MX 레코드
3. Vmware 로컬 메일 서버 구축 공부 (postfix)

### a. 환경

* VMware
* CentOS7 64bit
* Windows 10 64bit
* 

## 2) 스팸 메일 차단 기술

- RBM 기술? 자연어 처리?

## 3) 결론

* 어떤점이 현 기술에 문제가 있는지 파악하고 대안 기법 확인

# 2. 학습 파라미터

* 인간이 어떤 부분에서 메일을 스팸으로 분류하는지 확인해야함

* 메일 헤더, 내용, 메일이 어떻게 작동하는지 공부

# 3. 메일 서버 구축

* 참고자료

1. https://www.2cpu.co.kr/lec/2438

2. 

## 1) postfix 설치

* yum -y update

## 2) letsencrypt 설치

* yum install letsencrypt
* yum letsencrypt certonly --agree-tos --email "이메일주소" -d "도메인주소"

## 3) SELinux 비활성화

[root@localhost ~]# **sed -i 's/^SELINUX=.\*/SELINUX=disabled/g' /etc/selinux/config**

[root@localhost ~]# **cat /etc/selinux/config | grep disabled** **(변경 확인)**
\#   disabled - No SELinux policy is loaded.
SELINUX=**disabled**

## 4) 호스트네임 설정

hostnamectl set-hostname mail.eztest.com
