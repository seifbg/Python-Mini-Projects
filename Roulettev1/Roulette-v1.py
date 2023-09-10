import random

black=[15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]               #This is a list of all black numbers
red=[32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]              #List of red numbers
green=[0]                     #Green List


def deposit():               #Deposit function
    while True:
        try:
            x=float(input("The amount to deposit: "))                  #The input declared as float
            if(x<10):
                print("The amount should be superior to 10$")              #The minimum deposit must be superior to 10
            else:
                break
        except ValueError:
            print("Input Error!")      #Error
    return x
def inputnumber():            #Number input function
    n=0
    while (n==0):
        try:
            x=int(input("Choose a number: "))
            if ((x < 0) or (x > 36)):                   #The number provided must be between 0 & 36.
                n = 0
                print("You need to choose a number between 0 and 36!")
            else:
                break
        except ValueError:
            print("Input Error!")
    return x
def bet():                  #Bet Input function
    while True:
        try:
            y=float(input("Input the amount you wish to bet with (in Dollars): "))
            if(y>0):
                break
            else:
                print("The bet amount should be superior to 0$.")                #The bet amount must be superior to 0
        except ValueError:
            print("Verify the amount provided!")
    return y
n=0
amount = deposit()
while(amount>0):                     #The game continues while amount superior to 0
    continue_party=False
    while continue_party==False:
        try:
            num = inputnumber()
            r=int(input("Continue? (1 for Yes | Another number for No)."))
            if (r==1):
                print("Okay, lets continue")
                continue_party==True
                break
            elif (r>=0):
                print("Okay, lets go back.")
                continue_party==False
        except ValueError:
            print("Error")
    while continue_party==False:
        try:
            while(n==0):
                    betnum = bet()
                    if(betnum>amount):
                        print("Insufficient Balance!")                    #If the amount provided is less than the balance it returns a message.
                        n=0
                    elif(betnum<=amount):
                        break
            r=int(input("Continue? (1 for oui | Another number for No)."))
            if (r==1):
                print("Okay, lets continue.")
                continue_party==True
                break
            elif (r>=0):
                print("Okay, lets go back.")
                continue_party==False
        except ValueError:
            print("Input Error!")

    print("The game has started, we throw the ball.......")                 #The game starts
    rand=random.randint(0,37)                    #Random function pre-defined it rolls a number between 0 and 36.
    if(rand in red):
        color=1
    elif(rand in black):
        color=2
    elif(rand in green):
        color=3
    print("The roulette stopped, the ball stopped on number:  ",rand)              #Pops a message with random number.
    if(num in red):
        color2=1
    elif(num in black):
        color2=2
    elif(num in green):
        color2=3
    if(num==rand):               #In case the number choosen is the same as the random one the player wins (3x the bet amount)
        amount=amount+3*betnum
        print("WINNER! (3x)")
        print("You have now ",amount,"$ !")
    elif (color==color2):                       #In case the number has the same color as the random number the player wins 50% of the bet amount.
        amount=amount+(betnum/2)
        print("WINNER! (50% same color)")
        print("You have now ",amount,"$ !")
    elif (color==color2):                  #In case the number choosen is 0 and the random one is 0 the player wins 36x the bet amount.
        amount=amount+(betnum*36)
    else:                 #If none of the above is presented then the player loses and the bet amount is substracted from his balance.
        amount=amount-betnum
        print("LOST!")
        print("You have now ",amount,"$ !")
