[toc]



참고1: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=gusrn94o&logNo=221354431381

참고2: https://tbvjrornfl.tistory.com/80

# 1. 환경

* VMware
* Ubuntu 20.04
* Ubuntu 안에 VMware Windows 7 32bit 설치 (가상 머신 안의 가상머신에서 쿠쿠 샌드박스 구현)
* cuckoo 2.0.7

# 2. 설치

1) Ubuntu 20.04 iso 다운로드
2) VMware에 Ubuntu 설치
3) python 설치

```
sudo apt-get install python python3-pip python-dev libffi-dev libssl-dev

sudo apt-get install python3-virtualenv python-setuptools python-sqlalchemy python-jinja2 python-magic python3-pymongo python3-bottle libpcre3 libpcre3-dev

sudo apt-get install libjpeg-dev zlib1g-dev swig
```

4. 몽고DB 설치

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

sudo apt update
sudo apt install -y mongodb

sudo service mongodb start
sudo systemctl enable mongodb
```

5. tcpdump 설치

```
sudo apt-get install tcpdump apparmor-utils
sudo aa-disable /usr/sbin/tcpdump
sudo apt-get install tcpdump
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
sudo getcap /usr/sbin/tcpdump
```

6. volatility 설치

```
sudo apt-get install git
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility/
sudo python setup.py install
sudo apt-get install yara
```

7. m2crypto 설치

```
sudo pip install m2crypto
```

8. subversion 설치
9. cuckoo 샌드박스 설치

```
# python2로만 다운 가능
sudo apt install python2
sudo curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py

sudo pip2 install cuckoo
sudo pip2 install -U cuckoo
sudo pip2 install distorm3
cuckoo -d
cuckoo community
```

10. virtualBox 설치

```
sudo apt-get install virtualbox
sudo apt-get install net-tools
```

