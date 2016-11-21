import socket

def leftrotate(x,c):
    return (x << c)&0xFFFFFFFF | (x >> (32-c)&0x7FFFFFFF>>(32-c))

def MD5Calculation(Listof32Bits):    #Helper function to calculate the Message Digest using the PseudoCode Provided.
    s = [0]*64    #Initially sets 0 64 times to the list s
    K = [0]*64    #Initially sets 0 64 times to the list K
    a,b,c,d = 7,12,17,22
    for j in range(0,16,4):
        s[j],s[j+1],s[j+2],s[j+3] = a,b,c,d
    a,b,c,d = 5,9,14,20
    for j in range(16,32,4):
        s[j],s[j+1],s[j+2],s[j+3] = a,b,c,d
    a,b,c,d = 4,11,16,23
    for j in range(32,48,4):
        s[j],s[j+1],s[j+2],s[j+3] = a,b,c,d
    a,b,c,d = 6,10,15,21
    for j in range(48,64,4):
        s[j],s[j+1],s[j+2],s[j+3] = a,b,c,d
    K[0],K[1],K[2],K[3]     = 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee 
    K[4],K[5],K[6],K[7]     = 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501 
    K[8],K[9],K[10],K[11]   = 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be 
    K[12],K[13],K[14],K[15] = 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821 
    K[16],K[17],K[18],K[19] = 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa 
    K[20],K[21],K[22],K[23] = 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8 
    K[24],K[25],K[26],K[27] = 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed 
    K[28],K[29],K[30],K[31] = 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a 
    K[32],K[33],K[34],K[35] = 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c 
    K[36],K[37],K[38],K[39] = 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70 
    K[40],K[41],K[42],K[43] = 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05
    K[44],K[45],K[46],K[47] = 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665 
    K[48],K[49],K[50],K[51] = 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039 
    K[52],K[53],K[54],K[55] = 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1 
    K[56],K[57],K[58],K[59] = 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1 
    K[60],K[61],K[62],K[63] = 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    A  = a0
    B  = b0
    C  = c0
    D  = d0
    for i in range(0,64):
        if i>=0 and i<=15:
            F = (B & C) | ((~B) & D)
            F = F & 0xFFFFFFFF
            g = i
        elif i>=16 and i<= 31:
            F = (D & B) | ((~D) & C)
            F = F & 0xFFFFFFFF
            g = ((5*i) + 1)%16
        elif i>=32 and i<=47:
            F = B ^ C ^ D
            F = F & 0xFFFFFFFF
            g = ((3*i) + 5)%16
        elif i>=48 and i<=63:          
            F = C ^ (B | (~D))
            F = F & 0xFFFFFFFF
            g = (7*i)%16
        dTemp = D
        D = C
        C = B
        B = B + leftrotate((A + F + K[i] + Listof32Bits[g]),s[i])
        B = B & 0xFFFFFFFF
        A = dTemp
    a0 = (a0 + A) & 0xFFFFFFFF
    b0 = (b0 + B) & 0xFFFFFFFF
    c0 = (c0 + C) & 0xFFFFFFFF
    d0 = (d0 + D) & 0xFFFFFFFF
    return str(a0)+str(b0)+str(c0)+str(d0)    #Message Digest

########## FILL IN THE FUNCTIONS TO IMPLEMENT THE CLIENT ##########
def StartConnection (IPAddress, PortNumber):
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.connect((str(IPAddress),int(PortNumber)))
    return connection

def login (s, username, password):
    s.send("LOGIN "+str(username)+"\n")
    reply = s.recv(512)
    reply.strip("\n\r")  #Removes the end line and end file character from the reply.
    challenge = reply.split()     #Takes the reply from the server and splits it to a list of strings
    Challenge = challenge[2]      #Takes the string at the second index as this is the challenge that the server sends.
    PasswordLength = len(password)        
    ChallengeLength = len(Challenge)
    message = password+Challenge     #string for the message
    Block = message+"1"         #We need to add the string "1" to the message in accordance with the pseudo code before adding zeros.
    for i in range(508-(PasswordLength+ChallengeLength)):
        Block += "0"                
    SizeofMessage = str(PasswordLength + ChallengeLength)   #Gets the size of the actual message.
    if len(SizeofMessage) == 1:                                    #  |
        SizeofMessage = "00" + SizeofMessage                       #  |
    elif len(SizeofMessage) == 2:                                  #  | Makes sure the string is exactly 3 characters long and adds the appropriate amount of zeros to satisfy this.
        SizeofMessage = "0" + SizeofMessage                        #  | 
    Block += SizeofMessage      #Adds to the block of the message
    SumOfASCII = 0     
    ListofChunks = []       #Holds the list of 32-bit strings of the block.
    StartPoint = 0
    EndPoint = 32                                
    for i in range(16):     
        for j in range(StartPoint,EndPoint):
            SumOfASCII += ord(Block[j])    #Gets the ASCII value of the element in Block at index j and adds it to SumOfASCII.
        ListofChunks += [SumOfASCII]     
        StartPoint = EndPoint   # |
        EndPoint += 32          # | Changes the StartPoint and EndPoint to a newer value to continue to other chunks
        SumOfASCII = 0
    result = MD5Calculation(ListofChunks)  #Retrieves the result from the MD5Calculation and stores the message digest in the result variable.
    LoginCommand = "LOGIN "+str(username)+" "+str(result)+"\n"      #Command to LOGIN to the SERVER.
    s.send(LoginCommand)
    Reply = s.recv(512)
    Result = Reply.split()
    if Result[1] == "Successful":
        return True
    else:
        return False
