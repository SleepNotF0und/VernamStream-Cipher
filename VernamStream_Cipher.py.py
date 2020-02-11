while True:
    ch =int(input("Press 1 to Encrypt || Press 2 to Decrypt\n"))

    if ch == 1:
        text = input("text:") 

        key = input("Key:")  

        if len(key) != len(text):
            key = key*2         
        else:
            pass

        tx_ascii = [ord(tx) for tx in text]

        ky_ascii = [ord(ky) for ky in key]

        charactrize=[]

        for as1, as2 in zip(tx_ascii, ky_ascii): #@@@@@@
            charactrize.append(chr(as1 ^ as2)) 

        vernam ="".join(charactrize) ##@@@@@@@
        print("================================================")
        print("             !!! Encrypted !!!                  ")
        print("text:",vernam)
        print("================================================\n")

    elif ch == 2:

        text = input("text:") 

        key = input("Key:")  

        tx_ascii = [ord(tx) for tx in text]

        ky_ascii = [ord(ky) for ky in key]

        charactrize=[]
        for as1, as2 in zip(tx_ascii, ky_ascii): #@@@@@@
            charactrize.append(chr(as1 ^ as2)) 

        vernam ="".join(charactrize) #@@@@@
        print("================================================")
        print("             !!! Decrypted !!!                  ")
        print("text:",vernam)
        print("================================================\n")