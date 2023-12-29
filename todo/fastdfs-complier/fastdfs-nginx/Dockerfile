## Dockerfile
FROM centos:7

LABEL maintainer "wangjie"

ENV NGINX_VERSION 1.23.3
ENV LIBFASTCOMMON_VERSION V1.0.66
ENV LIBSERVERFRAME_VERSION V1.1.25
ENV FASTDFS_NGINX_MODULE_VERSION V1.23
ENV FASTDFS_VERSION V6.9.4
ENV BASE_PATH /app

#get all the dependences and nginx
RUN yum install -y git gcc make wget pcre pcre-devel openssl openssl-devel \
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
RUN git clone -b $FASTDFS_NGINX_MODULE_VERSION https://github.com/happyfish100/fastdfs-nginx-module.git fastdfs-nginx-module \ 
  && wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
  && tar -zxf nginx-${NGINX_VERSION}.tar.gz \
  && cd nginx-${NGINX_VERSION} \
  && ./configure --prefix=/usr/local/nginx \
      --add-module=${BASE_PATH}/fastdfs-nginx-module/src/ \
      --with-stream=dynamic \
  && make \
  && make install \
  && ln -s /usr/local/nginx/sbin/nginx /usr/bin/ \
  && rm -rf ${FASTDFS_PATH}/nginx-* \
  && rm -rf ${FASTDFS_PATH}/fastdfs-nginx-module

WORKDIR ${BASE_PATH}

#make the entrypoint.sh executable
COPY start.sh /usr/bin/
RUN chmod a+x /usr/bin/start.sh

ENTRYPOINT ["/usr/bin/start.sh"]