FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN apt-get install wget -y
RUN apt-get install git -y
RUN apt-get install unzip -y
RUN wget https://github.com/facebookresearch/fastText/archive/v0.9.1.zip
RUN unzip v0.9.1.zip
RUN cd /fastText-0.9.1
RUN cd /fastText-0.9.1
RUN ls
RUN git clone https://github.com/facebookresearch/fastText.git
WORKDIR /fastText/
RUN ls
RUN pip3 install .
RUN pip3 install mecab-python3
RUN export LANG=C.UTF-8
RUN export LANGUAGE=en_US:

