from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rea_enc(msg):
    private_key = RSA.generate(1024) # RSA.generate()를 이용해 개인키를 생성
    public_key = private_key.publickey()
    encdata = public_key.encrypt(msg,32)
    # private_key.publickey()로 공개키를 얻고, 이 공개키를 메세지로 암호화
    print(encdata)
    print('-------------------------------------')
    decdata = private_key.decrypt(encdata)
    print(decdata)
    # 공개키로 암호화한 메시지를 개인키로 복호


def main():
    msg = 'HELLOOOOOOO'
    rea_enc(msg.encode('utf-8'))

main()




# https://m.blog.naver.com/PostView.nhn?blogId=jkf941&logNo=220783412472&proxyReferer=https:%2F%2Fwww.google.com%2F

# https://blog.ryuss.com/109
# https://dhzzang.tistory.com/87

# https://djangoworld.tistory.com/16