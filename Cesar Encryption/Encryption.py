alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']                                #The english alphabet list.

def inputMessage():                                                    #Input Function, the user can enter the message to be encrypted later on.
    v=1
    while v==1:
        try:
            x=input("Input the message to encrypt (Either in lowercase or uppercase else it won't be crypted): ")
            for i in range(len(x)):                                        #This is a loop created to verify that the input is actually a message that contains no number or special characters.
                    if ((x[i].upper() in alphabet) or (x[i]==' ')):
                        v=0
                        break
                    else:
                        v=1
        except ValueError:
            print("Input Error!")
    return x

def encryption(x):                                            #This is the big part where the Cesar Encryption is made. This is a function created that has the Cesar Algorithm inside.
    nc=''
    space = ''
    for i in range(len(x)):
        if (x[i]==' '):                                      #Here we are saying that spaces are not considered to be encrypted so it stays a space.
            space=' '
            nc=nc+space
        else:
            n=(alphabet.index(x[i].upper())-3)%26                    #All of the above in here is the encryption of the letters. We substitue 3 from the index of the letter in Alphabet List then we use the modulo operator
            nc=nc+alphabet[n]                                       #to get a final number which is the index of the new letter.
            if(n>26):
                n=n-26                                      #If the new index is superior to 26 which is the number of the alphabet letters then we need to substract 26 from it.
            elif (n<0):                                    #else if it is a negative number we need to add 26 to it.
                n=n+26
    return nc





exit='f'
while (exit=='f'):                               #This is a loop, if the user enters the letter f at the end then the loop will break as you can see in line 48, any other letter will lead to a restart of the program as you can see in line 40.
    x=inputMessage()

    if(x.islower()):                                  #This is a condition where if the message written in lowercase then we need to print the new encrypted message in lowercase.
        print(encryption(x).lower())
    elif(x.isupper()):
        print(encryption(x).upper())                    #Same goes here for the uppercase.
    exit=input("Input any letter other than f to exit.")
    if (exit!='f'):
        print("Good bye!")
        break
