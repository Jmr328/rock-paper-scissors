import random

options = ['rock', 'paper', 'scissors']



def Game():
    while True:
        robotPick = random.choice(options)
        playerPick = input("Select one [ Rock, Paper, Scissors ]: ")
        print(robotPick)
        print(playerPick)

        if robotPick == playerPick:
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("It's a Tie!")
            break
        elif robotPick[0] and playerPick.lower() == "scissors":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Robot Wins!")
            break   
        elif robotPick[2] and playerPick.lower() == "paper":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Robot Wins!")
            break
        elif robotPick[1] and playerPick.lower() == "rock":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Robot Wins!")
            break
        elif robotPick.lower() == "rock" and playerPick.lower() == "paper":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Player Wins!")
            break
        elif robotPick.lower() == "scissors" and playerPick.lower() == "rock":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Player Wins!")
            break
        elif robotPick.lower() == "paper" and playerPick.lower() == "scissors":
            print("Robot chose: ", robotPick)
            print("Player chose: ", playerPick)
            print("Player Wins!")
            break
        else:
            print("Something aint right")

Game()