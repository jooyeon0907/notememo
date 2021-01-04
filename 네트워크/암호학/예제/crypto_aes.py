import base64
from Crypto import Random
from Crypto.Cipher import AES # Crypto.Cipher : 대칭키(AES,DES), 비대칭키(RSA) 알고리즘을 제공
import hashlib




# 블럭사이즈 자동 패딩처리  * 패딩 : 데이터를 특정 크기로 맞추기 위해 그 크기보다 부족한 부분을 뭔가로 채워넣는 작업 
BS = 16  # AES에서는 BLOCK_SIZE가 128bit로 고정(16바이트) / 암호화 키의 길이가 128bit, 192bit, 256bit인 세 가지 종류
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS) 
# 한글은 문자당 2바이트이므로 len(s.encode('utf-8')) 처리를 반드시 해줘야함 
#   -> len()함수를 활용해 길이를 통해 바이트 계산을 하는 방식이므로
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__(self, key):
        self.key = key
        # or self.key = hashlib.sha256().digest()    # 32바이트의 키 임의 생성


    def encrypt(self, raw):
        raw = pad(raw)
        # Hellooooooooooooo + (16 - 32 % 16) * chr(16 - 32 % 16)
        # Hellooooooooooooo + (16) * ''
        print(f"raw : {'Hellooooooooooooo' + (16) * ''}") # Hellooooooooooooo
        print(f"raw.encode('utf-8') : {raw.encode('utf-8')}") # b'Hellooooooooooooo\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f' 

        iv = Random.new().read( AES.block_size )  
        # Random.new() - 암호화된 '임의의 바이트'를 출력하는 파일 류 객체 반환
        # iv : 초기화 벡터 -> iv를 초기 셋팅해 암호화하고 복호화 할 때도 동일한 iv 값이 있어야함 
        print(f'iv(복호화 할 때와 같은 iv 값이 나와야함) : {iv}')
        
        cipher = AES.new( self.key, AES.MODE_CBC, iv ) # CBC모드로 암호화하고 , 32비트 암호 키 만들기 
                                                       # AES.new(key, *args, **kwargs) - Create a new AES cipher
     #   print(f"cipher.encrypt( raw.encode('utf-8') )  :{cipher.encrypt( raw.encode('utf-8') ) }")
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )
           # raw.encode('utf-8') 16바이트 바이너리로 변환 한 후, 다시  base64.b64encode로 인코딩 -> byte를 기준으로 문자열화 시키는 인코딩 방식
  
    """
    AES.new(key, *args, **kwargs) 
    -> 새 AES 암호를 생성 
        * key  : 대칭 암호에서 사용할 비밀 키. 길이는 16,24 또는 32바이트여야 함 
        * mode : 암호화 또는 암호 해독에 사용할 연결 모드
        * iv   : 암호화 또는 복호화에 사용할 초기화 벡터   
    
    encrypt(self, plaintext)
    -> 초기화시 설정된 키와 매개 변수로 데이터를 암호화 함.


    base64.b64encode(s, altchars=None)
    -> Base64를 사용하여 '바이트 열류 객체'를 인코딩하고 '바이트 열 객체'를 반환

    """

    def decrypt(self, enc):
        enc = base64.b64decode(enc)   
        print(f'base64.b64decode(enc): {enc}')
        # enc: b'-\xdb\xefc\xc9\x9dxL\x8f6JQ\xe2\x14o\x0bU(H\x98\xc6\x113\xb0\xf6C\xf4\xaf8\x14!\x03\x04B\xf0\x84\xb7\xee\xb8\xde\x1a\xbd\x1f\xa3\xe6\x88\x10\x1c'
        iv = enc[:16]
        print(f'iv(암호화 할 때와 같은 iv 값이 나와야함) : {iv}') # b'-\xdb\xefc\xc9\x9dxL\x8f6JQ\xe2\x14o\x0b'
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # print(f'cipher.decrypt : {cipher.decrypt} ')
        print(f'enc[16:] : {enc[16:]}') # b'U(H\x98\xc6\x113\xb0\xf6C\xf4\xaf8\x14!\x03\x04B\xf0\x84\xb7\xee\xb8\xde\x1a\xbd\x1f\xa3\xe6\x88\x10\x1c'
        # print(f'cipher.decrypt( enc[16:]) : {cipher.decrypt( enc[16:])}') # b'Hellooooooooooooo\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
        # s = b'Hellooooooooooooo\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
        # print('=========')
        # print(ord(s[len(s)-1:])) ## 15
        # print(s[:15])  ## b'Hellooooooooooo'
        return unpad(cipher.decrypt( enc[16:]) ).decode('utf-8')
    """
    base64.b64decode(s, altchars=None, validate=False)
    -> Base64로 인코딩 된 '바이트 열류 객체' 또는 'ASCII'문자열을 디코딩 -> bytes 객체로 반환

    decrypt(self, ciphertext)
    -> 초기화시 설정된 키와 매개 변수로 데이터를 해독한다.
    """

# AES256을 구현하기 위해 32 바이트의 키를 생성
key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,
        0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6, 0xA7, 0x6E, 0xE6, 0xE5, 0x3F]
data ="Hellooooooooooooo"

print(f'bytes(key) : {bytes(key)}')
print('-----------------------------------------------------------')
encrypted_data = AESCipher(bytes(key)).encrypt(data)  
print(f'암호화 : {encrypted_data}')
print('-----------------------------------------------------------')
decrypted_data = AESCipher(bytes(key)).decrypt(encrypted_data)
print(f"복호화 : {decrypted_data}")










# 참고 사이트
# https://mkjjo.github.io/python/2019/08/04/crypto.html



# https://jinisbonusbook.tistory.com/67

# base64
# https://effectivesquid.tistory.com/entry/Base64-%EC%9D%B8%EC%BD%94%EB%94%A9%EC%9D%B4%EB%9E%80

# iv , padding
# http://blog.daum.net/tlos6733/105