import random
SCORE = 0
TRY = 0
WORDS = open("words.txt")
list = []
for i in range(14854):
    list.append(WORDS.read(6))



while TRY < 6:
    CORRECT = list[random.randint(0,14854)].lower()
    WIN = 0
    TRY = 0



    while WIN == 0 and TRY < 6:
        GUESS = input("\n>").lower()
        if GUESS + "\n"  in list:
            for i in range(5):
                for j in range(5):
                    if GUESS[i] == CORRECT[i]:
                        print("🟩",end="")
                        break
                    if GUESS[i] == CORRECT[j]:
                        print("🟨",end="")
                        break
                    elif j == 4:
                        print("⬛",end="")
            if GUESS[0] == CORRECT[0] and GUESS[1] == CORRECT[1] and GUESS[2] == CORRECT[2] and GUESS[3] == CORRECT[3] and GUESS[4] == CORRECT[4]:
                WIN = 1
                SCORE += 1
            else:
                TRY +=1
        else:
            print("Not in words list")



#Tabela wyników
print("\nSCORE: " + str(SCORE))
while 1>0:
    NAME = input("ENTER A 3 CHARACTER NAME TO ADD TO LEADERBOARD: ").upper()
    if len(NAME) != 3:
        NAME = input("ENTER A 3 CHARACTER NAME TO ADD TO LEADERBOARD: ")
    else:
        break
SCOREBOARD = open("scoreboard.txt","a")
SCOREBOARD.write(str(SCORE) + ": " + NAME + "\n")
scorelist = []
for i in range(10):
    scorelist.append(SCOREBOARD.read())
print(SCOREBOARD.read())