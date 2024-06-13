'''Rock Paper Scissors game'''

import random

def get_computer_choice():
    choices= ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif(user_choice== 'rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
        return 'user'
    else:
        return 'computer'
    
def result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == 'tie':
        print("Its a Tie!!")
    elif winner == 'user':
        print("You win!!")
    else:
        print("You lose.")

def play_round():
    user_choice = input("Enter your choice:")
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid. Enter your choice:")
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    result(user_choice, computer_choice, winner)
    return winner

def play_game():
    user_score = 0
    computer_score = 0
    round = 1

    while True:
        print(f"\nRound {round}")
        winner = play_round()
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
        
        round += 1

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thank you for playing!")

print("Welcome to Rock, Paper, Scissors game!!")
play_game()