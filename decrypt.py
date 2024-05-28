#Chaocipher decryption

import encrypt

def decrypt(text, cipherText, plainText):
    return encrypt.encrypt(text, plainText, cipherText)

if __name__ == "__main__":
    text = "GZNDZ"
    cipherText = list("CHAOBDEFGIJKLMNPQRSTUVWXYZ")
    plainText = list("CIPHERABDFGJKLMNOQSTUVWXYZ")
    print(decrypt(text, cipherText, plainText))
