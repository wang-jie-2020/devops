FROM gitlab/gitlab-runner:v11.1.0

# 修改软件源
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse' > /etc/apt/sources.list && \
    echo 'deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse' >> /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get clean

# 安装 Docker （容器中也可以安装docker，但是需要将容器中的docker /var/run/docker.sock 关联到宿主机中的/var/run/docker.sock，这样就可以操作宿主机中的docker了）
RUN apt-get -y install apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update -y && \
    apt-get install -y docker-ce
COPY daemon.json /etc/docker/daemon.json

# 安装 Docker Compose
WORKDIR /usr/local/bin
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x docker-compose

# 安装 Java（可以网上下载，也可以自己copy进容器安装）
RUN mkdir -p /usr/local/java
WORKDIR /usr/local/java
COPY jdk-8u321-linux-x64.tar.gz /usr/local/java
RUN tar -zxvf jdk-8u321-linux-x64.tar.gz && \
    rm -fr jdk-8u321-linux-x64.tar.gz

# 安装 Maven （可以网上下载，也可以自己copy进容器安装）
RUN mkdir -p /usr/local/maven
WORKDIR /usr/local/maven
COPY apache-maven-3.8.4-bin.tar.gz /usr/local/maven
#RUN wget https://raw.githubusercontent.com/topsale/resources/master/maven/apache-maven-3.5.3-bin.tar.gz
# COPY apache-maven-3.5.3-bin.tar.gz /usr/local/maven
RUN tar -zxvf apache-maven-3.8.4-bin.tar.gz && \
    rm -fr apache-maven-3.8.4-bin.tar.gz
COPY settings.xml /usr/local/maven/apache-maven-3.8.4/conf/settings.xml

# 配置环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_321
ENV MAVEN_HOME /usr/local/maven/apache-maven-3.8.4
ENV PATH $PATH:$JAVA_HOME/bin:$MAVEN_HOME/bin

# 最后将工作目录转换会根目录
WORKDIR /
