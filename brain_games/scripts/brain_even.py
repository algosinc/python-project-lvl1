#!/usr/bin/env python
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    is_number_is_even()


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def is_number_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    num_question_repeat = 3  # number of question repeats
    for i in range(num_question_repeat):
        number = random.randint(1, 100)  # generate random int in range 1...100
        is_even = number % 2 == 0  # check is num is even

        answer = prompt.string(print(f'Question: {number}'))  # ask question
        if answer == 'yes':  # check user input
            is_answer_true = True
        elif answer == 'no':
            is_answer_true = False
        else:
            wrong_answer(answer, is_even)
            break

        # check if answer is correct
        if is_answer_true == is_even:
            print('Correct!')
        else:
            wrong_answer(answer, is_even)
            break

    if i == num_question_repeat - 1:
        print(f"Congratulations, {name}!")


def wrong_answer(answer, is_even):  # wrong answer generation
    if is_even:
        print(f"'{answer}'' is wrong answer ;(. Correct answer was 'yes'.")
    else:
        print(f"'{answer}'' is wrong answer ;(. Correct answer was 'no'.")

    print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
