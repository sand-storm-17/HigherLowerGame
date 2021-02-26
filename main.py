# Import Files
from game_data import data
from game_art import logo
from random import randint
from game_art import vs
# Header
print(logo)

# Code
size_data = len(data)


# Item information
def item(list_given):
    print(f"{list_given['name']},  {list_given['description']},  {list_given['country']}  \n")


# Game
def game():
    print("Welcome to the Higher Lower Game !!! \n \n")
    count = 0
    is_winning = True
    item2 = randint(0, size_data - 1)
    while is_winning:
        # Body

        item1 = item2
        item2 = randint(0, size_data - 1)

        item(data[item1])
        print(f"{vs}\n")
        item(data[item2])

        choice = input("Which of the two do you think have more followers? Type 'A' or 'B' \n \n")
        if data[item1]["follower_count"] > data[item2]["follower_count"]:
            correct_choice = 'A'
        else:
            correct_choice = 'B'

        if choice == correct_choice:
            is_winning = True
            count += 1
        else:
            is_winning = False

    print(f"Yay you won {count} times")
    continue_game = input("Do you want to play again? type 'y' or 'n' ")
    if continue_game == 'y':
        game()


game()
