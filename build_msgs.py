"""Module with functions that builds messages"""


def build_result_msg(result: str, score: str) -> str:
    """Function that builds a string to display the result of the round
    Args:
        result (str): Who won the round
        score (str): The score up to this momment
    Returns:
        str: Message with the result
    """
    return "\n".join([result, score])


def build_options_display(
    options: dict[str, str], user_option: str, computer_option: str, divider: str
) -> str:
    """Functions that builds a string to display the options
       of the user and computer
    Args:
        user_option (str): Option selected by the user
        computer_option (str): Option selected by the computer
        divider (str): A string with a divider
    Returns:
        str: String that displays the options of the user and computer
    """
    user_str = f"El usuario escogio: {options[user_option]}"
    computer_str = f"La computadora escogio: {options[computer_option]}"
    return "\n".join([user_str, computer_str, divider])


def build_round_header(rounds: int, divider: str) -> str:
    """Function that builds the round header string
    Args:
        rounds (int): Round to play
        divider (str): A string with a divisor
    Returns:
        str: The round header string
    """
    return "\n".join([divider, f"RONDA {rounds}", divider])


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
