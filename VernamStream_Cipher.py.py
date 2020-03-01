#Bug in the Decryptor

while True:
    ch =int(input("Press 1 to Encrypt || Press 2 to Decrypt\n>>>"))
    if ch == 1:
        text = input("text:") 
        print("!!! KEY MUST BE CHARACTERS !!!\n")
        key = input("Key:")  

        if len(key) != len(text):
            key = key*100         
        else:
            pass

        tx_ascii = [ord(tx) for tx in text]
        ky_ascii = [ord(ky) for ky in key]

        charactrize=[]
        for as1, as2 in zip(tx_ascii, ky_ascii): #@@@@@@
            charactrize.append(chr(as1 ^ as2)) 

        print("================================================")
        print("             !!! Encrypted !!!                  ")
        print("text:","".join(charactrize))
        print("================================================\n")

    elif ch == 2:

        text = input("text:") 
        key = input("Key:")  

        tx_ascii = [ord(tx) for tx in text]
        ky_ascii = [ord(ky) for ky in key]

        charactrize=[]
        for as1, as2 in zip(tx_ascii, ky_ascii): #@@@@@@
            charactrize.append(chr(as2 ^ as1)) 

        print("================================================")
        print("             !!! Decrypted !!!                  ")
        print("text:","".join(charactrize))
        print("================================================\n")
