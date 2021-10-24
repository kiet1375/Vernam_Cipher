from operator import xor
import socket

def encryptData(keys,text):

    encypted = bytearray()
    j = 0

    for i in text.encode():

        if(j == len(keys)):
            j = 0
        a = hex(i)
        b = hex (keys[j])
        out =  xor(int(a,16),int(b,16))
        encypted.append(out)
        j = j + 1
        
    return encypted

def decryptData(keys, text):

    decrypt = bytearray()
    j = 0 

    for i in text:

        if(j == len(keys)):
            j = 0
        a = hex(i)
        b = hex(keys[j])
        decrypt.append(xor(int(a,16),int(b,16)))
        j = j+1
    
    return decrypt



def Main():
    print("================= Welcome to Vernam Cipher Generator =========================")
    keys = [45,23,234,77,18,12,200,154,66,4,221]
    text = "Streams of paper with the random numbers in that fashion became a process known as 'one-time pad'. The Vernam using one-time pad is regarded as unbreakable."
    en = encryptData(keys, text)
    print("==============================================================================")
    print("")
    print("")
    print("Text to encypt:")
    print(text)
    print("")
    decrypt = bytearray()
    j = 0
    print("Encrypted text:")
    for i in en:
        print(str(chr(i)), end="")
    
    print("")
    print("")
    j = 0
    
    decrypt = decryptData(keys, en)
    
    print("Decrypted text:")
    for i in decrypt:
        print(str(chr(i)), end="")


if __name__=='__main__':
    Main()
