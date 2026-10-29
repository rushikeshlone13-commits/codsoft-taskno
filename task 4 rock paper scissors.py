import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    print("=" * 40)
    print(" CODSOFT - ROCK PAPER SCISSORS GAME")
    print("=" * 40)

    while True:
        print("\nChoices: rock, paper, scissors")
        user_choice = input("Enter your choice: ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Your Choice     : {user_choice}")
        print(f"Computer Choice : {computer_choice}")

        # Game Logic
        if user_choice == computer_choice:
            print("Result          : It's a Tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("Result          : You Win! 🎉")
            user_score += 1
        else:
            print("Result          : Computer Wins! 💻")
            computer_score += 1

        print(f"\n--- Scoreboard ---")
        print(f"User: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Final Scores:")
            print(f"User: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()