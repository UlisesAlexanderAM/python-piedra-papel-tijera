import random

OPTIONS = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
LIST_OF_OPTIONS = list(OPTIONS.keys())

computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print("*" * 10)
    print("RONDA", rounds)
    print("*" * 10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)


    rounds += 1
    if not user_option.isdigit():
        print("Opción invalida")
        continue

    if user_option == "4":
        print(score)
        continue

    if user_option not in LIST_OF_OPTIONS:
        print("Gracias por jugar.¡Adios!")
        break

    computer_option = random.choice(LIST_OF_OPTIONS)

    user_opt_str = OPTIONS[user_option]
    comp_opt_str = OPTIONS[computer_option]
    print(f"El usuario escogio: {user_opt_str}")
    print(f"La computadora escogio: {comp_opt_str}")

    print(ASTERISKS)

    if user_option == computer_option:
        print("Empate")
        print(score)
        rounds += 1
        continue

    user_win_str = f"Gana usuario: {user_opt_str} le gana a {comp_opt_str}".join(
        ["\n", ASTERISKS]
    )
    computer_win_str = (
        f"Gana computadora: {comp_opt_str} le gana a {user_opt_str}".join(
            ["\n", ASTERISKS]
        )
    )

    if user_option == "1" and computer_option == "2":
        computer_wins += 1
        rounds += 1
        print(computer_win_str)
    elif user_option == "1" and computer_option == "3":
        user_wins += 1
        rounds += 1
        print(user_win_str)

    if user_option == "2" and computer_option == "1":
        user_wins += 1
        rounds += 1
        print(user_win_str)
    elif user_option == "2" and computer_option == "3":
        computer_wins += 1
        rounds += 1
        print(computer_win_str)

    if user_option == "3" and computer_option == "1":
        computer_wins += 1
        rounds += 1
        print(computer_win_str)
    elif user_option == "3" and computer_option == "2":
        user_wins += 1
        rounds += 1
        print(user_win_str)

    if computer_wins == 2:
        print("El ganador es la computadora")
        break

    if user_wins == 2:
        print("El ganador es el usuario")
        break
