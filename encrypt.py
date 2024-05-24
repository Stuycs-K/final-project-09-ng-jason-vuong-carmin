#Chaocipher

__KEYSIZE__ = 26

def encrypt(text, key1, key2):
    # text 
    text = text.upper()
    output = ""
    for char in text: 
        for i in range(0, 26): 
            if char == key1[i]: 
                output += key2[__KEYSIZE__ - i - 1]
                key2 = swap(key2, __KEYSIZE__ - i - 1)
                break
    return output

def swap (key2, index):
    temp = key2[index]
    key2[index] = key2[(index + 13) % __KEYSIZE__]
    key2[(index + 13) % __KEYSIZE__] = temp
    return key2 


if __name__ == "__main__":
    text = "Hello, World!"
    key1 = list("HXUCZVAMDSLKPEFJRIGTWOBNYQ")
    key2 = list("PTLNBQDEOYSFAVZKGJRIHWXUMC")
    print(encrypt(text, key1, key2))