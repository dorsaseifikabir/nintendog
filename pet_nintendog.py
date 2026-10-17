from nintendogs import Nintendogs
import sys

count = 0

holly = Nintendogs("holly", "active, loves to play",
                   "gsd", "female", 0, 0, 0, 100, 100)
pongo = Nintendogs("pongo", "lazy, loves eating and sleeping",
                   "dalmatian", "male", 0, 0, 0, 100, 100)

dogs = {'holly': holly, 'pongo': pongo}
for key, value in dogs.items():
    value.show_status()

while True:
    player_choice = input(
        "\nhello! do you want to play with holly or pongo? type 'quit' to quit! ").lower().strip()

    if player_choice in dogs:
        chosen_dog = dogs[player_choice]
        print(f"\n{chosen_dog} is a great choice! you two will have a lot of fun!\n")
        break
    elif player_choice == 'quit':
        sys.exit()
    else:
        print("you must choose one of the given options!")

menu = {"feed": chosen_dog.feed, "give water": chosen_dog.give_water, "walk": chosen_dog.walk, "play fetch": chosen_dog.play_fetch,
        "bath": chosen_dog.bath, "cuddle": chosen_dog.cuddle, "let sleep": chosen_dog.sleep, "show status": chosen_dog.show_status}

for i, key in enumerate(menu.keys(), start=1):
    print(f'{i}. {key}')
print()


while True:
    valid_turn = True
    player_action = input(
        "what would you like to do? or you can type quit to exit!\n").lower().strip()
    if player_action == 'feed' or player_action == '1':
        chosen_dog.feed()
        count += 1
    elif player_action == 'give water' or player_action == '2':
        chosen_dog.give_water()
        count += 1
    elif player_action == 'walk' or player_action == '3':
        chosen_dog.walk()
        count += 1
    elif player_action == 'play fetch' or player_action == '4':
        chosen_dog.play_fetch()
        count += 1
    elif player_action == 'bath' or player_action == '5':
        chosen_dog.bath()
        count += 1
    elif player_action == 'cuddle' or player_action == '6':
        chosen_dog.cuddle()
        count += 1
    elif player_action == 'let sleep' or player_action == '7':
        chosen_dog.sleep()
        count += 1
    elif player_action == 'show status' or player_action == '8':
        chosen_dog.show_status()
        valid_turn = False
    elif player_action == 'quit':
        print(f'\n{chosen_dog} will miss you!\n')
        sys.exit()
    else:
        print(f'\nyou must either choose something from the menu or "quit"!\n')
        valid_turn = False
    if valid_turn:
        chosen_dog.turn()
    if count == 20 and chosen_dog.happiness >= 70:
        print("you're an amazing dog parent!")
        count = 0
    elif count == 20 and chosen_dog.happiness < 70:
        print("you have to try harder as a dog parent!")
        count = 0
