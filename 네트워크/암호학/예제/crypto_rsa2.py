from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA
import os.path

def createPEM():
    private_key = RSA.generate(1024) # RSA.generate()를 이용해 개인키를 생성
    f = open('mykey2.pem', 'wb+') # 개인키를 파일형태로 만들어서 저장  * wb+ : 이진 파일 읽고 쓰기(기존파일 삭제)
    f.write(private_key.exportKey('PEM'))
    f.close()

def readPEM():
    h = open('mykey2.pem','r')
    key = RSA.importKey(h.read()) 
    h.close()
    return key

def rsa_encrypt(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    encdata = public_key.encrypt(msg, 32)
    return encdata

def rsa_decrypt(msg):
    private_key = readPEM()
    decdata = private_key.decrypt(msg)
    return decdata


def main():
    file = '/home/jooyeon/jooyeon/memo/네트워크/암호학/예제/mykey2.pem'
    if os.path.isfile(file):
        print('파일 존재')
    else :
        print('파일 생성')
        createPEM()
    
    msg = "hello"
    print(rsa_encrypt(msg.encode('utf-8')))



main()


print('----------------------------------------')


def rsa_sign(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    hash = SHA.new(msg).digest()
    signature = private_key.sign(hash, '')
    return public_key, signature


def rsa_verify(msg, public_key, signature):
    hash = SHA.new(msg).digest()
    if public_key.verify(hash, signature):
        print("인증 O")
    else :
        print("인증 X")


def main2():
    msg = "hello word"
    public_key, signature = rsa_sign(msg.encode('utf-8'))
    rsa_verify(msg.encode('utf-8'), public_key, signature)


main2()