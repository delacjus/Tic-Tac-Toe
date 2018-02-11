B=["a","b","c","d","e","f","g","h","i"]
#********
#* board*
#********
def TTTB():
    print " ____________________"                  "    "     " ____________________"
    print "|      |      |      |"                 "   "    "|      |      |      |" 
    print "| ",M[0],"  | ",M[1],"  | ",M[2],"  |"  "   "    "| ",B[0],"  | ",B[1],"  | ",B[2],"  |"   
    print "|______|______|______|"                 "   "    "|______|______|______|"
    print "|      |      |      |"                 "   "    "|      |      |      |"
    print "| ",M[3],"  | ",M[4],"  | ",M[5],"  |"  "   "    "| ",B[3],"  | ",B[4],"  | ",B[5],"  |"
    print "|______|______|______|"                 "   "    "|______|______|______|"
    print "|      |      |      |"                 "   "    "|      |      |      |"
    print "| ",M[6],"  | ",M[7],"  | ",M[8],"  |"  "   "    "| ",B[6],"  | ",B[7],"  | ",B[8],"  |"
    print "|______|______|______|"                 "   "    "|______|______|______|"   
#******************************************
#* Make sure they pick a valid place to go*
#******************************************
def Turn(who):
    while 1>0:
        choice=raw_input("Enter a position-->")
        if choice=="a":
            if M[0]=="X" or M[0]=="O":
                print "Invalid Choice"
            else:
                M[0]=who
                break
        if choice=="b":
            if M[1]=="X" or M[1]=="O":
                print "Invalid Choice"
            else:
                M[1]=who
                break
        if choice=="c":
            if M[2]=="X" or M[2]=="O":
                print "Invalid Choice"
            else:
                M[2]=who
                break
        if choice=="d":
            if M[3]=="X" or M[3]=="O":
                print "Invalid Choice"
            else:
                M[3]=who
                break
        if choice=="e":
            if M[4]=="X" or M[4]=="O":
                print "Invalid Choice"
            else:
                M[4]=who
                break
        if choice=="f":
            if M[5]=="X" or M[5]=="O":
                print "Invalid Choice"
            else:
                M[5]=who
                break
        if choice=="g":
            if M[6]=="X" or M[6]=="O":
                print "Invalid Choice"
            else:
                M[6]=who
                break
        if choice=="h":
            if M[7]=="X" or M[7]=="O":
                print "Invalid Choice"
            else:
                M[7]=who
                break
        if choice=="i":
            if M[8]=="X" or M[8]=="O":
                print "Invalid Choice"
            else:
                M[8]=who
                break
        if  (M[0]!="X" or M[0]!="O")\
            and (M[1]!="X" or M[1]!="O")\
            and (M[2]!="X" or M[2]!="O")\
            and (M[3]!="X" or M[3]!="O")\
            and (M[4]!="X" or M[4]!="O")\
            and (M[5]!="X" or M[5]!="O")\
            and (M[6]!="X" or M[6]!="O")\
            and (M[7]!="X" or M[7]!="O")\
            and (M[8]!="X" or M[8]!="O"):
                print "Invalid Choice"
#************************************************
#* The AI looks in every place to see were to go*
#************************************************
def AI_move(AIwho,who):
    import random
    print "I am Thinking"
    import time
    Timer=random.randint(2,4)
    time.sleep(Timer)
    ix=0
    if M[0]==AIwho:
        if M[1]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[3]==AIwho:
        if M[4]==AIwho:
            if M[5]!="X" and M[5]!="O":
                if ix==0:
                    M[5]=AIwho
                    ix=1
    if M[6]==AIwho:
        if M[7]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[0]==AIwho:
        if M[3]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[1]==AIwho:
        if M[4]==AIwho:
            if M[7]!="X" and M[7]!="O":
                if ix==0:
                    M[7]=AIwho
                    ix=1
    if M[2]==AIwho:
        if M[5]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[0]==AIwho:
        if M[4]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[2]==AIwho:
        if M[4]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[2]==AIwho:
        if M[1]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[5]==AIwho:
        if M[4]==AIwho:
            if M[3]!="X" and M[3]!="O":
                if ix==0:
                    M[3]=AIwho
                    ix=1
    if M[8]==AIwho:
        if M[7]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[6]==AIwho:
        if M[3]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[7]==AIwho:
        if M[4]==AIwho:
            if M[1]!="X" and M[1]!="O":
                if ix==0:
                    M[1]=AIwho
                    ix=1
    if M[8]==AIwho:
        if M[5]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[8]==AIwho:
        if M[4]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[6]==AIwho:
        if M[4]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[1]==AIwho:
        if M[0]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[3]==AIwho:
            if M[5]!="X" and M[5]!="O":
                if ix==0:
                    M[5]=AIwho
                    ix=1
    if M[7]==AIwho:
        if M[6]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[3]==AIwho:
        if M[0]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[1]==AIwho:
            if M[7]!="X" and M[7]!="O":
                if ix==0:
                    M[7]=AIwho
                    ix=1
    if M[5]==AIwho:
        if M[2]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[0]==AIwho:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[2]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[1]==AIwho:
        if M[2]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[5]==AIwho:
            if M[3]!="X" and M[3]!="O":
                if ix==0:
                    M[3]=AIwho
                    ix=1
    if M[7]==AIwho:
        if M[8]==AIwho:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[3]==AIwho:
        if M[6]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[7]==AIwho:
            if M[1]!="X" and M[1]!="O":
                if ix==0:
                    M[1]=AIwho
                    ix=1
    if M[5]==AIwho:
        if M[8]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[8]==AIwho:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==AIwho:
        if M[6]==AIwho:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[0]==who:
        if M[1]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[3]==who:
        if M[4]==who:
            if M[5]!="X" and M[5]!="O":
                if ix==0:
                    M[5]=AIwho
                    ix=1
    if M[6]==who:
        if M[7]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[0]==who:
        if M[3]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[1]==who:
        if M[4]==who:
            if M[7]!="X" and M[7]!="O":
                if ix==0:
                    M[7]=AIwho
                    ix=1
    if M[2]==who:
        if M[5]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[0]==who:
        if M[4]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[2]==who:
        if M[4]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1


    if M[2]==who:
        if M[1]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[5]==who:
        if M[4]==who:
            if M[3]!="X" and M[3]!="O":
                if ix==0:
                    M[3]=AIwho
                    ix=1
    if M[8]==who:
        if M[7]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[6]==who:
        if M[3]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[7]==who:
        if M[4]==who:
            if M[1]!="X" and M[1]!="O":
                if ix==0:
                    M[1]=AIwho
                    ix=1
    if M[8]==who:
        if M[5]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[8]==who:
        if M[4]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[6]==who:
        if M[4]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1


    if M[1]==who:
        if M[0]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[4]==who:
        if M[3]==who:
            if M[5]!="X" and M[5]!="O":
                if ix==0:
                    M[5]=AIwho
                    ix=1
    if M[7]==who:
        if M[6]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[3]==who:
        if M[0]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[4]==who:
        if M[1]==who:
            if M[7]!="X" and M[7]!="O":
                if ix==0:
                    M[7]=AIwho
                    ix=1
    if M[5]==who:
        if M[2]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[4]==who:
        if M[0]==who:
            if M[8]!="X" and M[8]!="O":
                if ix==0:
                    M[8]=AIwho
                    ix=1
    if M[4]==who:
        if M[2]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1


    if M[1]==who:
        if M[2]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==who:
        if M[5]==who:
            if M[3]!="X" and M[3]!="O":
                if ix==0:
                    M[3]=AIwho
                    ix=1
    if M[7]==who:
        if M[8]==who:
            if M[6]!="X" and M[6]!="O":
                if ix==0:
                    M[6]=AIwho
                    ix=1
    if M[3]==who:
        if M[6]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==who:
        if M[7]==who:
            if M[1]!="X" and M[1]!="O":
                if ix==0:
                    M[1]=AIwho
                    ix=1
    if M[5]==who:
        if M[8]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    if M[4]==who:
        if M[8]==who:
            if M[0]!="X" and M[0]!="O":
                if ix==0:
                    M[0]=AIwho
                    ix=1
    if M[4]==who:
        if M[6]==who:
            if M[2]!="X" and M[2]!="O":
                if ix==0:
                    M[2]=AIwho
                    ix=1
    
    if ix==0:
        while 1>0:
            AI=random.randint(0,8)
            if M[AI]!="X" and M[AI]!="O":
                M[AI]=AIwho
                break
#*************************
#* sees if 3 are in a row*
#*************************
def Winner(who):
    Win=0
    if M[0]==who:
        if M[1]==who:
            if M[2]==who:
                Win=1
                print "You Win"
    if M[3]==who:
        if M[4]==who:
            if M[5]==who:
                Win=1
                print "You Win"
    if M[6]==who:
        if M[7]==who:
            if M[8]==who:
                Win=1
                print "You Win"
    if M[0]==who:
            if M[3]==who:
                if M[6]==who:
                    Win=1
                    print "You Win"
    if M[1]==who:
        if M[4]==who:
            if M[7]==who:
                Win=1
                print "You Win"
    if M[2]==who:
        if M[5]==who:
            if M[8]==who:
                Win=1
                print "You Win"
    if M[0]==who:
        if M[4]==who:
            if M[8]==who:
                Win=1
                print "You Win"
    if M[2]==who:
        if M[4]==who:
            if M[6]==who:
                Win=1
                print "You Win"
    return Win
#************************************
#* sees if 3 of the IA's is in a row*
#************************************
def loser(AIwho):
    Lose=0
    if M[0]==AIwho: 
        if M[1]==AIwho:
            if M[2]==AIwho:
                Lose=1
                print "You Lose"
    if M[3]==AIwho:
        if M[4]==AIwho:
            if M[5]==AIwho:
                Lose=1
                print "You Lose"
    if M[6]==AIwho:
        if M[7]==AIwho:
            if M[8]==AIwho:
                Lose=1
                print "You Lose"
    if M[0]==AIwho:
        if M[3]==AIwho:
            if M[6]==AIwho:
                Lose=1
                print "You Lose"
    if M[1]==AIwho:
        if M[4]==AIwho:
            if M[7]==AIwho:
                Lose=1
                print "You Lose"
    if M[2]==AIwho:
        if M[5]==AIwho:
            if M[8]==AIwho:
                Lose=1
                print "You Lose"
    if M[0]==AIwho:
        if M[4]==AIwho:
            if M[8]==AIwho:
                Lose=1
                print "You Lose"
    if M[2]==AIwho:
        if M[4]==AIwho:
            if M[6]==AIwho:
                Lose=1
                print "You Lose"
    return Lose
#****************************************
#* if the board is full the game is Tied*
#****************************************
def Tied():
    if  (M[0]=="X" or M[0]=="O")\
    and (M[1]=="X" or M[1]=="O")\
    and (M[2]=="X" or M[2]=="O")\
    and (M[3]=="X" or M[3]=="O")\
    and (M[4]=="X" or M[4]=="O")\
    and (M[5]=="X" or M[5]=="O")\
    and (M[6]=="X" or M[6]=="O")\
    and (M[7]=="X" or M[7]=="O")\
    and (M[8]=="X" or M[8]=="O"):
        print "We have a Tied Game"
        Done=1
        return Done
#*******************
#* resets the moves*
#*******************
def reset():
    global M
    M=[" "," "," "," "," "," "," "," "," "]
#************************************************
#* easy IA [ramdom moves*
#************************************************
def AIE(AIwho,who):
    import random
    print "I am Thinking"
    import time
    Timer=random.randint(2,4)
    time.sleep(Timer)           
    while 1>0:
        AI=random.randint(0,8)
        if M[AI]!="X" and M[AI]!="O":
            M[AI]=AIwho
            break 
