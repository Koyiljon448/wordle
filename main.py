from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random


def main():
    print("Hello Wordle:")
    wordle = Wordle("APPLE")
    while wordle.can_attempts:
        x = input("\nType your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} character long!"
                + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You have solved the puzzle.")
    else:
        print("You failed to solve the puzzle.")


def display_results(wordle: Wordle, draw_border_around=None):
    print("\nYour result so far...\n")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    drew_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readline():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def drew_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_lenght = size + pad * 2
    top_border = "┌" + "─" * content_lenght + "┐"
    bottom_border = "└" + "─" * content_lenght + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


if __name__ == "__main__":
    main()
