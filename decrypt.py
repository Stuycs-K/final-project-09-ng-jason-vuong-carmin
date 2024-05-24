#Chaocipher decryption

import encrypt

def decrypt(text, key1, key2):
    output = ""
    text = text.upper()
    for char in text:
        for i in range(0, 26): 
            if char == key2[encrypt.__KEYSIZE__ - i - 1]: 
                output += key1[i]
                key2 = encrypt.swap(key2, encrypt.__KEYSIZE__ - i - 1)
                break
    return output

if __name__ == "__main__":
    text = "CCKLBQJYKJ"
    key1 = list("HXUCZVAMDSLKPEFJRIGTWOBNYQ")
    key2 = list("PTLNBQDEOYSFAVZKGJRIHWXUMC")
    print(decrypt(text, key1, key2))
