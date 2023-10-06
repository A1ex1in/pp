from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from base64 import b64decode
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
from base64 import b64decode

password = b'Ars longa, vita brevis'
salt = b64decode('aIPmr/bAh8EAk76Hna7wnA==')
keys = PBKDF2(password, salt, 64, count=1000000, hmac_hash_module=SHA512)
key = keys[:32]

message = 'cBilS/BiRyr8t+izl8HzypP5M10XFTYtNb5chePEMagXX1/I56mvysFHTcCuq3ijFLrap8LRX0g7rC6w98yYQZYwfcQ/UlUrk4jZS4qF5UPMGVB77061Z6TLcwiNbb0v90m1germqdUQTtZ0vnvRkYr6tYomgfXbYeiGvYfsEPqqq1+mL3/6OYBasF74IA9GKPMbJ4xL6/LwXsPQOjExj7/PuSGK1A+gMbxKUx7P8NcdtWkINPCN4/GG0xKvfsj1lKVEptoGf6LkQXCsKl6lqCqfspX7Vbnc9kU3W8R2cJUJKMt1p3yCPPUk9gJr+G4jRVtBYaZZFwOJS/Y+w8OTzA=='

# AES decryption
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = b64decode(message)
pt = cipher.decrypt(ciphertext)
print(pt.decode('utf-8'))