from Cryptodome import Random
from Cryptodome.Cipher import AES

#BS = 16
#def pad(data):
#    padding = BS - len(data) % BS
#    return data + padding * chr(padding)

def unpad(data):
    return data[0:-ord(data[-1])]

def decrypt_node(hex_data, key='0'*32, iv='0'*16):
    data = ''.join(map(chr, bytearray.fromhex(hex_data)))
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(aes.decrypt(data))

#def encrypt_node(data, key='0'*32, iv='0'*16):
#    aes = AES.new(key, AES.MODE_CBC, iv)
#    return aes.encrypt(pad(data)).encode('hex')

#print(encrypt_node('this-needs-to-be-encrypted'))
print(decrypt_node('b88e5f69c7bd5cd67c9c12b9ad73e8c1ca948ab26da01e6dad0e7f95448e79f4'))
