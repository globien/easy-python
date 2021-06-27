# -*-coding:utf-8 -*-

"""
# File       : 305_双向加密通信.py
# Time       ：2021-05-03 4:11 下午
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""

from Crypto import Random
from Crypto.PublicKey import RSA

# 获取一个伪随机数生成器
random_generator = Random.new().read
# 获取一个rsa算法对应的密钥对生成器实例
rsa = RSA.generate(1024, random_generator)

# 生成私钥并保存
private_pem = rsa.exportKey()
with open('data/rsa.key', 'wb') as f:
    f.write(private_pem)

# 生成公钥并保存
public_pem = rsa.publickey().exportKey()
with open('data/rsa.pub', 'wb') as f:
    f.write(public_pem)


from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64

# 数据加密
message = "好奇怪的数字123。"
message = bytes(message, encoding='Utf-8')
with open('data/rsa.pub', 'rb') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    cipher_text = base64.b64encode(cipher_obj.encrypt(message)).decode('Utf-8')
    print('cipher test: ', cipher_text)

# 数据解密
with open('data/rsa.key', 'rb') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    random_generator = Random.new().read
    plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator).decode('Utf-8')
    print('plain text: ', plain_text)

