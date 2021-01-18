from Crypto.Cipher import AES
from Crypto.Util.Padding import pad , unpad
from base64 import b64decode , b64encode
import binascii

KEY = "This is a key123".encode("utf-8")
IV = "THis is a   R454".encode("utf-8")
MODE = AES.MODE_CBC



def encrypto(message,KEY,MODE,IV):

    formated_text = message.encode("utf-8")
    pad_text = pad(formated_text,16)
    e_cipher = AES.new(KEY,MODE,IV)
    encrypted_text = e_cipher.encrypt(pad_text)
    f_text = b64encode(encrypted_text)
    return f_text

def decrypto(message,KEY,MODE,IV):

    formated_text = b64decode(message)
    d_cipher = AES.new(KEY,MODE,IV)
    decrypted_text = d_cipher.decrypt(formated_text)
    f_text = unpad(decrypted_text,16)
    return f_text




