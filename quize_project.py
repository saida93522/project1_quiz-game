"""This application is a trivia quiz program.
The user chooses a topic and is then asked to complete quiz questions about that topic.
A 'Correct!' message is showed if the user answers a question correctly,
otherwise
a message with the correct answer.
After the user has completed all of the questions,
the number of questions successfully answered will be displayed."""
import copy
import sys
from quiz_questions import questions


def main():
    try:
        welcome_banner()
        while True:
            print('Enter "q" or "quit" to quit the game! ')
            print(
                'Choose from one of the following topics to be quizzed on.')
            for t in questions.keys():  # display all the current topics
                print(f'-*- {t.capitalize()}')

            topic = input('\nEnter Here: ').lower()
            if topic == 'quit' or topic == 'q':
                print('Your quiz session has ended......')
                sys.exit()
            elif topic in questions:
                quiz_questions(questions[topic])
            else:
                print('Not a valid topic, please try again.\n')

    except KeyError as key_err:
        print(f'key error {key_err}')


def welcome_banner():
    """ This function introduces the user to the quiz game """
    print('\t*' * 10)
    print('\t\tWelcome!')
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('\t*' * 10)
    print()


def quiz_questions(topic):
    """this function loops through set of questions based on chosen topic and returns the users score"""
    try:

        # returns size of quiz question
        current_list_size = len(topic)
        score = 0
        # loops through the passed topic questions list
        for i in copy.deepcopy(topic):
            print(i)
            user = input('Enter here:\t').lower()
            # return correct if the given key question matches the its corresponding value i.e users answer
            if topic[i].lower() == user:
                print('correct\n')
                score += 1
            else:
                print(
                    f'Sorry that was incorrect. The correct answer I was looking for was {topic[i]}\n')  # if not correct display the correct answer
                # del questions[topic][i]

        if score == current_list_size:  # check to see if they answered all the questions correctly
            print('Nice! you got all the answers correct!')
        else:
            # otherwise return score.
            print(f'You got {score}/{str(current_list_size)} correct!')
    except KeyError:
        print('Something went wrong in quiz_questions(), check logic')


main()
