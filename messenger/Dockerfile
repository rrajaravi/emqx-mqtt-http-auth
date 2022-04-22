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
RUN apt-get install -y sudo make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git libedit-dev iproute2

# Add fonts and refresh font cache
# ADD deployment/fonts/blenderPro /usr/share/fonts/truetype/blenderPro
# ADD deployment/fonts/arial /usr/share/fonts/truetype/arial
# RUN fc-cache -f -v
RUN usermod -aG sudo ${USER}
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Install pyenv
ENV LC_CTYPE=UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

USER ${USER}
WORKDIR /home/${USER}
RUN curl https://pyenv.run | bash
RUN echo 'export PATH="/home/${USER}/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Install Python
ENV PATH="/home/${USER}/.pyenv/bin:/home/${USER}/.pyenv/versions/messenger-3.8.0/bin/:${PATH}"
RUN pyenv install -s 3.8.0
RUN pyenv virtualenv 3.8.0 messenger-3.8.0
RUN pyenv init -
RUN pyenv virtualenv-init -

# Install app dependencies
COPY .python-version /home/${USER}/.python-version
RUN pip install -q pip-tools
COPY --chown=ubuntu requirements.txt /home/${USER}/requirements.txt
RUN pip-sync /home/${USER}/requirements.txt

COPY --chown=ubuntu . /home/${USER}/messenger
WORKDIR /home/${USER}/messenger

EXPOSE 8000

ENTRYPOINT [ "/home/ubuntu/messenger/manage.py", "runserver", "0.0.0.0:8000"]
