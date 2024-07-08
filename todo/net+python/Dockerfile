FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /root
RUN apt update \
    && apt install wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev -y \
    && wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz \
    && tar xzf Python-3.10.11.tgz \
    && cd Python-3.10.11 \
    && ./configure --enable-optimizations --enable-shared \
    && make altinstall \
    && cp libpython3.10.so.1.0 /usr/lib/ \
	&& ln -s /usr/local/bin/python3.10 /usr/bin/python \
	&& ln -s /usr/local/bin/pip3.10 /usr/bin/pip
