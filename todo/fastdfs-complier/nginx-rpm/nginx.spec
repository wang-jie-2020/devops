Summary: High Performance Web Server
Name: nginx
Version: 1.23.3
Release: el7
License: GPL
Group: Applications/Server
Source: nginx-1.23.3.tar.gz
URL: http://nginx.org/
Distribution: Linux
Packager: wangjie
BuildRoot: root/nginx-1.23.3-el7
BuildRequires: gcc,gcc-c++,pcre-devel,zlib-devel
%description
nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server
%post
id nginx &>/dev/null
 if [ $? -ne 0 ];
 then
   useradd nginx
 fi
echo "export PATH=/usr/local/nginx/sbin:$PATH" >> /etc/profile
source /etc/profile
declare -a filePaths
filePaths=(/var/log/nginx  /var/run  /var/cache/nginx)
for i in ${filePaths[*]}
do
        if [ ! -d ${i} ];
        then
                mkdir  ${i}
        fi
done
%preun
userdel -r nginx
%prep
%setup -q
%build
./configure \
--prefix=/usr/local/nginx \
--user=nginx \
--group=nginx \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--pid-path=/var/run/nginx.pid \
--lock-path=/var/run/nginx.lock \
--modules-path=/usr/lib64/nginx/modules \
--sbin-path=/usr/local/nginx/sbin/nginx \
--http-client-body-temp-path=/var/cache/nginx/client_temp \
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_addition_module \
--with-http_sub_module \
--with-http_dav_module \
--with-http_flv_module \
--with-http_mp4_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_random_index_module \
--with-http_secure_link_module \
--with-http_stub_status_module \
--with-http_auth_request_module \
--with-mail \
--with-mail_ssl_module \
--with-file-aio \
--with-ipv6
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%files
/usr/local/nginx
/etc/nginx

