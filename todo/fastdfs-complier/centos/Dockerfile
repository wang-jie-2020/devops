## Dockerfile
FROM centos:7

LABEL maintainer "wangjie"

## yum
RUN curl -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo \
	&& yum makecache 

#get all the dependences
RUN yum install -y git gcc gcc-c++ make wget pcre pcre-devel openssl openssl-devel zlib-devel rpm-build rpmdevtools \
	&& rm -rf /var/cache/yum/* 