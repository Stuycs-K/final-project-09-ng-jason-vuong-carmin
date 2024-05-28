#Chaocipher decryption

import encrypt

def decrypt(text, cipherText, plainText):
    text = text.upper()
    output = ""
    for char in text: 
        plainText, cipherText = encrypt.shift(char, plainText, cipherText)
        #print(cipherText)
        output += plainText[0]
        cipherText = encrypt.fixedCipher(cipherText) 
        plainText = encrypt.fixedPlain(plainText)
    return output

if __name__ == "__main__":
    text = "GZNDZ"
    cipherText = list("CHAOBDEFGIJKLMNPQRSTUVWXYZ")
    plainText =  list("CIPHERABDFGJKLMNOQSTUVWXYZ")
    print(decrypt(text, cipherText, plainText))
