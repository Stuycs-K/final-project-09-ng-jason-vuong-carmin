#Chaocipher

__KEYSIZE__ = 26
__NADIR__ = __KEYSIZE__ // 2

def encrypt(text, cipherText, plainText):
    # text 
    text = text.upper()
    output = ""
    for char in text: 
        cipherText, plainText = shift(char, cipherText, plainText)
        output += cipherText[0]
        cipherText = fixedCipher(cipherText) 
        plainText = fixedPlain(plainText)
    return output

def shift(character, cipherText, plainText): 
    #shift until 
    if character not in plainText: 
        print("Invalid character inputted")
        exit(1)

    while (plainText[0] != character): 
        temp = plainText[0] 
        for i in range (__KEYSIZE__): 
            plainText[i] = plainText[ (i+1) % __KEYSIZE__]
        plainText[__KEYSIZE__ - 1] = temp 
        temp = cipherText[0]
        for i in range (__KEYSIZE__): 
            cipherText[i] = cipherText[ (i+1) % __KEYSIZE__]
        cipherText[__KEYSIZE__ - 1] = temp
    
    return cipherText, plainText 


def fixedCipher (cipherText): 
    temp = cipherText[1] 
    for i in range(1, __NADIR__): 
        cipherText[i] = cipherText[i + 1]
    cipherText[__NADIR__ ] = temp 
    return cipherText

def fixedPlain (plainText): 
    temp = plainText[0] 
    for i in range (__KEYSIZE__): 
        plainText[i] = plainText[ (i+1) % __KEYSIZE__]
    plainText[__KEYSIZE__ - 1] = temp 
    temp = plainText[2] # extract 2 from the zenith 
    for i in range (2, __NADIR__ ): 
        plainText[i] = plainText[i + 1]
    plainText[__NADIR__] = temp 
    return plainText
    
def decrypt(text, cipherText, plainText):
    text = text.upper()
    output = ""
    for char in text: 
        plainText, cipherText = shift(char, plainText, cipherText)
        #print(cipherText)
        output += plainText[0]
        cipherText = fixedCipher(cipherText) 
        plainText = fixedPlain(plainText)
    return output

if __name__ == "__main__":
    choice = input("Type 1 for encryption mode and 2 for decryption: ")
    
    if choice != "1" and choice != "2":
        print("Invalid choice")
        exit(1)

    cipherText = list(input("Please enter the CIPHER TEXT KEY: "))
    plainText = list(input("Please enter the PLAIN TEXT KEY: "))

    if len(cipherText) != __KEYSIZE__ or len(plainText) != __KEYSIZE__:
        print("Invalid key length. Please enter a key of length 26.")
        exit(1)

    text = input("Please enter the text to be encrypted or decrypted: ")

    if choice == "1":
        result = encrypt(text, cipherText, plainText)
        print(" ")
        print ("------ENCRYPTED TEXT------")
        print(result)
    elif choice == "2":
        result = decrypt(text, cipherText, plainText)
        print(" ")
        print ("------DECRYPTED TEXT------")
        print(result)
