"""
Game of Rock,paper or scissor in spanish
---
Juego de piedra, papel o tijera
"""
from random import choice

from build_msgs import (
    build_options_display,
    build_result_msg,
    build_round_header,
    build_score,
)
from check_user_wins import check_user_wins

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

INPUT_MSG = "Teclee el numero de la opción deseada: "
ASK_NUM_ROUNDS = "Ingrese el numero de rondas a jugar: "
LEN_INPUT_MSG = len(INPUT_MSG)
ASTERISKS = "*" * LEN_INPUT_MSG


def main():
    """Function with the main logic of the game"""
    print(INSTRUCTIONS)
    while True:
        computer_wins = 0
        user_wins = 0
        current_round = 1

        rounds = input(ASK_NUM_ROUNDS)
        if not rounds.isdigit():
            print("Formato incorrecto, debe ingresar un numero")
            continue

        rounds = int(rounds)

        user_option = input(INPUT_MSG)

        score = build_score(user_wins, computer_wins, ASTERISKS)

        if not user_option.isdigit():
            print("Opción invalida")
            continue

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

        if user_option == computer_option:
            result_msg = build_result_msg("Empataste esta ronda", score)
            print(result_msg)
            current_round += 1
            continue

        elif check_user_wins(user_option, computer_option):
            result_msg = build_result_msg("Ganaste esta ronda", score)
            print(result_msg)
            current_round += 1
            user_wins += 1

        else:
            result_msg = build_result_msg("Perdiste esta ronda", score)
            print(result_msg)
            current_round += 1
            computer_wins += 1

        if current_round > rounds:
            break


if __name__ == "__main__":
    main()
