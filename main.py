import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper , scissors): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} computer chose  {computer}")
    if player == computer:
        return "It's a tie!!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win"
        else:
            return "Paper covers rock! you lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! you win"
        else:
            return "scissors cuts paper! you lose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you win"
        else:
            return "Rock smashes scissors! you lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
########################
# examples
# choices = {"player": "rock", "computer": "paper"}
# p_choice = choices["player"]

# def greeting():
#     return "Hi"

# response = greeting()
# print(response)


# food = ["Pizza", "Carrorts", "eggs"]
# dinner = random.choice(food)

# a = 3
# b = 5

# if a != 5:
#     print("Yes")
# else:
#     print("No")


# age = 30
# print(f"Ellis is {age} years old.")

# age = 20
# if age >= 18:
#     print("You are an adult")
# elif age > 12:
#     print("You are a teenager.")
# elif age > 1:
#     print("You are a child")
# else:
#     print("you are a baby")
