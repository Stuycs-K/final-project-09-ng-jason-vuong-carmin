# this is for a bytestream 

import os 
import sys 

global keySize
keySize = 1

def encrypt(data, cipherStream, keyStream):
    # text 
    output = []
    for byte in data: 
        cipherStream, keyStream = shift(byte, cipherStream, keyStream)
        output.append(cipherStream[0])
        cipherStream = fixedCipher(cipherStream) 
        keyStream = fixedPlain(keyStream)
    return bytes(output)

def shift(byte, cipherStream, keyStream): 
    #shift until 
    if byte not in keyStream: 
        print("Invalid byte inputted")
        print(f"There doesn't exist a character with the ASCII value of {byte} in the keystream.")
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
    for i in range(1, keySize // 2): 
        cipherStream[i] = cipherStream[i + 1]
    cipherStream[keySize // 2] = temp 
    return cipherStream

def fixedPlain (keyStream): 
    temp = keyStream[0] 
    for i in range (keySize): 
        keyStream[i] = keyStream[ (i+1) % keySize]
    keyStream[keySize - 1] = temp 
    temp = keyStream[2] # extract 2 from the zenith 
    for i in range (2, keySize // 2): 
        keyStream[i] = keyStream[i + 1]
    keyStream[keySize // 2] = temp 
    return keyStream
    
def decrypt(text, cipherStream, keyStream):
    output = []
    for char in text: 
        keyStream, cipherStream = shift(char, keyStream, cipherStream)
        #print(cipherStream)
        output.append(keyStream[0])
        cipherStream = fixedCipher(cipherStream) 
        keyStream = fixedPlain(keyStream)
    return bytes(output)

if __name__ == "__main__":

    # print(encrypt (sys.argv[1], sys.argv[2], sys.argv[3]))
    cipherArr = []
    keyArr = []

    if (len (sys.argv) < 6 ): 
        print('Not enough args')
        exit(1) 

    cipherLoc = sys.argv[1]
    # input("Please enter the path for the cipher file: ")
    with open(cipherLoc, "rb") as cipherFile:
        cipherStream = cipherFile.read()
        for x in cipherStream: 
          cipherArr.append(x) 
     
            
    # cipherStream = list(open(sys.argv[1], "r").read())
    # # print(cipherStream)
    keySize = len(cipherStream)
    keyLoc = sys.argv[2]
    # input ("Please enter the path for the key file: ")

    with open(keyLoc, "rb") as keyFile: 
        keyStream = keyFile.read()
        for x in keyStream: 
          keyArr.append(x)

    if len(keyStream) != keySize:
        print("Keys are of different lengths")
        exit(1)
    
    with open(sys.argv[3], "rb") as text: 
        text = text.read() 
    if (sys.argv[5] == "encrypt"): 
        text = encrypt(text, cipherArr, keyArr)
    elif (sys.argv[5] == "decrypt"): 
        text = decrypt(text, cipherArr, keyArr)

    with open(sys.argv[4], "wb+") as outPut: 
        outPut.write(text)

    # open(sys.argv[3], "r").read()
    # input("Please enter the text you've read: ")
    # choice = input("Type 1 for encryption mode and 2 for decryption: ")
    # if choice != "1" and choice != "2":
    #     print("Invalid choice")
    #     exit(1)
    # if choice == "1":
    #     result = encrypt(text, cipherStream, keyStream)
    #     print(" ")
    #     print ("------ENCRYPTED TEXT------")
    #     print(result)
    # elif choice == "2":
    #     result = decrypt(text, cipherStream, keyStream)
    #     print(" ")
    #     print ("------DECRYPTED TEXT------")
    #     print(result)


    

