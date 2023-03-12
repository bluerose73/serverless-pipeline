# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
# RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN  apt-get update \
  && apt-get install -y wget \
  && apt-get install xz-utils \
  && rm -rf /var/lib/apt/lists/*

RUN ["bash", "./init.sh"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]