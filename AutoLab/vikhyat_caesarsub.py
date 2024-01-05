def caesar(shift,str):
    # String will always be in capital letter 
    # Creating a dictionary 
    dict_cap = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    dict_cap_rev = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    
    if (shift==0):
        return str
    elif(shift>0): #If shift is positive
        output_str = []
        for i in range(len(str)):
            if(str[i] in dict_cap):
                temp = dict_cap[str[i]]
                if(temp+shift>26):
                    temp = (temp+shift)%26
                    output_str.append(dict_cap_rev[temp])
                elif(temp+shift<=26):
                    output_str.append(dict_cap_rev[temp+shift])
            elif(str[i] == " "):
                output_str.append(" ")
                
        out_str = "".join(output_str)
        return out_str
    else: # If shift is negative 
        shift = abs(shift)
        b = shift%26
        shift = 26 - b
        output_str = []
        for i in range(len(str)):
            if(str[i] in dict_cap):
                temp = dict_cap[str[i]]
                if(temp+shift>26):
                    temp = (temp+shift)%26
                    output_str.append(dict_cap_rev[temp])
                elif(temp+shift<=26):
                    output_str.append(dict_cap_rev[temp+shift])
            elif(str[i] == " "):
                output_str.append(" ")        
        out_str= "".join(output_str)
        return out_str
    
