"""Module with a function that check if the user won the round"""


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
