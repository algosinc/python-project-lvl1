#!/usr/bin/env python
import random
import game_engine

game_description = 'What is the result of the expression?'


def qa_generator():  # question and right answer generation

    val_a = random.randint(1, 100)
    val_b = random.randint(1, 100)
    operator = random.randint(1, 3)

    if operator == 1:  # operator +
        question_text = str(val_a) + ' + ' + str(val_b)
        right_answer = val_a + val_b

    elif operator == 2:  # operator -
        question_text = str(val_a) + ' - ' + str(val_b)
        right_answer = val_a - val_b

    elif operator == 3:  # operator *
        question_text = str(val_a) + ' * ' + str(val_b)
        right_answer = val_a * val_b

    return question_text, right_answer


def main():
    game_engine.game_logic()  # start The game


if __name__ == '__main__':
    main()
