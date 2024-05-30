# this is for a bytestream 

import os 
import sys 

global keySize = 1

def encrypt(data, cipherStream, keyStream):
    # text 
    text = text.upper()
    output = ""
    for byte in data: 
        cipherStream, keyStream = shift(byte, cipherStream, keyStream)
        output += cipherStream[0]
        cipherStream = fixedCipher(cipherStream) 
        keyStream = fixedPlain(keyStream)
    return output

def shift(byte, cipherStream, keyStream): 
    #shift until 
    if byte not in keyStream: 
        print("Invalid byte inputted")
        exit(1)

    while (keyStream[0] != byte): 
        temp = keyStream[0] 
        for i in range (keySize): 
            keyStream[i] = keyStream[ (i+1) % keySize]
        keyStream[keySize - 1] = temp 
        temp = cipherStream[0]
        for i in range (keySize): 
            cipherStream[i] = cipherStream[ (i+1) % keySize]
        cipherStream[keySize - 1] = temp
    
    return cipherStream, keyStream 


def fixedCipher (cipherStream): 
    temp = cipherStream[1] 
    for i in range(1, __NADIR__): 
        cipherStream[i] = cipherStream[i + 1]
    cipherStream[__NADIR__ ] = temp 
    return cipherStream

def fixedPlain (keyStream): 
    temp = keyStream[0] 
    for i in range (keySize): 
        keyStream[i] = keyStream[ (i+1) % keySize]
    keyStream[keySize - 1] = temp 
    temp = keyStream[2] # extract 2 from the zenith 
    for i in range (2, __NADIR__ ): 
        keyStream[i] = keyStream[i + 1]
    keyStream[__NADIR__] = temp 
    return keyStream
    
def decrypt(text, cipherStream, keyStream):
    text = text.upper()
    output = ""
    for char in text: 
        keyStream, cipherStream = shift(char, keyStream, cipherStream)
        #print(cipherStream)
        output += keyStream[0]
        cipherStream = fixedCipher(cipherStream) 
        keyStream = fixedPlain(keyStream)
    return output

if __name__ == "__main__":

    cipherLoc = input("Please enter the path for the cipher file: ")
    cipherStream = list(open(cipherLoc).read("r"))
    keySize = len(cipherStream)
    keyLoc = input ("Please enter the path for the key file: ")
    keyStream = list(open(keyLoc).read("r"))

    if len(keyStream) != keySize:
        print("Keys are of different lengths")
        exit(1)

    while (True) {
        text = input("Please enter the text you've read: ").read("r")
        

    } 
    text = input("Please enter the text to be encrypted or decrypted: ")

    if choice == "1":
        result = encrypt(text, cipherStream, keyStream)
        print(" ")
        print ("------ENCRYPTED TEXT------")
        print(result)
    elif choice == "2":
        result = decrypt(text, cipherStream, keyStream)
        print(" ")
        print ("------DECRYPTED TEXT------")
        print(result)
