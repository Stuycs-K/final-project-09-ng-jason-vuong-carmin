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

def swap (key2, index):
    temp = key2[index]
    key2[index] = key2[(index + 13) % __KEYSIZE__]
    key2[(index + 13) % __KEYSIZE__] = temp
    return key2 

def reorder (cipherText, index): 
    # reorder the ciphertext 
    # this is t
    temp = cipherText[(index + 1) % __KEYSIZE__]
    for i in range(0, __KEYSIZE__):
        #pseudo code 
        #swap the ith element with the ith + 13 element
        #then move everything down  

    key1 = []
    key2 = []
    for i in range(0, 26):
        key1.append(plainText[cipherText.index(chr(65 + i))])
        key2.append(cipherText[i])
    return key1, key2


if __name__ == "__main__":
    text = "Hello, World!"
    cipherText = list("HXUCZVAMDSLKPEFJRIGTWOBNYQ")
    plainText = list("PTLNBQDEOYSFAVZKGJRIHWXUMC")
    print(encrypt(text, cipherText, plainText))