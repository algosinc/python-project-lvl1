#!/usr/bin/env python
import prompt
import __main__
from string import Template

number_of_requests = 3  # number of question request


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    welcome_text = Template('Hello, ${user_name}!')
    print(welcome_text.substitute(user_name=name))
    print(__main__.game_description)


def check_result(user_answer, right_answer):
    if user_answer == str(right_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}'' is wrong answer ;(. Correct answer was \
                '{right_answer}'.")
        try_again_text = Template("Let's try again, ${user_name}!")
        print(try_again_text.substitute(user_name=name))
        return False


def game_logic():

    welcome_user()

    i = 0
    is_user_answer = True

    while i in range(number_of_requests) and is_user_answer is True:
        question_text, right_answer = __main__.qa_generator()
        user_answer = prompt.string(print(f'Question: {question_text}'))
        is_user_answer = check_result(user_answer, right_answer)

        if i == number_of_requests - 1:
            congrat_text = Template("Congratulations, ${user_name}!")
            print(congrat_text.substitute(user_name=name))

        i += 1
