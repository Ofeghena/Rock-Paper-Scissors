import random
# Definition of user option!
def userOption():
    userChoice = input("Choose Rock 'R', Paper 'P' or Scissors 'S':")
    if userChoice in ["Rock", "rock", "r", "R"]:
        userChoice = "R"
    elif userChoice in ["Paper", "paper", "p", "P"]:
        userChoice = "P"
    elif userChoice in ["Scissors", "scissors", "s", "S"]:
        userChoice = "S"
    else:
        print("Not in the option, try again.")
    return userChoice
# Definition of computer(cpu) option!
def cpuOption():
    option = ["Rock", "Paper", "Scissors"]
    cpuChoice = random.choice(option)
    if cpuChoice == "Rock":
        cpuChoice = "R"
    elif cpuChoice == "Paper":
        cpuChoice = "P"
    else:
        cpuChoice = "S"
    return cpuChoice
# Check of both player's moves and determination of winner!
while True:
    userChoice = userOption()
    cpuChoice = cpuOption()

    if userChoice == "R":
        if cpuChoice == "R":
            print("Player (Rock) : CPU (Rock)")
            print("It's a tie!")
        elif cpuChoice == "P":
            print("Player (Rock) : CPU (Paper)")
            print("Paper covers rock! Computer wins!")
            break
        elif cpuChoice == "S":
            print("Player (Rock) : CPU (Scissors)")
            print("Rock smashes scissors! You win!")
            break
    elif userChoice == "P":
        if cpuChoice == "R":
            print("Player (Paper) : CPU (Rock)")
            print("Paper covers rock! You win!")
            break
        elif cpuChoice == "P":
            print("Player (Paper) : CPU (Paper)")
            print("It's a tie!")
        elif cpuChoice == "S":
            print("Player (Paper) : CPU (Scissors)")
            print("Scissors cuts paper! Computer wins!")
            break
    elif userChoice == "S":
        if cpuChoice == "R":
            print("Player (Scissors) : CPU (Rock)")
            print("Rock smashes scissors! Computer wins!")
            break
        elif cpuChoice == "P":
            print("Player (Scissors) : CPU (Paper)")
            print("Scissors cuts paper! You win!")
            break
        elif cpuChoice == "S":
            print("Player (Scissors) : CPU (Scissors)")
            print("It's a tie!")
print("The end of the program! Thank you!")