## Dockerfile
FROM centos:7

LABEL maintainer "wangjie"

ENV NGINX_VERSION 1.23.3

#get all the dependences and nginx
RUN yum install -y git gcc gcc-c++ make wget pcre pcre-devel openssl openssl-devel zlib-devel rpm-build rpmdevtools \
	&& rm -rf /var/cache/yum/* 
	
RUN rpmdev-setuptree \
	&& cd /root/rpmbuild/SOURCES \
	&& wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz 
	
COPY nginx.spec /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild
RUN rpmbuild -bb SPECS/nginx.spec

WORKDIR /root/rpmbuild/RPMS/x86_64
RUN rpm -ivh nginx-${NGINX_VERSION}-el7.x86_64.rpm \
	&& ln -s /usr/local/nginx/sbin/nginx /usr/bin/ 

COPY start.sh /usr/bin/
RUN chmod a+x /usr/bin/start.sh

ENTRYPOINT ["/usr/bin/start.sh"]