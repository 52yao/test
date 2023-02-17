import os
import hmac
import base64

# 从key.txt中读取private_key
with open('key.txt', 'r') as f:
    keys = f.read().splitlines()

# 构造JWT的header和payload
header = {
    'alg': 'HS256',
    'typ': 'JWT'
}
payload = {
    'sub': '1234567890',
    'name': 'John Doe',
    'password':'12345',
    'iat': 1516239022
}

# 对header和payload进行编码
header_enc = base64.urlsafe_b64encode(str(header).encode()).decode().strip('=')
payload_enc = base64.urlsafe_b64encode(str(payload).encode()).decode().strip('=')

for private_key in keys:
    # 使用private_key对header和payload进行签名
    signature = hmac.new(private_key.encode(), f"{header_enc}.{payload_enc}".encode(), 'sha256').digest()
    signature_enc = base64.urlsafe_b64encode(signature).decode().strip('=')

    # 拼接JWT字符串
    jwt_token = f"{header_enc}.{payload_enc}.{signature_enc}"

    # 将JWT字符串保存到文件中
    with open('jwt_token.txt', 'a') as f:
        f.write(jwt_token + '\n'+'\n')
