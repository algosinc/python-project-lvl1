#!/usr/bin/env python
import random
import game_engine


game_description = 'Answer "yes" if given number is prim\'e. \
                    Otherwise answer "no".'


def qa_generator():  # question and right answer generation

    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                     47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    value = random.randint(1, 101)

    if value in prime_numbers:  # chek number is prime
        right_answer = 'yes'
    else:
        right_answer = 'no'

    question_text = value
    return question_text, right_answer


def main():
    game_engine.game_logic()  # start The game


if __name__ == '__main__':
    main()
