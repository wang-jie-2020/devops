## Dockerfile
FROM centos:7

LABEL maintainer "wangjie"

ENV NGINX_VERSION 1.23.3
ENV BASE_PATH /app

#get all the dependences and nginx
RUN yum install -y git gcc make wget pcre pcre-devel openssl openssl-devel \
  && rm -rf /var/cache/yum/*

#create the dirs to store the files downloaded from internet
RUN mkdir ${BASE_PATH} 
WORKDIR ${BASE_PATH}

# comile nginx
RUN wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
  && tar -zxf nginx-${NGINX_VERSION}.tar.gz \
  && cd nginx-${NGINX_VERSION} \
  && ./configure \
  && make \
  && make install \
  && ln -s /usr/local/nginx/sbin/nginx /usr/bin/ \
  && rm -rf ${BASE_PATH}/nginx-* 

WORKDIR ${BASE_PATH}

#make the entrypoint.sh executable
COPY start.sh /usr/bin/
RUN chmod a+x /usr/bin/start.sh

ENTRYPOINT ["/usr/bin/start.sh"]