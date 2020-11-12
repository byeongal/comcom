## 커먼컴퓨터 개발자 채용 온라인 과제 풀이

### 문제 본문
The prime factors of 13195 are 5, 7, 13 and 29 (5 * 7 * 13 * 29 = 13195), and the largest prime factor is 29.
Implement a simple web server that can return the largest prime factor of the given number.

Submission:
1. Fully working public URL
ex) http://{your_ip}?input=13195 => output 29 on web browser.
2. Github Repo URL

Requirements:
User docker / kubernetes (https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).
Dockerfile & kubernetes yaml file must be included in your Github repository.
input range: 0~1000000

Good Luck!

### 풀이
문제를 간단하게 정리하면 소인수 분해를 하여 입력받은 수를 어떠한 소수들의 곱으로 표현 하였을 때, 가장 큰 소수를 찾아 브라우저에 출력을 시키는 문제이다. 

해당 문제를 풀기위해 **Flask**를 이용하여 간단한 웹서버를 만들었고, 웹 서버를 구동하게 되면, 가장 먼저 입력된 범위 내의 모든 소수를 구하여 리스트에 저장하였다. 소인수 분해를 단 한번만 하는 경우에는 입력된 수의 제곱근 까지 반복을 하며 확인을 하면 되지만, 소인수 분해를 여러번 하는 경우 미리 소수를 구한 다음 반복하면 불필요한 연산을 제거할 수 있다. 소수의 리스트를 제작한 다음에는 해당 소수로 입력으로 들어오는 수를 나누는 작업을 반복하여 입력으로 주어진 수를 소인수 분해 하였다. 

### 사용법
1. git repository 를 다운로드 받고, 필요한 파일을 설치 한다.
```shell
git clone https://github.com/byeongal/comcom.git
cd comcom
pip install requirements.txt
```

2. `server.py`파일을 실행한다.
```shell
python server.py --ip=<0.0.0.0> --port=<5000>
```

3. 웹브라우저에서 설정한 IP와 PORT에 맞게 접속을 하고 / 뒤에 소인수 분해할 숫자를 넣어준다.

ex) http://203.246.112.132:25000/input=13195

### 사용법(도커이미지)
1. Dockerfile을 다운로드 받는다.
```shell
wget https://github.com/byeongal/comcom/blob/main/Dockerfile
```

2. Dockerfile을 빌드 한다.
```shell
docker build -t comcom
```

3. 빌드한 도커 이미지를 실행 한다
```shell
docker run --rm -d -p <serverport>:5000 comcom
```

### 사용법(도커컴포즈)
1. 도커 컴포즈 파일을 다운로드 받는다.
```shell
wget https://github.com/byeongal/comcom/blob/main/docker-compose.yml
```

2. 도커 컴포즈 파일을 실행 한다.
```shell
docker-compose up -d
``` 