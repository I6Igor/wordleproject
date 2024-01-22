def bubble_sort_rev(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(arr[j]) < key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def get_words(filename):
    with open(filename, "r") as file:
        return [word.strip() for word in file.readlines()]

def get_name():
    NAME = input("ENTER A 3-5 CHARACTER NAME TO ADD TO LEADERBOARD: ").upper()
    while len(NAME) > 5 or len(NAME) < 3:
        NAME = input("ENTER A 3-5 CHARACTER NAME TO ADD TO LEADERBOARD: ").upper()
    return NAME

def leaderboard():
    file = open("scoreboard.txt", "r")
    data = file.readlines()
    file.close()
    highscores = [dict(name=line.strip().split()[1], score=line.strip().split()[0]) for line in data]
    sorted_highscores = bubble_sort_rev(highscores, key=lambda arr: arr["score"])
    for i, line in enumerate(sorted_highscores[:5], 1):
        if len(line['name']) < 5:
            print(f"{i}. {line['name']} \t\t{line['score']}")
        else:
            print(f"{i}. {line['name']} \t{line['score']}")

def get_choice():
    choice = input("> ")
    while int(choice) <= 0 or int(choice) > 3:
        choice = input("> ")
    return choice

def menu():
    print("""==========================================
    ##      ##                  ##   ##       
    ##  ##  ##   ###   ## #   ####   ##    ### 
    ##  ##  #   ## ##  ####  ## ##   ##   # ## 
    ## ### ##  ##  ##  ##    ## ##   ##  ## ## 
    ## ### #   ##  ## ##     ## ##   ##   ####  
    ### ###    ## ##  ##     #####   ##   ##    
    ##  ##      ###   ##     ## ##   ##    ###
    ==========================================""")

    print("1. PLAY")
    print("2. HIGHSCORES")
    print("3. QUIT")
    while 1 > 0:
        choice = get_choice()
        if int(choice) == 3:
            exit()
        if int(choice) == 2:
            leaderboard()
        if int(choice) == 1:
            break