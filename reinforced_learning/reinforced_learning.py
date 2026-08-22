import random

history = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

def ai_move():

    if sum(history.values()) == 0:
        return random.choice(["rock", "paper", "scissors"])

    prediction = max(history, key=history.get)

    if prediction == "rock":
        return "paper"

    elif prediction == "paper":
        return "scissors"

    else:
        return "rock"

while True:

    user = input(
        "\nChoose Rock, Paper, Scissors (or quit): "
    ).lower()

    if user == "quit":
        break

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid move")
        continue

    history[user] += 1

    computer = ai_move()

    print(f"You played: {user}")
    print(f"AI played: {computer}")

    if user == computer:
        print("Draw")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win")

    else:
        print("AI Wins")

    print("\nLearning Data:")
    print(history)