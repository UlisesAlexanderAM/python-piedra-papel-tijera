"""
Game of Rock,paper or scissor in spanish
---
Juego de piedra, papel o tijera
"""
from random import choice

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


def build_score(user_wins: int, computer_wins: int, divider: str) -> str:
    """Function that builds the score string

    Args:
        user_wins (int): Number of victories for the user
        computer_wins (int): Number of victories for the computer
        divider (str): A string with a divisor

    Returns:
        str: The score string
    """
    computer_score = f"Victorias de la computadora: {computer_wins}"
    user_score = f"Victorias del usuario: {user_wins}"
    score = "\n".join(["Marcador", computer_score, user_score, divider])
    return score


def build_round_header(rounds: int, divider: str) -> str:
    """Function that builds the round header string

    Args:
        rounds (int): Round to play
        divider (str): A string with a divisor

    Returns:
        str: The round header string
    """
    return "\n".join([divider, f"RONDA {rounds}", divider])


def build_options_display(user_option: str, computer_option: str, divider: str) -> str:
    """Functions that builds a string to display the options
       of the user and computer

    Args:
        user_option (str): Option selected by the user
        computer_option (str): Option selected by the computer
        divider (str): A string with a divider

    Returns:
        str: String that displays the options of the user and computer
    """
    user_str = f"El usuario escogio: {OPTIONS[user_option]}"
    computer_str = f"La computadora escogio: {OPTIONS[computer_option]}"
    return "\n".join([user_str, computer_str, divider])


def build_result_msg(result: str, score: str) -> str:
    """Function that builds a string to display the result of the round

    Args:
        result (str): Who won the round
        score (str): The score up to this momment

    Returns:
        str: Message with the result
    """
    return "\n".join([result, score])


def check_user_wins(user_option: str, computer_option: str) -> bool:
    """Function that checks if the user won the round

    Args:
        user_option (str): The option that the user choose
        computer_option (str): The option that the computer choose

    Returns:
        bool: True if the user won false otherwise
    """
    if user_option == "1" and computer_option == "3":
        return True
    if user_option == "2" and computer_option == "1":
        return True
    if user_option == "3" and computer_option == "2":
        return True
    else:
        return False


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

        options_display = build_options_display(user_option, computer_option, ASTERISKS)

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
