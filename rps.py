import random

def get_user_choice(choices):
    print("\nChoose one:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    user_input = input("Enter the number of your choice: ")
    if user_input.lower() == "secret":
        print("Easter Egg unlocked! You win this round automatically!")
        return "Easter Egg"
    try:
        idx = int(user_input) - 1
        if 0 <= idx < len(choices):
            return choices[idx]
    except ValueError:
        pass
    print("Invalid input. Try again.")
    return get_user_choice(choices)

def get_computer_choice(choices):
    return random.choice(choices)

def determine_winner(user, computer, rules):
    if user == "Easter Egg":
        return "user"
    if user == computer:
        return "tie"
    elif computer in rules[user]:
        return "user"
    else:
        return "computer"

def main():
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    # Rules: each key beats the values in its list
    rules = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Spock", "Paper"],
        "Spock": ["Scissors", "Rock"]
    }
    print("Welcome to Extended Rock, Paper, Scissors, Lizard, Spock!")
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        play = input("\nDo you want to play a round? (yes/no): ").strip().lower()
        if play not in ["yes", "y"]:
            print(f"\nFinal Score: You {user_score} - Computer {computer_score} (Rounds played: {rounds})")
            print("Thanks for playing!")
            break

        user_choice = get_user_choice(choices)
        computer_choice = get_computer_choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice, rules)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        rounds += 1
        print(f"Score: You {user_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()