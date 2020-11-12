from flask import Flask

app = Flask(__name__)

# 상수 정의 부분
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000
MIN_NUMBER = 0
MAX_NUMBER = 1000000

# 소수들을 저장해둘 리스트
prime_list = []

@app.route('/')
def hello_user():
    return 'Hello ComCom'

@app.route('/input=<number>')
def get_number(number):
    number = int(number)
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        return f'숫자의 범위가 {MIN_NUMBER} 부터 {MAX_NUMBER} 까지 주어져야 합니다.'
    if number == 0 or number == 1:
        return '가장큰 소인수를 구할 수 없습니다.'
    idx = 0
    last_number = None
    while number != 1:
        while number % prime_list[idx] == 0:
            last_number = prime_list[idx]
            number //= prime_list[idx]
        idx += 1
    return f'output {last_number}'

# 에라토스테네스의 체
def init():
    prime_bool_list = [ True ] * (MAX_NUMBER + 1)
    prime_bool_list[0] = prime_bool_list[1] = False
    i = 2
    while i * i <= MAX_NUMBER:
        if prime_bool_list[i]:
            j = i * i
            while j <= MAX_NUMBER:
                prime_bool_list[j] = False
                j += i
        i += 1
    for number in range(2, MAX_NUMBER + 1):
        if prime_bool_list[number]:
            prime_list.append(number)
    del prime_bool_list

if __name__ == '__main__':
    init()
    app.run(host=SERVER_IP, port=SERVER_PORT)