import getopt
from sys import argv

from flask import Flask

app = Flask(__name__)

# 상수 정의 부분
MIN_NUMBER = 0
MAX_NUMBER = 1000000

# 소수들을 저장해둘 리스트
prime_list = []

@app.route('/')
def hello_user():
    html = """\
    <!DOCTYPE html>
    <html>
    <head>
        <title>COMCOM Coding Interview</title>
    </head>
    <body>
        <p>How to Use</p>
        <p>http://serverip:serverport/input=number</p>
        <p>ex) http://35.185.172.168/input=12345</p>
    </body>
    """
    return html

@app.route('/input=<number>')
def get_number(number):
    number = int(number)
    html = '''\
    <!DOCTYPE html>
    <html>
    <head>
        <title>COMCOM Coding Interview</title>
    </head>
        <body>
        <p>{}</p>
    </body>
    '''
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        output = f'숫자의 범위가 {MIN_NUMBER} 부터 {MAX_NUMBER} 까지 주어져야 합니다.'
    elif number == 0 or number == 1:
        output = '가장큰 소인수를 구할 수 없습니다.'
    else:
        idx = 0
        last_number = None
        while number != 1:
            while number % prime_list[idx] == 0:
                last_number = prime_list[idx]
                number //= prime_list[idx]
            idx += 1
        output = f'output {last_number}'
    return html.format(output)

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

def main(args):
    init()
    optlist, args = getopt.getopt(args[1:], '', ['ip=', 'port='])
    server_ip = '0.0.0.0'
    server_port = 5000
    for opt, arg in optlist:
        if opt == '--ip':
            server_ip = arg
        elif opt == '--port':
            server_port = int(arg)
    app.run(host=server_ip, port=server_port)

if __name__ == '__main__':
    main(argv)
