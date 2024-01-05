def bin2dec(num):
    dec = 0
    cnt = 0
    num = int(num)
    while num!=0:
        dec += num%10 * (2**cnt)
        num = num//10
        cnt += 1
    return dec

def dec2bin(num):
    binar = ''
    while num!=0:
        binar += str(num%2)
        num = num//2
    return binar[::-1]

def hex2dec(num):
    dec = 0
    cnt = 0
    hex_dic = {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14, 'F':15}
    for i in range(len(num)):
        if num[i] in hex_dic.keys():
            dec += hex_dic[num[i]] * (16**(len(num)-1-cnt))
        else:
            dec += int(num[i]) * (16**(len(num)-1-cnt))
        cnt += 1
    return dec

def dec2hex(num):
    hexdec = ''
    hex_dic = {0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',
               7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
               13:'D', 14:'E', 15:'F'}
    while num>=0:
        if num%16 in hex_dic.keys():
            hexdec += hex_dic[num%16]
        else:
            hexdec += str(num%16)
        if num//16==0:
            break
        num = num//16
    return hexdec[::-1]

def hex2bin(num):
    res = ''
    hex_bin_dic = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
                   '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
                   'C':'1100','D':'1101','E':'1110','F':'1111'}
    for i in range(len(num)):
        res += hex_bin_dic[num[i]]
    return res

def bin2hex(num):
    res = ''
    bin_hex_dic = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5',
                   '0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B',
                   '1100':'C','1101':'D','1110':'E','1111':'F'}
    for i in range(0,len(num),4):
        res += bin_hex_dic[num[i:i+4]]
    return res
def initialpermutation(inpstr):
    matrix = [[0 for i in range(8)] for j in range(8)]
    rows = 0
    cols = 1
    l = 57
    matrix[0][0] = inpstr[l]
    for o in range(63):
        if(cols%8==0):
            rows+=1
            cols=0
            l+=58
            if (rows==4):
                l = 56
            else:
                None
            matrix[rows][cols] = inpstr[l]
            cols+=1
        else:
            l-=8
            matrix[rows][cols] = inpstr[l]
            cols+=1
            
    
    out = ''
    for o in range(8):
        out+="".join(matrix[o])
        
    return out

def inversepermutation(inpstr):
    matrix = [[0 for i in range(8)] for j in range(8)]
    rows = 0
    columns = 1
    l = 39
    k = 7
    matrix[0][0] = inpstr[l]
    for o in range(63):
        if(columns%8==0):
            columns = 0
            rows+=1
            l = 39 - rows
            k = 7 - rows
            matrix[rows][columns] = inpstr[l]
            columns+=1
        elif(columns%2==0):
            l+=8
            matrix[rows][columns] = inpstr[l]
            columns+=1
        else:
            matrix[rows][columns] = inpstr[k]
            k+=8
            columns+=1
     
    out = ''
    for o in range(8):
        out+="".join(matrix[o])
    return out

permuted_1 = [[57,49,41,33,25,17,9],[1,58,50,42,34,26,18],[10,2,59,51,43,35,27],[19,11,3,60,52,44,36],[63,55,47,39,31,23,15],[7,62,54,46,38,30,22],[14,6,61,53,45,37,29],[21,13,5,28,20,12,4]]

permuted_2 = [[14,17,11,24,1,5],[3,28,15,6,21,10],[23,19,12,4,26,8],[16,7,27,20,13,2],[41,52,31,37,47,55],[30,40,51,45,33,48],[44,49,39,56,34,53],[46,42,50,36,29,32]] 

def pc1_pass(key):
    key_56 = [[0 for i in range(7)] for j in range(8)]
    for i in range(len(permuted_1)):
        for j in range(len(permuted_1[0])):
            key_56[i][j] = key[permuted_1[i][j]-1]
    res=''
    for i in range(len(key_56)):
        res+="".join(key_56[i])
    return res

def pc2_pass(str):
    key_48 = [[0 for i in range(6)] for j in range(8)]
    for i in range(len(permuted_2)):
        for j in range(len(permuted_2[0])):
            key_48[i][j] = str[permuted_2[i][j]-1]
    res=''
    for i in range(len(key_48)):
        res+="".join(key_48[i])
    return res

# Generating 16 keys
permuted_1 = [[57,49,41,33,25,17,9],[1,58,50,42,34,26,18],[10,2,59,51,43,35,27],[19,11,3,60,52,44,36],[63,55,47,39,31,23,15],[7,62,54,46,38,30,22],[14,6,61,53,45,37,29],[21,13,5,28,20,12,4]]

permuted_2 = [[14,17,11,24,1,5],[3,28,15,6,21,10],[23,19,12,4,26,8],[16,7,27,20,13,2],[41,52,31,37,47,55],[30,40,51,45,33,48],[44,49,39,56,34,53],[46,42,50,36,29,32]] 

iter_dict = {'0':1,'1':1,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':1,'9':2,'10':2,'11':2,'12':2,'13':2,'14':2,'15':1} 

# Generating 1 key using PC_1 and PC_2

def keygen(iter,key):
    pc_1_str = ''
    for i in range(len(permuted_1)):
        for j in range(len(permuted_1[i])):
            pc_1_str += key[permuted_1[i][j]-1]
            
    c = pc_1_str[:28]
    d = pc_1_str[28:]
    # Shifting to left by 1 position
    c = c[1:] + c[:1]
    d = d[1:] + d[:1]
    cd = c + d
    pc_2_str = ''
    for i in range(len(permuted_2)):
        for j in range(len(permuted_2[i])):
            pc_2_str += cd[permuted_2[i][j]-1]
    
    # Generating 16 keys
    
    keys = []
    keys.append(pc_2_str)
    for i in range(1,16):
        c = c[iter_dict[str(i)]:] + c[:iter_dict[str(i)]]
        d = d[iter_dict[str(i)]:] + d[:iter_dict[str(i)]]
        cd = c + d
        pc_2_str = ''
        for i in range(len(permuted_2)):
            for j in range(len(permuted_2[i])):
                pc_2_str += cd[permuted_2[i][j]-1]
        keys.append(pc_2_str)
        
    return keys[iter]

        

def S_box():
    S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    
    S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    
    S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
    
    S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
    
    S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
    
    S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
    
    S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
    
    S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

    S = [S1,S2,S3,S4,S5,S6,S7,S8]
    
    return S

def E_bit_pass(str):
    E_bit = [[32,1,2,3,4,5],[4,5,6,7,8,9],[8,9,10,11,12,13],[12,13,14,15,16,17],[16,17,18,19,20,21],[20,21,22,23,24,25],[24,25,26,27,28,29],[28,29,30,31,32,1]]
    for i in range(len(E_bit)):
        for j in range(len(E_bit[0])):
            E_bit[i][j] = str[E_bit[i][j]-1]
    res=''
    for i in range(len(E_bit)):
        res+="".join(E_bit[i])
    return res



def P_box_pass(str):
    P_mat = [[16,7,20,21],[29,12,28,17],[1,15,23,26],[5,18,31,10],[2,8,24,14],[32,27,3,9],[19,13,30,6],[22,11,4,25]]
    for i in range(len(P_mat)):
        for j in range(len(P_mat[0])):
            P_mat[i][j] = str[P_mat[i][j]-1]
    res=''
    for i in range(len(P_mat)):
        res+="".join(P_mat[i])
    return res


def S_box_pass(str):
    
    str_6_arr = []
    for i in range(0,len(str),6):
        str_6_arr.append(str[i:i+6])
    
    S = S_box()
    S_out = ''
    # S_out must be of length 32bits
    for i in range(len(str_6_arr)):
        row = bin2dec(int(str_6_arr[i][0]+str_6_arr[i][5]))
        col = bin2dec(int(str_6_arr[i][1:5]))
        if len(dec2bin(S[i][row][col]))==0:
            S_out+='0000'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==1:
            S_out+='000'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==2:
            S_out+='00'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==3:
            S_out+='0'+dec2bin(S[i][row][col])
        else:
            S_out+=dec2bin(S[i][row][col])
    return S_out

# Using keygen output keys to get correct encryption
def cipherfunction(right_ini,key):
    E_bit = [[32,1,2,3,4,5],[4,5,6,7,8,9],[8,9,10,11,12,13],[12,13,14,15,16,17],[16,17,18,19,20,21],[20,21,22,23,24,25],[24,25,26,27,28,29],[28,29,30,31,32,1]]
    
    P_mat = [[16,7,20,21],[29,12,28,17],[1,15,23,26],[5,18,31,10],[2,8,24,14],[32,27,3,9],[19,13,30,6],[22,11,4,25]]
    
    left_d_48 = ''
    E_bit_mat = [[0 for i in range(6)] for j in range(8)]
    for i in range(len(E_bit)):
        for j in range(len(E_bit[0])):
            E_bit_mat[i][j] = right_ini[E_bit[i][j]-1]

    for i in range(len(E_bit_mat)):
        left_d_48+="".join(E_bit_mat[i])

    left_d_48 = str(left_d_48)
    key = str(key)
    
    xor_out = ''

    for i in range(len(left_d_48)):
        xor_out+=str(int(left_d_48[i])^int(key[i]))
    
    xor_out_6 = []
    for i in range(0,len(xor_out),6):
        xor_out_6.append(xor_out[i:i+6])
   
    S = S_box()
    S_out = ''
    # S_out must be of length 32bits
    for i in range(len(xor_out_6)):
        row = bin2dec(int(xor_out_6[i][0]+xor_out_6[i][5]))
        col = bin2dec(int(xor_out_6[i][1:5]))
        if len(dec2bin(S[i][row][col]))==0:
            S_out+='0000'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==1:
            S_out+='000'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==2:
            S_out+='00'+dec2bin(S[i][row][col])
        elif len(dec2bin(S[i][row][col]))==3:
            S_out+='0'+dec2bin(S[i][row][col])
        else:
            S_out+=dec2bin(S[i][row][col])

            
    final_S_out = ''
    for i in range(len(P_mat)):
        for j in range(len(P_mat[0])):
            final_S_out+=S_out[P_mat[i][j]-1]
            
    return final_S_out

def xor_out_str(left_ini,cipherfunction_out):
    xor_out = ''
    for i in range(len(left_ini)):
        xor_out+=str(int(left_ini[i])^int(cipherfunction_out[i]))
    return xor_out

def encryption(inp,key):
    left_ini = initialpermutation(inp)[0:32]
    right_ini = initialpermutation(inp)[32:64]
    left_iter = ''
    right_iter = ''
    for i in range(16):
        left_iter = right_ini
        right_iter = xor_out_str(left_ini,cipherfunction(right_ini,keygen(i,key)))
        left_ini = left_iter
        right_ini = right_iter
        
    return inversepermutation(right_iter+left_iter)

def decryption(inp,key):
    left_ini = initialpermutation(inp)[32:64]
    right_ini = initialpermutation(inp)[0:32]
    left_iter = ''
    right_iter = ''
    for i in range(16):
        right_iter = left_ini
        left_iter = xor_out_str(right_ini,cipherfunction(left_ini,keygen(15-i,key)))
        left_ini = left_iter
        right_ini = right_iter
    return inversepermutation(left_iter+right_iter)

    
def main():
    plaintext = '5AFE'*4
    plaintext_bin = hex2bin(plaintext)
    key = 'C0DE'*4
    key_bin = hex2bin(key)
    ciphertxt = bin2hex(encryption(hex2bin('5AFE'*4),hex2bin('C0DE'*4)))
    ciphertxt_bin = encryption(hex2bin('5AFE'*4),hex2bin('C0DE'*4))

    decrypted_txt = bin2hex(decryption(ciphertxt_bin,hex2bin('C0DE'*4)))
    decrypted_txt_bin = decryption(ciphertxt_bin,hex2bin('C0DE'*4))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Plaintext :' +plaintext)

    print('Key :' +key)

    print('Ciphertxt :' +ciphertxt)

    print('Decrypted_txt :' +decrypted_txt)
    
    print()
    if plaintext==decrypted_txt:
        print('DES Algorithm is working fine')
    else:
        print('DES Algorithm is not working.')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    for i in range(16):
        print('48 Bit SubKeys :' +bin2hex(keygen(i,hex2bin('C0DE'*4))))
        
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    print('E_box_input :' +bin2hex(hex2bin('ABABABAB')))
    print('E_box_output :' +bin2hex(E_bit_pass(hex2bin('ABABABAB'))))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    print('S_box_input :' +bin2hex(hex2bin('ABABABABABAB')))
    print('S_box_output :' +bin2hex(S_box_pass(hex2bin('ABABABABABAB'))))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    print('P_box_input :' +bin2hex(hex2bin('ABABABAB')))
    print('P_box_output :' +bin2hex(P_box_pass(hex2bin('ABABABAB'))))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    print('PC-1_input :' +bin2hex(hex2bin('C0DE'*4)))   
    print('PC-1_output :' +bin2hex(pc1_pass(hex2bin('C0DE'*4))))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    print('PC-2_input :' +bin2hex(hex2bin('C0C0C0C0C0C0C0C0')))
    print('PC-2_output :' +bin2hex(pc2_pass(hex2bin('C0C0C0C0C0C0C0C0'))))
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
main()