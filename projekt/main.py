import random
from colorama import Fore, Style
from functions import *
words = tuple(get_words("words.txt"))
words_num = len(words)
while 1>0:
    SCORE = 0
    TRY = 0
    menu()


    while TRY < 6:
        CORRECT = words[random.randint(0,words_num)].lower()
        #print(CORRECT)
        WIN = 0
        TRY = 0
        print("GUESS 5 LETTER WORD")
        while WIN == 0 and TRY < 6:
            GUESS = input("\n>").lower()
            if GUESS in words:
                for i in range(5):
                    for j in range(5):
                        if GUESS[i] == CORRECT[i]:
                            print(Fore.GREEN + "■ " + Style.RESET_ALL,end="")
                            break
                        if GUESS[i] == CORRECT[j]:
                            print(Fore.YELLOW + "■ " + Style.RESET_ALL,end="")
                            break
                        elif j == 4:
                            print("■ ",end="")
                if GUESS[0] == CORRECT[0] and GUESS[1] == CORRECT[1] and GUESS[2] == CORRECT[2] and GUESS[3] == CORRECT[3] and GUESS[4] == CORRECT[4]:
                    WIN = 1
                    SCORE += 1
                else:
                    TRY +=1
                    print("\nTry " + str(TRY) + "/6" )
            else:
                print("Not in words list")



    #Tabela wyników
    print("\nSCORE: " + str(SCORE))
    NAME = get_name()
    scoreboard = open("scoreboard.txt","a")
    scoreboard.write(str(SCORE) + " " + NAME + "\n")
    scoreboard.close()

    leaderboard()