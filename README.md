# test
1、这是一个用来爆破jwt的py脚本，需要在本地创建一个key.txt文档，里面写入一些常用的私钥。
2、在jwt.py中修改对应的header及paylaod，参考如下：
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

python jwt.py执行即可 ，执行成功后会在当前目录下创建一个jwt_token.txt的文件，里面保存生成的jwt。
![图片](https://user-images.githubusercontent.com/67967304/219542936-593d596d-0828-4ed5-ad0a-ef1a4679d8a0.png)

手动将生成的jwt与网站中的jwt进行对比，如果一致，则对应的key值为密钥
