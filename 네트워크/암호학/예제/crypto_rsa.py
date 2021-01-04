from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA
import os.path


def createPEM():
    private_key = RSA.generate(1024) # RSA.generate()를 이용해 개인키를 생성 
    f = open('mykey.pem', 'wb+') # 개인키를 파일형태로 만들어서 저장  * wb+ : 이진 파일 읽고 쓰기(기존파일 삭제)
    f.write(private_key.exportKey('PEM'))    
    f.close()
"""
RSA.generate(bits, randfunc=None, progress_func=None, e=65537)
-> 새로운 RSA 키 개체를 무작위로 생성
    *  bits(int) : RSA 모듈러스이 키 길이 또는 크기(비트).256의 배수 여야하며 1024보다 작아서는 안됨. 2048 권장

exportKey(slef, format = 'PEM', passphrase = None, pkcs=1)
-> 이 RSA 키를 내보냅니다.
    * format(문자열) - 키 래핑에 사용할 형식
"""


def readPEM():
    h = open('mykey.pem', 'r')
    key = RSA.importKey(h.read())  # 저장된 개인키 읽기
    h.close()
    return key # mykey.pem 파일에 저장된 개인키를 읽어서 리턴 
"""
RSA.importKey ( externKey , passphrase = None )
-> 표준 형식으로 인코딩 된 RSA 키(공개 또는 개인 절반)를 가져온다
    * externKey(문자열) : 가져올 RSA 키이며 문자열로 인코딩됨.
"""

# RSA 공개키로 메시지를 암호화 하는  함수
def rsa_encrypt(msg): 
    private_key = readPEM()
    public_key = private_key.publickey()
    print(f"public_key : {public_key}")
    encdata = public_key.encrypt(msg, 32)  # private_key.publickey()로 공개키를 얻고, 이 공개키로 메시지 암호화  
    print(f"encdata : {encdata}")
    return encdata

"""
publickey(slef)
-> 공개 정보만을 담고 있는 새로운 키 생성 

encrypt(self, plaintext, K)
-> RSA로 데이터를 암호화
    * plaintext(바이트 문자열 또는 long) : RSA로 암호화 할 데이터 조각
    * K(바이트 문자열 또는 long) : 임의의 매개 변수 (호환성을 위해서만. 이 값은 무시됨))
"""

# RSA 개인키로 메시지를 복호화하는 함수
def rsa_decrypt(msg):   
    private_key = readPEM()
    decdata = private_key.decrypt(msg) # 공개키로 암호화한 메시지 개인키로 복호화
    return decdata
"""
decrypt(self, ciphertext)
-> RSA를 사용하여 데이터를 해독.
"""

def main1():
    file = '/home/jooyeon/jooyeon/memo/네트워크/암호학/예제/mykey.pem'
    if os.path.isfile(file):
        print('파일 존재')
    else :
        createPEM()

    msg = "Hello World"
    ciphered = rsa_encrypt(msg.encode('utf-8'))
    print(f"ciphered : {ciphered}")

    decipthered = rsa_decrypt(ciphered)
    print(f"decipthered : {decipthered}")


main1()


print("------------------------------------------------------------")

# 사용자의 개인키로 서명하는 측
def rsa_sign(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    hash = SHA.new(msg).digest()
    print(f"hash : {hash}")
    signature = private_key.sign(hash, '') # 개인키의 sign() 이용 : 사용자의 개인키로 서명하기.
                                           # 확인해야 할 정보인 msg의 SHA256 해시를 구하고 이 값에 개인키로 서명
   # print(f"signature :{signature}")
    return public_key, signature

"""
sign(self, M, K)
-> RSA로 데이터에 서명함
    * M(바이트 문자열 또는 long) : RSA로 서명할 데이터 조각
    * K(바이트 문자열 또는 long) : 임의의 매개 변수(호환성을 위해서만. 이 값은 무시됨)
"""


# 시용자의 공개키로 서명 확인하는 측
def rsa_verify(msg, public_key, signature):
    hash = SHA.new(msg).digest()            # 확인해야 할 정보인 msg의 SHA256 해시를 구함 
    print(f"hash : {hash}")
    if public_key.verify(hash, signature):  # 공개키의 verify() 함수의 인자로 해시값과 서명 된 정보 입력 
        print('인증 O')
    else :
        print('인증 X')

"""
verify(self, M, signature)
-> RSA 서명의 유효성 확인
    * M(바이트 문자열 또는 long) : 예상되는 메시지
    * signature(sing에 반환되는 2개 항목 튜플 ) : 확인할 RSA 서명. 첫 번째 항목은 실제 서명, 두 번째 항목은 항상 무시됨.
"""

def main2():
    msg = 'My name is jooyeon'
    public_key, signature = rsa_sign(msg.encode('utf-8'))
    rsa_verify(msg.encode('utf-8'), public_key, signature)


main2()










# Crypto.PublicKey.RSA._RSAobj
# https://pythonhosted.org/pycrypto/Crypto.PublicKey.RSA._RSAobj-class.html

# https://m.blog.naver.com/PostView.nhn?blogId=jkf941&logNo=220783412472&proxyReferer=https:%2F%2Fwww.google.com%2F

# https://blog.ryuss.com/109
# https://dhzzang.tistory.com/87

# https://djangoworld.tistory.com/16