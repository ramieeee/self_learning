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

# 3. 메일 서버 구축

* 참고자료

1. https://www.2cpu.co.kr/lec/2438
2. https://y0c.github.io/2018/09/28/centos7-mail-server/
3. https://whitewing4139.tistory.com/147

## 1) postfix 설치

```
yum -y install postfix
```



## 2) SSL 인증서 세팅

```
mkdir /etc/postfix/ssl
cd /etc/postfix/ssl
openssl req -x509 -nodes -newkey rsa:2048 -keyout server.key -out server.crt -nodes -days 365
```

## 3) postfix 설정

```
vi /etc/postfix/main.cf

# 메일 호스트명 
   myhostname = mail.example.com    // 사용하려는 이메일 호스트 입력

# 도메인 명
   mydomain = example.com            // 사용하려는 이메일 도메인 입력

# 서버에서 메일 발송시 나타나는 도메인 (From 도메인 설정)
   myorigin = $myhostname
   
home_mailbox = mail/
mynetworks = 127.0.0.0/8
inet_interfaces = all
inet_protocols = all
smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
smtpd_sasl_local_domain =
smtpd_sasl_security_options = noanonymous
broken_sasl_auth_clients = yes
smtpd_sasl_auth_enable = yes
smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination
smtp_tls_security_level = may
smtpd_tls_security_level = may
smtp_tls_note_starttls_offer = yes
smtpd_tls_loglevel = 1
smtpd_tls_key_file = /etc/postfix/ssl/server.key
smtpd_tls_cert_file = /etc/postfix/ssl/server.crt
smtpd_tls_received_header = yes
smtpd_tls_session_cache_timeout = 3600s
tls_random_source = dev:/dev/urandom
```

```
vi /etc/postfix/master.cf

smtp      inet  n       -       n       -       -       smtpd
#smtp      inet  n       -       n       -       1       postscreen
#smtpd     pass  -       -       n       -       -       smtpd
#dnsblog   unix  -       -       n       -       0       dnsblog
#tlsproxy  unix  -       -       n       -       0       tlsproxy
submission inet n       -       n       -       -       smtpd
  -o syslog_name=postfix/submission
  -o smtpd_tls_security_level=encrypt
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
  -o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
  -o milter_macro_daemon_name=ORIGINATING
smtps     inet  n       -       n       -       -       smtpd
  -o syslog_name=postfix/smtps
  -o smtpd_tls_wrappermode=yes
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
  -o smtpd_recipient_restrictions=permit_sasl_authenticated,reject
  -o milter_macro_daemon_name=ORIGINATING
```

## 4) dovecot 설치

```
yum -y install dovecot

vi /etc/dovecot/conf.d/10-master.conf

# Postfix smtp-auth
unix_listener /var/spool/postfix/private/auth {
	mode = 0660
	user = postfix
	group = postfix
}
```

```
# auth 설정 수정
vi /etc/dovecot/conf.d/10-auth.conf

auth_mechanisms = plain login

# 이 설정은 안해주면 계정을 입력할때 Test@example.com 이 아니라 Test로 입력해야 로그인이 됨
auth_username_format = %Ln

```

```
# home_mailbox와 맞춰줘야 수신이 제대로 동작함
vi /etc/dovecot/conf.d/10-mail.conf

mail_location = maildir:~/mail
```

## 5) POP3 설정

```
vi /etc/dovecot/conf.d/20-pop3.conf

# 주석 해제
pop3_uidl_format = %08Xu%08Xv
```

## 6) 서비스 시작 및 방화벽 설정

```
systemctl restart postfix
systemctl enable postfix
systemctl restart dovecot
systemctl enable dovecot

firewall-cmd --permanent --add-service=smtp
firewall-cmd --permanent --add-port=587/tcp
firewall-cmd --permanent --add-port=465/tcp
firewall-cmd --permanent --add-port=110/tcp
firewall-cmd --permanent --add-service=pop3s
firewall-cmd --permanent --add-port=143/tcp
firewall-cmd --permanent --add-service=imaps
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
```

## 7) 메일 보내기 테스트

```
mail -s "제목" user@example.com <<< '본문 작성'
```



## 3) SELinux 비활성화

## 4) 호스트네임 설정

* 프로젝트 서버: hostnamectl set-hostname mail.project.com
* 스팸 서버: hostnamectl set-hostname mail.test.com

