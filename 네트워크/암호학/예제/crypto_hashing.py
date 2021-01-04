import hashlib

"""
hash method
- update(data) : 데이터의 바이트로 해시 객체 업데이트 - 모든 인수를 연결하는 단일 호출과 동일
- digest() : 'bytes 객체'로 update() 메서드에 전달 된 바이트의 다이제스트를 반환. 
             0~255까지의 전체 범위에 있는 바이트를 포함할 수 있음
- hexdigest() : digest()와 비슷하지만, 다이제스트는 16진수만 포함하는 이중 길이의 '문자열'로 반환
                전자 메일이나 기타 바이너리가 아닌 환경에서 값을 안전하게 교환하는데 사용할 수 있음.
- digest_size : 결과 해시의 바이트 단위의 크기
- block_size  : 해시 알고리즘의 바이트 단위의 내부 블록 크기
"""

data = 'Test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)  
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'Hello World'.encode()
hash_object2 = hashlib.sha1(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)
print(f"block_size : {hash_object2.block_size}")
print(f"digest_size : {hash_object2.digest_size}")
print(f"digest : {hash_object2.digest()}")


print('-----------------------------------------------------')


data4 = 'zzzzzzzzzzzzzzzzzzzz'
print(hashlib.sha256(data4.encode()).hexdigest())


data3 = 'Hello World'.encode()
hash_object3 = hashlib.sha256()
hash_object3.update(data3)
hex_dig3 = hash_object3.hexdigest() # hexdigent  이용하여 객체로부터 SHA256 해시에 대한 16진수 값을 구함
print(hex_dig3) # 64자리 문자열 반환 
print(f"block_size : {hash_object3.block_size}")
print(f"digest_size : {hash_object3.digest_size}")
print(f"digest : {hash_object3.digest()}")











# hash.uhpdate()
# https://nodejs.org/api/crypto.html#crypto_hash_update_data_inputencoding




# https://python.flowdas.com/library/hashlib.html