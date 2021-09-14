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
* postfix
* dovecot

## 2) 스팸 메일 차단 기술

- RBM 기술? 자연어 처리?

## 3) 결론

* 어떤점이 현 기술에 문제가 있는지 파악하고 대안 기법 확인 필요

# 2. 학습 파라미터

* 인간이 어떤 부분에서 메일을 스팸으로 분류하는지 확인해야함
* 메일 헤더, 내용, 메일이 어떻게 작동하는지 공부

# 3. 네임서버 구축

* mail.project.com(스팸 피해자) = 192.168.100.142
* mail.test.com(스팸 발신자) = 192.168.100.140
* DNS = 192.168.100.143

```
yum -y install bind bind-chroot
```

```
vim /etc/hosts

# project.com 서버
192.168.100.142 mail.project.com

# test.com 서버
192.168.100.140 mail.test.com
```

```
vim /etc/sysconfig/network

# project.com 서버
HOSTNAME=192.168.100.142

# test.com 서버
HOSTNAME=192.168.100.140
```

```
# DNS
vim /etc/named.conf

options {

# 나의 어떤 IP와 포트로 청취할 것인가의 옵션
listen-on port 53 { any; };

# 위 옵션과 같이 IPv6 의 IP 와 포트를 청취할 것인지 설정
listen-on-v6 port 53 { none; };

# 어떤 IP한테서의 쿼리를 허용할 것인지 설정
allow-query { any; };
};

dnssec-validation no;

# zone 설정
zone "project.com" IN {
        type master;
        file "project.com.db";
        allow-update { none; };
};

zone "test.com" IN {
        type master;
        file "test.com.db";
        allow-update { none; };
};
```

```
vi /var/named/project.com.db

$TTL    3H
@       SOA     @       root.   ( 2  1D  1H  1W  1H )
        IN      NS      @
        IN      A       192.168.100.142
        IN      MX      10      mail.project.com.

mail    IN      A       192.168.100.142
```

```
vi /var/named/test.com.db

$TTL    3H
@       SOA     @       root.   ( 2  1D  1H  1W  1H )
        IN      NS      @
        IN      A       192.168.100.140
        IN      MX      10      mail.test.com.

mail    IN      A       192.168.100.140
```

```
# 적용이 잘 되었는지 확인
named-checkconf
named-checkzone project.com project.com.db
named-checkzone test.com test.com.db
```

```
# 서비스 시작
systemctl restart named
systemctl enable named
```

```
# 방화벽 내리기
systemctl stop firewalld
systemctl disable firewalld
```

```
# nameserver 작동 확인
nslookup
> server 192.168.100.143
Default server: 192.168.100.143
Address: 192.168.100.143#53
> mail.project.com
Server:		192.168.100.143
Address:	192.168.100.143#53

Name:	mail.project.com
Address: 192.168.100.142
> mail.test.com
Server:		192.168.100.143
Address:	192.168.100.143#53

Name:	mail.test.com
Address: 192.168.100.140
```

```
# 각 서버에서 DNS 설정

# project.com, test.com 서버
nmcli con mod ens33 ipv4.dns 192.168.100.143
systemctl restart NetworkManager
reboot
```



# 4. 메일 서버 구축

* 참고자료

4. https://erider.co.kr/127 <- 메일 명령어 관련 블로그
5. https://cghsecurity.tistory.com/15?category=907152 <- 네임서버 구축
3. https://www.youtube.com/watch?v=iFMnYUvBqEA&list=PLVsNizTWUw7EJ9z-LW3lv3VC-6HI9I3hN&index=52 <- sendmail 서버 구축

## 1) sendmail 구축

```
yum -y install sendmail-cf dovecot
```

```
vim /etc/mail/sendmail.cf

# project.com 서버
85 Cwproject.com
264 O DaemonPortOptions=Port=smtp, Name=MTA

# test.com 서버
85 Cwtest.com
264 O DaemonPortOptions=Port=smtp, Name=MTA
```

```
# RELAY 메일 전달하는 기능 추가
vim /etc/mail/access

# project.com, test.com 서버
project.com     RELAY
test.com        RELAY
192.168.100     RELAY

# 두 서버 모두에서 설정한 내용 적용
makemap hash /etc/mail/access < /etc/mail/access
```

```
# 두 서버 모두
vim /etc/dovecot/conf.d/10-ssl.conf
8: ssl = yes
```

```
vim /etc/dovecot/conf.d/10-mail.conf

# 주석 해제
25 mail_location = mbox:~/mail:INBOX=/var/mail/%u
121 mail_access_groups = mail
166 lock_method = fcntl
```

```
systemctl restart sendmail
systemctl enable sendmail
```

# 5. Spamassassin 설치

```
yum -y install spamassassin
```

```
# Mailbox 로 전송되기 전에 spamassassin 이 처리하도록 설정
vim /etc/procmailrc

# 아래 내용 추가
INCLUDERC=/etc/mail/spamassassin/spamassassin-default.rc
```

```
# spamassassin 설정

cd /etc/mail/spamassassin
vim local.cf

# 새 줄 추가
required_score 5
```

```
# spamassassin이 기본적으로 root 계정으로 실행되기때문에 실행 그룹 추가

groupadd -g 5555 spamd
useradd -u 5555 -g spamd -s /bin/false -d /var/log/spamassassin spamd
chown spamd:spamd /var/log/spamassassin
```

```
systemctl restart spamassassin
systemctl enable spamassassin
```

