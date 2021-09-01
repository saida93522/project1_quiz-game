"""This application is a trivia quiz program.
The user chooses a topic and is then asked to complete quiz questions about that topic.
A 'Correct!' message is showed if the user answers a question correctly,
otherwise
a message with the correct answer.
After the user has completed all of the questions,
the number of questions successfully answered will be displayed."""
import copy
import sys
# import topic Questions
from quiz_questions import questions


def main():
    try:
        welcome_banner()
        while True:
            print(' Enter "q" or "quit" to quit the game! ')
            print(
                'Choose from one of the following topics to be quizzed on: *Art\t*Space\t*Sport.')
            topic = input('Enter Here: ').lower()
            if topic == 'art':
                art_questions()
            elif topic == 'space':
                space_questions()
            elif topic == 'sport':
                sport_questions()
            elif topic == 'quit' or 'q':
                print('Session ended')
                sys.exit()
            else:
                print('Not a valid topic, please try again.\n')

    except KeyError as key_err:
        print(f'key error {key_err}')


def welcome_banner():
    print('\t*' * 10)
    print('\t\tWelcome!')
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('\t*' * 10)
    print()

# *****TOPICS****


def art_questions():
    try:
        print(f'Chosen topic: Art\n')
        quiz_questions('art')

    except Exception as err:
        # update later
        print(f'Something went wrong in artQuestions() {err}')


def space_questions():
    try:
        print(f'Chosen topic: Space\n')
        quiz_questions('space')

    except Exception as err:
        # update later
        print(f'Something went wrong in artQuestions() {err}')


def sport_questions():
    try:
        print(f'Chosen topic: Sport\n')
        quiz_questions('sport')

    except Exception as err:
        # update later
        print(f'Something went wrong in artQuestions() {err}')


def quiz_questions(topic):
    try:

        current_list_size = len(questions[topic])
        score = 0
        for i in copy.deepcopy(questions[topic]):
            print(i)
            user = input('Enter here:\t').lower()
            if questions[topic][i].lower() == user:
                print('correct')
                score += 1
                # del questions[topic][i]
            else:
                print(
                    f'Sorry that was incorrect. The correct answer we were looking for was {questions[topic][i]}\n')
                # del questions[topic][i]

        if score == current_list_size:
            print('Nice! you got all the answers correct!')
        else:
            print(f'You got {score}/{str(current_list_size)} correct!')
    except KeyError:
        print('Something went wrong in quiz_questions()')


main()
