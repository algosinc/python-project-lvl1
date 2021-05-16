#!/usr/bin/env python
import random
import game_engine


game_description = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def qa_generator():  # question and right answer generation

    val_a = random.randint(1, 100)
    val_b = random.randint(1, 100)

    question_text = str(val_a) + ' ' + str(val_b)
    right_answer = find_gcd(val_a, val_b)

    return question_text, right_answer


def main():
    game_engine.game_logic()  # start The game


if __name__ == '__main__':
    main()
