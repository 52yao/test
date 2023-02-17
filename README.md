##### 在做项目中经常会遇到有站点用jwt来做身份验证和授权，万一其中某个管理员是使用了弱密码作为密钥呢，于是有了这个工具。</br>

# jwt2.0

usage: jwt2.py [-h] [-jwt JWT] [-alg ALG]</br>

爆破JWT弱密钥</br>

options:</br>
  -h, --help  show this help message and exit</br>
  -jwt JWT    要爆破的JWT字符串</br>
  -alg ALG    签名算法，可选值为['sha256', 'sha238', 'sha512']中的一种，默认为sha256</br>

1、在本地新建一个key.txt文档，写入一些常用的密钥</br></br>
2、修改jwt2.py里对应的header和payload的值</br></br>
3、用法：</br>
python jwt2.py -jwt eydhbGcnOiAnc2hhNTEyJywgJ3R5cCc6ICdKV1QnfQ.eydzdWInOiAnMTIzNDU2Nzg5MCcsICduYW1lJzogJ0pvaG4gRG9lJywgJ2hhaGFoJzogJyAyMjIyJywgJ3Bhc3N3b3JkJzogJzEyMzQ1JywgJ2lhdCc6IDE1MTYyMzkwMjJ9.MTakSzD_lg10qoeRwgD3ybfnPs8fiJEXGTj7wD_TNqgngs8VSN2Ryp4S34CC93znpLw4UYw4qqUVzg0titiblA -alg sha512</br></br></br>

-jwt为必选项，后面跟着要爆破的jwt</br></br>
-alg为可选项，后面跟签名算法，如果不带此参数，默认使用sha256</br></br>

![图片](https://user-images.githubusercontent.com/67967304/219557266-67e342dc-33f6-4552-a5ac-7d9003559456.png)






# jwt1.0
1、这是一个用来爆破jwt的py脚本，需要在本地创建一个key.txt文档，里面写入一些常用的私钥。</br>
2、在jwt.py中修改对应的header及paylaod，参考如下：</br>
header = {</br>
    'alg': 'HS256',</br>
    'typ': 'JWT'</br>
}</br>
payload = {</br>
    'sub': '1234567890',</br>
    'name': 'John Doe',</br>
    'password':'12345',</br>
    'iat': 1516239022</br>
}</br>
</br>
3、python jwt.py执行即可 ，执行成功后会在当前目录下创建一个jwt_token.txt的文件，里面保存生成的jwt。
![图片](https://user-images.githubusercontent.com/67967304/219542936-593d596d-0828-4ed5-ad0a-ef1a4679d8a0.png)

</br>手动将生成的jwt与网站中的jwt进行对比，如果一致，则对应的key值为密钥
