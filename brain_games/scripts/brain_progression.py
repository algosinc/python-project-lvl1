#!/usr/bin/env python
import random
import game_engine


game_description = 'What number is missing in the progression?'


def qa_generator():  # question and right answer generation

    # first number in progression
    list_start = random.randint(1, 100)
    # progression step
    list_step = random.randint(1, 100)
    # quanity of numbers in progression
    list_length = random.randint(5, 10)
    # last number in progression
    list_end = list_start + list_step * list_length

    # set the item to be found in the middle of progression
    list_lost_item = list_length // 2 - 1
    # generate full progression
    prog_list = list(range(list_start, list_end, list_step))
    # progression before lost item
    prog_list1 = prog_list[0: list_lost_item]
    # progression after lost item
    prog_list2 = prog_list[list_lost_item + 1: list_length - 1]
    # generate question text
    question_text = ' '.join(str(e) for e in prog_list1) + ' ... ' + \
                    ' '.join(str(e) for e in prog_list2)
    right_answer = prog_list[list_lost_item]

    return question_text, right_answer


def main():
    game_engine.game_logic()  # start The game


if __name__ == '__main__':
    main()
