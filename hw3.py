import numpy as np
plaintext = input('Enter a plaintext in Hexadecimal:')
key = input('Enter a key in Hexadecimal:')
#明文 16進位轉10進位轉2進位
plaintext = bin(int(plaintext,16))
key = bin(int(key,16))
plaintext = plaintext[2:]
key = key[2:]
plaintext = plaintext.zfill(64)
key = key.zfill(64)
#initial permutation
new_plaintext = ""
#key:舊位子 value:新位子
IP_inverse = {58:0, 50:1, 42:2, 34:3, 26:4, 18:5, 10:6, 2:7,
      60:8, 52:9, 44:10, 36:11, 28:12, 20:13, 12:14, 4:15,
      62:16, 54:17, 46:18, 38:19, 30:20, 22:21, 14:22, 6:23,
      64:24, 56:25, 48:26, 40:27, 32:28, 24:29, 16:30, 8:31,
      57:32, 49:33, 41:34, 33:35, 25:36, 17:37, 9:38, 1:39,
      59:40, 51:41, 43:42, 35:43, 27:44, 19:45, 11:46, 3:47,
      61:48, 53:49, 45:50, 37:51, 29:52, 21:53, 13:54, 5:55,
      63:56, 55:57, 47:58, 39:59, 31:60, 23:61, 15:62, 7:63} 
IP = dict((k, v) for v, k in IP_inverse.items()) #key跟value反過來
for i in range(64):
    new_plaintext = new_plaintext + plaintext[IP.get(i)-1]
#print('initial_P:',new_plaintext)

#key:擴展後的位子 value:要放第幾個bit
E = {1:32, 2:1, 3:2, 4:3, 5:4, 6:5, 
     7:4, 8:5, 9:6, 10:7, 11:8, 12:9, 
     13:8, 14:9, 15:10, 16:11, 17:12, 18:13, 
     19:12, 20:13, 21:14, 22:15, 23:16, 24:17,
     25:16, 26:17, 27:18, 28:19, 29:20, 30:21,
     31:20, 32:21, 33:22, 34:23, 35:24, 36:25,
     37:24, 38:25, 39:26, 40:27, 41:28, 42:29,
     43:28, 44:29, 45:30, 46:31, 47:32, 48:1}

PC_1 = {1:57, 2:49, 3:41, 4:33, 5:25, 6:17, 7:9,
       8:1, 9:58, 10:50, 11:42, 12:34, 13:26, 14:18,
       15:10, 16:2, 17:59, 18:51, 19:43, 20:35, 21:27,
       22:19, 23:11, 24:3, 25:60, 26:52, 27:44, 28:36,
       29:63, 30:55, 31:47, 32:39, 33:31, 34:23, 35:15,
       36:7, 37:62, 38:54, 39:46, 40:38, 41:30, 42:22,
       43:14, 44:6, 45:61, 46:53, 47:45, 48:37, 49:29,
       50:21, 51:13, 52:5, 53:28, 54:20, 55:12, 56:4}
PC_2 = {1:14, 2:17, 3:11, 4:24, 5:1, 6:5,
       7:3, 8:28, 9:15, 10:6, 11:21, 12:10,
       13:23, 14:19, 15:12, 16:4, 17:26, 18:8,
       19:16, 20:7, 21:27, 22:20, 23:13, 24:2,
       25:41, 26:52, 27:31, 28:37, 29:47, 30:55,
       31:30, 32:40, 33:51, 34:45, 35:33, 36:48,
       37:44, 38:49, 39:39, 40:56, 41:34, 42:53,
       43:46, 44:42, 45:50, 46:36, 47:29, 48:32}

S1 = {0:'14', 1:'4', 2:'13', 3:'1', 4:'2', 5:'15', 6:'11', 7:'8', 8:'3', 9:'10', 10:'6', 11:'12', 12:'5', 13:'9', 14:'0', 15:'7',
      16:'0', 17:'15', 18:'7', 19:'4', 20:'14', 21:'2', 22:'13', 23:'1', 24:'10', 25:'6', 26:'12', 27:'11', 28:'9', 29:'5', 30:'3', 31:'8',
      32:'4', 33:'1', 34:'14', 35:'8', 36:'13', 37:'6', 38:'2', 39:'11', 40:'15', 41:'12', 42:'9', 43:'7', 44:'3', 45:'10', 46:'5', 47:'0', 
      48:'15', 49:'12', 50:'8', 51:'2', 52:'4', 53:'9', 54:'1', 55:'7', 56:'5', 57:'11', 58:'3', 59:'14', 60:'10', 61:'0', 62:'6', 63:'13'}

S2 = {0:'15', 1:'1', 2:'8', 3:'14', 4:'6', 5:'11', 6:'3', 7:'4', 8:'9', 9:'7', 10:'2', 11:'13', 12:'12', 13:'0', 14:'5', 15:'10',
      16:'3', 17:'13', 18:'4', 19:'7', 20:'15', 21:'2', 22:'8', 23:'14', 24:'12', 25:'0', 26:'1', 27:'10', 28:'6', 29:'9', 30:'11', 31:'5',
      32:'0', 33:'14', 34:'7', 35:'11', 36:'10', 37:'4', 38:'13', 39:'1', 40:'5', 41:'8', 42:'12', 43:'6', 44:'9', 45:'3', 46:'2', 47:'15', 
      48:'13', 49:'8', 50:'10', 51:'1', 52:'3', 53:'15', 54:'4', 55:'2', 56:'11', 57:'6', 58:'7', 59:'12', 60:'0', 61:'5', 62:'14', 63:'9'}

S3 = {0:'10', 1:'0', 2:'9', 3:'14', 4:'6', 5:'3', 6:'15', 7:'5', 8:'1', 9:'13', 10:'12', 11:'7', 12:'11', 13:'4', 14:'2', 15:'8',
      16:'13', 17:'7', 18:'0', 19:'9', 20:'3', 21:'4', 22:'6', 23:'10', 24:'2', 25:'8', 26:'5', 27:'14', 28:'12', 29:'11', 30:'15', 31:'1',
      32:'13', 33:'6', 34:'4', 35:'9', 36:'8', 37:'15', 38:'3', 39:'0', 40:'11', 41:'1', 42:'2', 43:'12', 44:'5', 45:'10', 46:'14', 47:'7', 
      48:'1', 49:'10', 50:'13', 51:'0', 52:'6', 53:'9', 54:'8', 55:'7', 56:'4', 57:'15', 58:'14', 59:'3', 60:'11', 61:'5', 62:'2', 63:'12'}

S4 = {0:'7', 1:'13', 2:'14', 3:'3', 4:'0', 5:'6', 6:'9', 7:'10', 8:'1', 9:'2', 10:'8', 11:'5', 12:'11', 13:'12', 14:'4', 15:'15',
      16:'13', 17:'8', 18:'11', 19:'5', 20:'6', 21:'15', 22:'0', 23:'3', 24:'4', 25:'7', 26:'2', 27:'12', 28:'1', 29:'10', 30:'14', 31:'9',
      32:'10', 33:'6', 34:'9', 35:'0', 36:'12', 37:'11', 38:'7', 39:'13', 40:'15', 41:'1', 42:'3', 43:'14', 44:'5', 45:'2', 46:'8', 47:'4', 
      48:'3', 49:'15', 50:'0', 51:'6', 52:'10', 53:'1', 54:'13', 55:'8', 56:'9', 57:'4', 58:'5', 59:'11', 60:'12', 61:'7', 62:'2', 63:'14'}

S5 = {0:'2', 1:'12', 2:'4', 3:'1', 4:'7', 5:'10', 6:'11', 7:'6', 8:'8', 9:'5', 10:'3', 11:'15', 12:'13', 13:'0', 14:'14', 15:'9',
      16:'14', 17:'11', 18:'2', 19:'12', 20:'4', 21:'7', 22:'13', 23:'1', 24:'5', 25:'0', 26:'15', 27:'10', 28:'3', 29:'9', 30:'8', 31:'6',
      32:'4', 33:'2', 34:'1', 35:'11', 36:'10', 37:'13', 38:'7', 39:'8', 40:'15', 41:'9', 42:'12', 43:'5', 44:'6', 45:'3', 46:'0', 47:'14', 
      48:'11', 49:'8', 50:'12', 51:'7', 52:'1', 53:'14', 54:'2', 55:'13', 56:'6', 57:'15', 58:'0', 59:'9', 60:'10', 61:'4', 62:'5', 63:'3'}

S6 = {0:'12', 1:'1', 2:'10', 3:'15', 4:'9', 5:'2', 6:'6', 7:'8', 8:'0', 9:'13', 10:'3', 11:'4', 12:'14', 13:'7', 14:'5', 15:'11',
      16:'10', 17:'15', 18:'4', 19:'2', 20:'7', 21:'12', 22:'9', 23:'5', 24:'6', 25:'1', 26:'13', 27:'14', 28:'0', 29:'11', 30:'3', 31:'8',
      32:'9', 33:'14', 34:'15', 35:'5', 36:'2', 37:'8', 38:'12', 39:'3', 40:'7', 41:'0', 42:'4', 43:'10', 44:'1', 45:'13', 46:'11', 47:'6', 
      48:'4', 49:'3', 50:'2', 51:'12', 52:'9', 53:'5', 54:'15', 55:'10', 56:'11', 57:'14', 58:'1', 59:'7', 60:'6', 61:'0', 62:'8', 63:'13'}

S7 = {0:'4', 1:'11', 2:'2', 3:'14', 4:'15', 5:'0', 6:'8', 7:'13', 8:'3', 9:'12', 10:'9', 11:'7', 12:'5', 13:'10', 14:'6', 15:'1',
      16:'13', 17:'0', 18:'11', 19:'7', 20:'4', 21:'9', 22:'1', 23:'10', 24:'14', 25:'3', 26:'5', 27:'12', 28:'2', 29:'15', 30:'8', 31:'6',
      32:'1', 33:'4', 34:'11', 35:'13', 36:'12', 37:'3', 38:'7', 39:'14', 40:'10', 41:'15', 42:'6', 43:'8', 44:'0', 45:'5', 46:'9', 47:'2', 
      48:'6', 49:'11', 50:'13', 51:'8', 52:'1', 53:'4', 54:'10', 55:'7', 56:'9', 57:'5', 58:'0', 59:'15', 60:'14', 61:'2', 62:'3', 63:'12'}

S8 = {0:'13', 1:'2', 2:'8', 3:'4', 4:'6', 5:'15', 6:'11', 7:'1', 8:'10', 9:'9', 10:'3', 11:'14', 12:'5', 13:'0', 14:'12', 15:'7',
      16:'1', 17:'15', 18:'13', 19:'8', 20:'10', 21:'3', 22:'7', 23:'4', 24:'12', 25:'5', 26:'6', 27:'11', 28:'0', 29:'14', 30:'9', 31:'2',
      32:'7', 33:'11', 34:'4', 35:'1', 36:'9', 37:'12', 38:'14', 39:'2', 40:'0', 41:'6', 42:'10', 43:'13', 44:'15', 45:'3', 46:'5', 47:'8', 
      48:'2', 49:'1', 50:'14', 51:'7', 52:'4', 53:'10', 54:'8', 55:'13', 56:'15', 57:'12', 58:'9', 59:'0', 60:'3', 61:'5', 62:'6', 63:'11'}

P = {1:16, 2:7, 3:20, 4:21, 5:29, 6:12, 7:28, 8:17,
     9:1, 10:15, 11:23, 12:26, 13:5, 14:18, 15:31, 16:10,
     17:2, 18:8, 19:24, 20:14, 21:32, 22:27, 23:3, 24:9,
     25:19, 26:13, 27:30, 28:6, 29:22, 30:11, 31:4, 32:25}

key_PC1 = ""
for i in range(56):
    key_PC1 = key_PC1 + key[PC_1.get(i+1)-1]
#print(key_PC1)

L = new_plaintext[:32]  #L0
R = new_plaintext[32:]  #R0
new_L = ""
new_R = ""
C = key_PC1[:28]    #C0
D = key_PC1[28:]    #D0
new_C = ""  #做完rotation的C
new_D = ""  #做完rotation的D
new_CD = "" #newC newD combine
S1_R = ""   #還沒經過S1的6bit二進位string
S2_R = ""
S3_R = ""
S4_R = ""
S5_R = ""   
S6_R = ""
S7_R = ""
S8_R = ""
new_S1_R = ""   #經過S1後的4bit二進位string
new_S2_R = ""
new_S3_R = ""
new_S4_R = ""
new_S5_R = ""   
new_S6_R = ""
new_S7_R = ""
new_S8_R = ""
Sbox_R = ""
for round in range(16):
    new_L = R

    #Expansion E
    Exception_R = ""
    for i in range(48):
        Exception_R = Exception_R + R[E.get(i+1)-1]
    #print(Exception_R)

    #Transform
    if (round == 0) or (round == 1) or (round == 8) or (round == 15):
        new_C = C[1:] + C[0]
        new_D = D[1:] + D[0]
    else:
        new_C = C[2:] + C[0] + C[1]
        new_D = D[2:] + D[0] + D[1]
    
    new_CD = new_C + new_D
    #PC-2
    new_key = ""  #每一輪transform新產生出的key
    for i in range(48):
        new_key = new_key + new_CD[PC_2.get(i+1)-1]
    #keylist = hex(int(new_key,2))
    #print(keylist[2:])
    #f_fuction
    #Exception_R XOR new_key
    XOR_R = ""  #Exception_R XOR new_key的結果
    for i in range(48):
        if new_key[i] == Exception_R[i]:
            XOR_R = XOR_R + '0'
        else:
            XOR_R = XOR_R + '1'
    
    #S-box
    #做好XOR後 6bit為一組
    S1_R = XOR_R[:6]
    S2_R = XOR_R[6:12]
    S3_R = XOR_R[12:18]
    S4_R = XOR_R[18:24]
    S5_R = XOR_R[24:30]
    S6_R = XOR_R[30:36]
    S7_R = XOR_R[36:42]
    S8_R = XOR_R[42:48]
    #S1
    row = int(S1_R[0] + S1_R[5],2)
    column = int(S1_R[1:5],2)
    index = row * 16 + column
    new_S1_R = S1.get(index)
    new_S1_R = str(bin(int(new_S1_R)))
    new_S1_R = new_S1_R[2:]
    new_S1_R = new_S1_R.zfill(4)
    #S2
    row = int(S2_R[0] + S2_R[5],2)
    column = int(S2_R[1:5],2)
    index = row * 16 + column
    new_S2_R = S2.get(index)
    new_S2_R = str(bin(int(new_S2_R)))
    new_S2_R = new_S2_R[2:]
    new_S2_R = new_S2_R.zfill(4)
    #S3
    row = int(S3_R[0] + S3_R[5],2)
    column = int(S3_R[1:5],2)
    index = row * 16 + column
    new_S3_R = S3.get(index)
    new_S3_R = str(bin(int(new_S3_R)))
    new_S3_R = new_S3_R[2:]
    new_S3_R = new_S3_R.zfill(4)
    #S4
    row = int(S4_R[0] + S4_R[5],2)
    column = int(S4_R[1:5],2)
    index = row * 16 + column
    new_S4_R = S4.get(index)
    new_S4_R = str(bin(int(new_S4_R)))
    new_S4_R = new_S4_R[2:]
    new_S4_R = new_S4_R.zfill(4)
    #S5
    row = int(S5_R[0] + S5_R[5],2)
    column = int(S5_R[1:5],2)
    index = row * 16 + column
    new_S5_R = S5.get(index)
    new_S5_R = str(bin(int(new_S5_R)))
    new_S5_R = new_S5_R[2:]
    new_S5_R = new_S5_R.zfill(4)
    #S6
    row = int(S6_R[0] + S6_R[5],2)
    column = int(S6_R[1:5],2)
    index = row * 16 + column
    new_S6_R = S6.get(index)
    new_S6_R = str(bin(int(new_S6_R)))
    new_S6_R = new_S6_R[2:]
    new_S6_R = new_S6_R.zfill(4)
    #S7
    row = int(S7_R[0] + S7_R[5],2)
    column = int(S7_R[1:5],2)
    index = row * 16 + column
    new_S7_R = S7.get(index)
    new_S7_R = str(bin(int(new_S7_R)))
    new_S7_R = new_S7_R[2:]
    new_S7_R = new_S7_R.zfill(4)
    #S8
    row = int(S8_R[0] + S8_R[5],2)
    column = int(S8_R[1:5],2)
    index = row * 16 + column
    new_S8_R = S8.get(index)
    new_S8_R = str(bin(int(new_S8_R)))
    new_S8_R = new_S8_R[2:]
    new_S8_R = new_S8_R.zfill(4)
    Sbox_R = new_S1_R + new_S2_R + new_S3_R + new_S4_R + new_S5_R + new_S6_R + new_S7_R + new_S8_R
    
    #Sbox_list = hex(int(Sbox_R,2))
    #print(Sbox_list[2:])

    #Permutation
    Permutation_R = ""  #經過每個round最後一步驟(Permutation)後的R
    for i in range(32):
        Permutation_R = Permutation_R + Sbox_R[P.get(i+1)-1]
    
    #L XOR Permutation_R 完，再放到new_R
    new_R = ""
    for i in range(32):
        if L[i] == Permutation_R[i]:
            new_R = new_R + '0'
        else:
            new_R = new_R + '1'
    
    #為下一round準備要使用的變數
    R = new_R
    L = new_L
    C = new_C
    D = new_D   

#new_R前段跟後段交換，再使用Final Permutation，產生密文
DES_plaintext = R + L
#final Permutation
ciphertext = ""
for i in range(64):
    ciphertext = ciphertext + DES_plaintext[IP_inverse.get(i+1)]
ciphertext = hex(int(ciphertext,2))
ciphertext = ciphertext[2:]
result = ""
for i in range(len(ciphertext)):
    if(ord(ciphertext[i]) >= 97) and (ord(ciphertext[i]) <= 122):
        result = result + chr(ord(ciphertext[i])-32)
    else:
        result = result + ciphertext[i]
print('ciphertext:', result)