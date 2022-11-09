FROM ubuntu:22.04

ENV TZ Asia/Seoul
ENV PYTHONIOENCODING UTF-8
ENV LC_CTYPE C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive #no interactive

#RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
RUN dpkg --add-architecture i386
RUN apt update && apt upgrade -y
RUN apt-get update && apt-get install -y netcat
RUN apt-get dist-upgrade

RUN apt install python3 python3-dev python3-pip -y
RUN apt install git curl wget vim zsh gdb make -y
RUN apt install libffi-dev build-essential libssl-dev libc6-i386 libc6-dbg gcc-multilib make -y

RUN apt-get install libcapstone-dev -y
RUN apt-get install libc6:i386 -y
RUN apt install ruby-full -y
RUN apt install ruby-dev -y

RUN gem install one_gadget
RUN gem install seccomp-tools

RUN pip3 install unicorn
RUN pip3 install keystone-engine
RUN pip3 install pathlib2
RUN pip3 install pwntools #only using python3
RUN pip3 install capstone ropper
RUN pip3 install ropgadget

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

WORKDIR root
RUN git clone https://github.com/pwndbg/pwndbg && \
	cd pwndbg && chmod +x setup.sh && ./setup.sh

RUN mkdir .zsh
RUN git clone https://github.com/sindresorhus/pure .zsh/pure
RUN git clone https://github.com/zdharma/fast-syntax-highlighting .zsh/fast-syntax-highlighting
RUN echo "ZSH_THEME=""\\nsource /root/.zsh/fast-syntax-highlighting/F-Sy-H.plugin.zsh\\nfpath+=/root/.zsh/pure\\nautoload -U promptinit; promptinit\\nprompt pure" > .zshrc

RUN mkdir /pwn
WORKDIR /pwn
CMD [ "/bin/zsh" ]

