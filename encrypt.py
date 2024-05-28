#Chaocipher

__KEYSIZE__ = 26
__NADIR__ = __KEYSIZE__ // 2

def encrypt(text, cipherText, plainText):
    # text 
    text = text.upper()
    output = ""
    for char in text: 
        for i in range(0, 26): 
            if char == plainText[i]: 
                output += cipherText[i]
                key2 = reorder(cipherText, i)
                break
    return output

def shift(character, cipherText, plainText): 
    #shift until 
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
        cipherText[i] = cipherText[i + __NADIR__]
    cipherText[__NADIR__ + 1] = temp 
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
    
def zenithMethod (cipherText, index): 
    temp = cipherText[(index + 1) % __KEYSIZE__]
    for i in range(__NADIR__): 
        cipherText[(index + i + 1) % __KEYSIZE__ ] = cipherText[(index + i + 2) % __KEYSIZE__ ] 
    cipherText[(index + __NADIR__ + 1) % __KEYSIZE__] = temp 


def swap (key2, index):
    temp = key2[index]
    key2[index] = key2[(index + 13) % __KEYSIZE__]
    key2[(index + 13) % __KEYSIZE__] = temp
    return key2 

def reorder (cipherText, index): 
    # reorder the ciphertext 
    # this is t
    temp = cipherText[(index + 1) % __KEYSIZE__]
    for i in range(0, __NADIR__):
        swap(cipherText, (index + i) % __KEYSIZE__)
        #pseudo code 
        #swap the ith element with the ith + 13 element
        #then move everything down  
        

    return 


if __name__ == "__main__":
    text = "Hello, World!"
    cipherText = list("HXUCZVAMDSLKPEFJRIGTWOBNYQ")
    plainText = list("PTLNBQDEOYSFAVZKGJRIHWXUMC")
    erm = list("GIJKLMNPQRSTUVWXYZCHAOBDEF")
    print(fixedPlain(erm))