FROM ubuntu:20.04

ARG USER=ubuntu
ARG UID=1000
ARG GID=1000

RUN useradd -ms /bin/bash ${USER} --uid=${UID}

# set timezone
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y locales && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
# Install required client utilites
# RUN apt-get install -y apt-utils fontconfig libmysqlclient-dev mysql-client vim net-tools iputils-ping
# For mysql
RUN apt-get install -y mysql-client libmysqlclient-dev
# Install pyenv dependencies, iproute2 is for ip command not pyenv dep
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git libedit-dev iproute2

RUN wget https://www.emqx.io/downloads/broker/v4.2.10/emqx-ubuntu20.04-4.2.10-x86_64.deb
RUN apt install ./emqx-ubuntu20.04-4.2.10-x86_64.deb
# Add fonts and refresh font cache
# ADD deployment/fonts/blenderPro /usr/share/fonts/truetype/blenderPro
# ADD deployment/fonts/arial /usr/share/fonts/truetype/arial
# RUN fc-cache -f -v

# Install pyenv
ENV LC_CTYPE=UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN apt-get install -y sudo
RUN usermod -aG sudo ${USER}
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY --chown=emqx loaded_plugins /var/lib/emqx/loaded_plugins
COPY --chown=emqx plugin_conf/emqx*.conf /etc/emqx/plugins/

USER ${USER}
WORKDIR /home/${USER}
COPY --chown=ubuntu ../ /home/${USER}/emqx

EXPOSE 18083 1883 8083
ENTRYPOINT [ "sudo", "/usr/bin/emqx", "foreground" ]