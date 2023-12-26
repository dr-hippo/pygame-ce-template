"""Helper script to ask questions when building."""


def yn(question) -> bool:
    """
    Ask yes-no question, returning result as True or False.

    :return Answer to question"""
    print("")  # Newline to make it a little less claustrophobic
    answer = None
    while answer is None:
        txt = input("  " + question + " (y/n): ")
        if txt == "y" or txt == "Y":
            answer = True
        elif txt == "n" or txt == "N":
            answer = False
    print("")
    return answer