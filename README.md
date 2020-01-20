# allinthemind_webservice

## Create a Dockerfile
```bash
cat <<'EOF'> Dockerfile
FROM ubuntu:18.04

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf \
  && apt update -y \
  && apt install -y python-pip apache2 libapache2-mod-wsgi python-dev git \
  && apt clean

WORKDIR /var/www/

RUN  echo "nameserver 8.8.8.8" > /etc/resolv.conf \
  && git clone https://github.com/victorcmsantos/allinthemind_webservice.git html6

RUN ln -nf /var/www/html6/06-allinthemind.conf /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod wsgi

RUN chown www-data. html6 -R

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf \
  && pip install -r html6/requirements.txt

RUN sed -i 's/Listen 80/#Listen 80/' /etc/apache2/ports.conf

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

EXPOSE 86

CMD /usr/sbin/apache2ctl -D FOREGROUND
EOF
```

## Build a new image
```bash
sudo docker build -t allinthemind03 .
```

## Run this new image
```bash
sudo docker run -d -p 80:86  allinthemind03
```

## How to create a simple user:
```bash
curl -s -H "Content-Type: application/json" -X POST   -d '{"username":"gleyss","password":"12","email":"gleyss@teste.com"}' http://allinthemind-webservice.victorsantos.net/register/student
```

## How to get the Token, exemple is a "admin role":
```bash
curl -s -H "Content-Type: application/json" -X POST   -d '{"username":"vivi@teste.com","password":"12"}' http://allinthemind-webservice.victorsantos.net/login
```

## How to create a Tutor user, as admin role:
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlYjAyMjczYS00ZDQ5LTRhYjEtYjg2YS0wNmJjMDYyMWJkMTQiLCJleHAiOjE1NzkxNzkyNjEsImZyZXNoIjpmYWxzZSwiaWF0IjoxNTc5MTc4MzYxLCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNTc5MTc4MzYxLCJpZGVudGl0eSI6InZpdmlAdGVzdGUuY29tIn0.0yS-Mrc2Ly_-s8fW30AFMghHpIrcOjAgpdnZJX--S0I" -H "Content-Type: application/json" -X POST   -d '{"username":"eliane","password":"12","email":"eliane@teste.com"}' http://allinthemind-webservice.victorsantos.net/register/tutor
```

## How to List all users, as admin role:
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkZTY3ZjY5ZC1lZWY1LTRkYTgtODViYy0yY2E5MGM5NDJkNGUiLCJleHAiOjE1NzkyNTIyMjksImZyZXNoIjpmYWxzZSwiaWF0IjoxNTc5MjUxMzI5LCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNTc5MjUxMzI5LCJpZGVudGl0eSI6InZpdmlAdGVzdGUuY29tIn0.Wa0hXszkUKmNTE4XCBvsibYPurGZ9Syr2zkphBOIJ_E"  http://allinthemind-webservice.victorsantos.net/admin/users
```

## How to add a new class, as tutor role:
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGFlMDVmZi02ZTNiLTQ5ZDgtOWQ5Yy05NGIwNjQ3MGRmNWMiLCJleHAiOjE1Nzk1MjA0NTEsImZyZXNoIjpmYWxzZSwiaWF0IjoxNTc5NTE5NTUxLCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNTc5NTE5NTUxLCJpZGVudGl0eSI6ImVsaWFuZUB0ZXN0ZS5jb20ifQ.j_Pwu5n4ux6Va5P_QIEktEuzZ3MosShJt-xFqXEtZB8" -H "Content-Type: application/json" -X POST   -d '{"classname":"ElianeClasseHTML", "course":"html"}' http://allinthemind-webservice.victorsantos.net/class/add
```

## How to get all own classes, as tutor role:


