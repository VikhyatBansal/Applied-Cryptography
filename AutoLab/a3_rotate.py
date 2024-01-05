def rotate(plaintext,key):
    mat_lc = [[0 for i in range(26)] for i in range(26)]
    mat_capital = [[0 for i in range(26)] for i in range(26)]
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""
    cipher_capital = ""
    
    for i in range(26):
        for j in range(26):
            mat_capital[i][j] = alphabets_capital[(i+j)%26]
            
    for i in range(26):
        for j in range(26):
            mat_lc[i][j] = alphabets[(i+j)%26]
    
    i = 0
    for l in range(len(plaintext)):
        if(plaintext[l] in alphabets):
            cipher += mat_lc[ord(key[i])-97][ord(plaintext[l])-97]
            i+=1
            if(i==len(key)):
                i=0
    
        elif(plaintext[l] in alphabets_capital):
            cipher_capital += mat_capital[ord(key[i])-65][ord(plaintext[l])-65]
            i+=1
            if(i==len(key)):
                i=0
            
        else:
            if(len(cipher_capital)==0):
                cipher += " "
            else:
                cipher_capital += " "
            
    if(len(cipher_capital)==0):
        return cipher
    else:
        return cipher_capital
            

# plaintext = input("Enter the plaintext: ")
# key = input("Enter the key: ")
# print("The cipher text is: ",rotate(plaintext,key))