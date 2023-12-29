## Dockerfile
FROM centos:7

LABEL maintainer "wangjie"

ENV NGINX_VERSION 1.23.3
ENV LIBFASTCOMMON_VERSION V1.0.66
ENV LIBSERVERFRAME_VERSION V1.1.25
ENV FASTDFS_NGINX_MODULE_VERSION V1.23
ENV FASTDFS_VERSION V6.9.4
ENV LIBFASTCOMMON_PACKAGE_VERSION 1.0.66
ENV LIBSERVERFRAME_PACKAGE_VERSION 1.1.25
ENV FASTDFS_PACKAGE_VERSION 6.9.4
ENV BASE_PATH /app

#get all the dependences and nginx
RUN yum install -y git gcc gcc-c++ make wget pcre pcre-devel openssl openssl-devel zlib-devel rpm-build rpmdevtools \
	&& rm -rf /var/cache/yum/* 

#create the dirs to store the files downloaded from internet
RUN mkdir ${BASE_PATH} \
	&& mkdir -p ${BASE_PATH}/fastdfs-nginx-module \
	&& mkdir -p ${BASE_PATH}/fastdfs \
	&& mkdir -p ${BASE_PATH}/libfastcommon \
	&& mkdir -p ${BASE_PATH}/libserverframe 

WORKDIR ${BASE_PATH}

## compile the libfastcommon
RUN git clone -b $LIBFASTCOMMON_VERSION https://github.com/happyfish100/libfastcommon.git libfastcommon \
  && cd libfastcommon \
  && ./make.sh \
  && ./make.sh install \
  && rm -rf ${BASE_PATH}/libfastcommon

## compile the libserverframe
RUN git clone -b $LIBSERVERFRAME_VERSION https://github.com/happyfish100/libserverframe.git libserverframe \
  && cd libserverframe \
  && ./make.sh \
  && ./make.sh install \
  && rm -rf ${BASE_PATH}/libserverframe

## compile the fastdfs
RUN git clone -b $FASTDFS_VERSION https://github.com/happyfish100/fastdfs.git fastdfs \
  && cd fastdfs \
  && ./make.sh \
  && ./make.sh install \
  && rm -rf ${BASE_PATH}/fastdfs

# comile nginx
RUN git clone -b $FASTDFS_NGINX_MODULE_VERSION https://github.com/happyfish100/fastdfs-nginx-module.git fastdfs-nginx-module 

RUN rpmdev-setuptree \
	&& cd /root/rpmbuild/SOURCES \
	&& wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz 
	
COPY nginx.spec /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild
RUN rpmbuild -bb SPECS/nginx.spec

## official rpm
# RUN rpm -ivh http://www.fastken.com/yumrepo/el7/noarch/FastOSrepo-1.0.0-1.el7.centos.noarch.rpm \
# && yum -y install fastdfs-server-${FASTDFS_PACKAGE_VERSION}-1.el7.x86_64 \
	# fastdfs-tool-${FASTDFS_PACKAGE_VERSION}-1.el7.x86_64 \
	# fastdfs-config-${FASTDFS_PACKAGE_VERSION}-1.el7.x86_64
	
# WORKDIR /root/rpmbuild/RPMS/x86_64
# RUN rpm -ivh nginx-${NGINX_VERSION}-el7.x86_64.rpm \
	# && ln -s /usr/local/nginx/sbin/nginx /usr/bin/ 

# COPY start.sh /usr/bin/
# RUN chmod a+x /usr/bin/start.sh

# ENTRYPOINT ["/usr/bin/start.sh"]