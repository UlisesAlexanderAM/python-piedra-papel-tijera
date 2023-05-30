"""
Game of Rock,paper or scissor in spanish
---
Juego de piedra, papel o tijera
"""
from random import choice

from libs.build_msgs import (
    build_options_display,
    build_result_msg,
    build_round_header,
    build_score,
)
from libs.check_user_wins import check_user_wins

OPTIONS = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
LIST_OF_OPTIONS = list(OPTIONS.keys())

INSTRUCTIONS = """
Instrucciones: teclee el numero de la opcion deseada
para el juego de piedra, papel o tijera:
1.- Piedra
2.- Papel
3.- Tijera
4.- Saltar ronda
Cualquier otro numero - Salir del juego
"""
WELCOME_MSG = "Bienvenido al juego de piedra, papel o tijera"

INPUT_MSG = "Teclee el numero de la opción deseada: "
ASK_NUM_ROUNDS = "Ingrese el numero de rondas a jugar: "
LEN_INPUT_MSG = len(INPUT_MSG)
ASTERISKS = "*" * LEN_INPUT_MSG


def ask_rounds() -> int:
    while True:
        rounds = input(ASK_NUM_ROUNDS)
        if rounds.isdigit():
            break
        print("Valor invalido ingrese un numero")

    return int(rounds)


def validate_user_selection() -> str:
    while True:
        print(INSTRUCTIONS)
        user_option = input(INPUT_MSG)
        if user_option.isdigit():
            break
        print("Opcion invalida. Ingrese una opcion valida")

    return user_option


def check_winner(user_option: str, computer_option: str):
    if user_option == computer_option:
        result = 0
    elif check_user_wins(user_option, computer_option):
        result = 1
    else:
        result = -1

    return result


def modified_wins(user_wins: int, computer_wins: int, result: int):
    if result == 1:
        user_wins += 1
    elif result == -1:
        computer_wins += 1

    return user_wins, computer_wins


def round_result_msg(result: int, score: str):
    if result == 0:
        return build_result_msg("Empataste esta ronda", score)
    if result == 1:
        return build_result_msg("Ganaste esta ronda", score)
    if result == -1:
        return build_result_msg("Perdiste esta ronda", score)


def main():
    """Function with the main logic of the game"""
    print(WELCOME_MSG)
    computer_wins = 0
    user_wins = 0
    current_round = 1
    rounds = ask_rounds()
    while True:
        score = build_score(user_wins, computer_wins, ASTERISKS)

        user_option = validate_user_selection()

        if user_option == "4":
            print(score)
            continue

        if user_option not in LIST_OF_OPTIONS:
            print("Gracias por jugar.¡Adios!")
            break

        round_header = build_round_header(current_round, ASTERISKS)

        print(round_header)
        print(score)

        computer_option = choice(LIST_OF_OPTIONS)

        options_display = build_options_display(
            OPTIONS, user_option, computer_option, ASTERISKS
        )

        print(options_display)

        result = check_winner(user_option, computer_option)
        user_wins, computer_wins = modified_wins(user_wins, computer_wins, result)
        current_round += 1
        result_msg = round_result_msg(result, score)
        print(result_msg)

        if current_round > rounds:
            break


if __name__ == "__main__":
    main()
