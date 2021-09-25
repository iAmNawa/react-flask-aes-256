from Cryptodome.Cipher import AES
from hashlib import md5
import base64

password = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
input = 'hello world'
output = 'UhbVSFjVt-gidWEGsnmqVA=='

BLOCK_SIZE = 16

def pad (data):
    pad = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + pad * chr(pad)

def unpad (padded):
    pad = ord(chr(padded[-1]))
    return padded[:-pad]

def get_key_iv (password):
    m = md5()
    m.update(password.encode('utf-8'))
    key = m.hexdigest()

    m = md5()
    m.update((password + key).encode('utf-8'))
    iv = m.hexdigest()

    return [key,iv]

def _encrypt(data, password):

    key,iv = get_key_iv(password)
    data = pad(data)

    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv[:16].encode('utf-8'))

    encrypted = aes.encrypt(data.encode('utf-8'))
    return base64.urlsafe_b64encode(encrypted)

def _decrypt(edata, password):
    edata = base64.urlsafe_b64decode(edata)
    key,iv = get_key_iv(password)

    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv[:16].encode('utf-8'))
    return unpad(aes.decrypt(edata))


output = _encrypt(input, password)
print(output)
plaintext = _decrypt(output, password)
print(plaintext)
