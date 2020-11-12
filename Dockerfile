# git, python 설치
FROM python:3.7.9-buster
RUN apt-get update
RUN apt-get install -y git

# 소스 코드 다운로드
RUN git clone https://github.com/byeongal/comcom.git /usr/src/comcom

# 필요한 파일 설치
WORKDIR /usr/src/comcom
RUN pip install -r requirements.txt

# web 서버 실행
EXPOSE 5000
CMD python server.py
