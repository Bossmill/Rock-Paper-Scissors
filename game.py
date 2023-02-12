import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    player = int(input("Enter your choice (1, 2, or 3): "))
    computer = random.randint(1,3)
    
    if player == 1 and computer == 3:
        print("You chose Rock and the computer chose Scissors. You win!")
    elif player == 2 and computer == 1:
        print("You chose Paper and the computer chose Rock. You win!")
    elif player == 3 and computer == 2:
        print("You chose Scissors and the computer chose Paper. You win!")
    elif player == computer:
        print("It's a tie!")
    else:
        print("You lost. Better luck next time.")

if __name__ == "__main__":
    play_game()
