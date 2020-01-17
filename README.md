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
