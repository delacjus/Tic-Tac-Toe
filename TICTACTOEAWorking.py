while 1>0:
    from TTTfunA import TTTB
    from TTTfunA import Turn
    from TTTfunA import AI_move
    from TTTfunA import Winner
    from TTTfunA import loser
    from TTTfunA import Tied
    from TTTfunA import reset
    from TTTfunA import AIE
    reset()
    TTTB()
    #****************************************
    #* Asks if the player wants to be X or O*
    #****************************************
    while 1>0:
        who=raw_input("Would you like to be X or O -->")
        if who=="X" or who=="O" or who=="x" or who=="o":
            break
        if who!="X" or who!="O" or who!="x" or who!="o":
            print
            print "Invalid Choice"
            print
    if who=="X" or who=="x":
        print "You are now X"
        AIwho="O"
    if who=="O" or who=="o":
        print "You are now O"
        AIwho="X"
    if who=="x":
        who="X"
    if who=="o":
        who="O"
    first="0"
    second="0"
    idx=0
    #*******************************
    #* Ask if they want to go first*
    #*******************************
    while idx<2:
        when=raw_input("Would you like to go first 'Y/N'-->")
        if when=="yes" or when=="Yes" or when=="YES" or when=="Y" or when=="y":
            first="1"
            idx=3
            break
        if when=="no" or when=="No" or when=="NO" or when=="N" or when=="n":
            second="1"
            idx=3
            break
        if when!="yes" or when!="Yes" or when!="YES" or when!="no" or when!="No" or when!="NO" or when=="Y" or when=="y" or when=="N" or when=="n":
            print
            print "Invalid Choice"
            print
    idx=0
    #************************************************
    #* Asks if they want it Hard or easy*
    #************************************************
    while idx<2:
        dif=raw_input("Would you like to play on Easy or Hard 'E/H'-->")
        if dif=="easy" or dif=="Easy" or dif=="EASY" or dif=="E" or dif=="e":
            difc="0"
            idx=3
            break
        if dif=="hard" or dif=="Hard" or dif=="HARD" or dif=="H" or dif=="h":
            difc="1"
            idx=3
            break
        if dif!="hard" or dif!="Hard" or dif!="HARD" or dif!="H" or dif!="h" or dif!="easy" or dif!="Easy" or dif!="EASY" or dif!="E" or dif!="e":
            print
            print "Invalid Choice"
            print
    #************************
    #* player plays the game*
    #************************
    TTTB()
    idx1=0
    while 1>0:
        if first=="1":
            Turn(who)
            TTTB()
        Done=Tied()
        Win=Winner(who)
        Lose=loser(AIwho)
        if Done==1:
            break
        if Win==1:
            break
        if Lose==1:
            break
        if difc=="1":
            AI_move(AIwho,who)
        if difc=="0":
            AIE(AIwho,who)  
        TTTB()
        Done=Tied()
        Win=Winner(who)
        Lose=loser(AIwho)
        if Done==1:
            break
        if Win==1:
            break
        if Lose==1:
            break
        if second=="1":
            Turn(who)
            TTTB()
        Done=Tied()
        Win=Winner(who)
        Lose=loser(AIwho)
        Done=Tied()
        if Done==1:
            break
        if Win==1:
            break
        if Lose==1:
            break
    
    print "Game Over"
    idx2=0
    #**********************************
    #* Asks if they want to play again*
    #**********************************
    while 0<1:
        Again=raw_input("Want to play Again? Then type Y/N -->")
        print
        if Again=="no" or Again=="No" or Again=="N" or Again=="n":
            idx2=2
            break
        elif Again=="NO":
            print "Don't be Hating"
            idx2=2
            break
        elif Again=="yes" or Again=="Yes" or Again=="YES" or Again=="Y" or Again=="y":
            break
        elif Again!="yes" or Again!="Yes" or Again!="YES":
            print "Invalid Answer"
            print
    if idx2==2:
        break

    
