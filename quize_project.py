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
from quiz_questions import art_questions, space_questions, sports_questions


def choose_topic(topic):
    try:
        while topic != 'q' or 'quit':
            if topic == 'art':
                artQuestions()
            elif topic == 'space':
                spaceQuestions()
            elif topic == 'sport' or topic == 'sports':
                sportQuestions()
            else:
                print(
                    'Error,now restarting game.Try again make sure to check your spelling\n')
                return main()
            break

    except Exception as err:
        print(f'something went wrong in choosing a topic{err}')

# *****TOPICS****


def artQuestions():
    try:
        print(f'Chosen topic: Art\n')
        section = 'art'
        art_score = 0
        quiz_list, first_score = quizeQuestions(art_questions, art_score)
        # ask if they want more art question else call function send them
        print('Would you like some more art questions? or to restart game?')
        print(
            "Type 'restart' to restart the game. Type 'more' for extra art questions? ")
        new_topic = input('Enter Here: ').lower()
        if new_topic == 'restart':
            return main()

        elif new_topic == 'more':  # try rendering these from quiz_question.py file
            art_questions[0] = {"question": "Which kid's TV characters are named after Renaissance artists?\t",
                                "answer": "Teenage Mutant Ninja Turtles"}
            art_questions[1] = {"question": "The graphite in an artist's pencil is made of what chemical element?\t",
                                "answer": "Carbon"
                                }
        second_quiz, second_score = quizeQuestions(art_questions,  art_score)

        display_result(quiz_list, first_score,
                       second_quiz, second_score, section)

    except Exception as err:
        # update later
        print(f'Something went wrong in artQuestions() {err}')


# display space questions
def spaceQuestions():
    try:
        print(f'Chosen topic: Space\n')
        space_score = 0
        section = 'space'

        # first set of questions
        space_quiz, first_score = quizeQuestions(space_questions, space_score)
        # ask if they want more art question else call function send them
        # TODO: Fix duplication here
        print('Would you like more space questions? or to restart game?')
        print(
            "Type 'restart' to restart the game. Type 'more' for extra space questions? ")
        new_topic = input('Enter Here: ').lower()
        if new_topic == 'restart':
            return main()

        elif new_topic == 'more':
            space_questions[0] = {"question": "What was the first human-made object to leave the solar system?\t",
                                  "answer": "Voyager 1"
                                  }

            space_questions[1] = {"question": "When an asteroid enters the Earth's atmosphere and burns up, it is known as what?\t",
                                  "answer": "Meteor"
                                  }
        # second set of questions
        extra_questions, extra_score = quizeQuestions(
            space_questions,  space_score)
        display_result(space_quiz, first_score,
                       extra_questions, extra_score, section)

    except Exception as err:
        # update later
        print(f'Something went wrong in spaceQuestion() {err}')


# displays sports questions
def sportQuestions():
    try:
        section = 'sport'

        print(f'Chosen topic: Sport\n')
        sportScore = 0
        sportQuiz, sport_score = quizeQuestions(sports_questions, sportScore)

        # TODO: Fix duplication here
        # ask if they want more art question else call function send them
        print('Would you like more sports questions? or to restart game?')
        print(
            "Type 'restart' to restart the game. Type 'more' for extra art questions? ")
        new_topic = input('Enter Here: ').lower()
        if new_topic == 'restart':
            return main()

        elif new_topic == 'more':
            sports_questions[0] = {"question": "The Olympics are held every how many years?\t",
                                   "answer": "4"}
            sports_questions[1] = {"question": "Who has won more tennis grand slam titles, Venus Williams or Serena Williams?\t",
                                   "answer": "Serena Williams"}
        extra_quiz, second_score = quizeQuestions(sports_questions, sportScore)
        display_result(sportQuiz, sport_score,
                       extra_quiz, second_score, section)

    except Exception as err:
        # update later
        print(f'Something went wrong in sportQuestions() {err}')


# psuedo:create a function that accepts any given quizlist. returns the size and the score
def quizeQuestions(my_quiz_dict, correct_score):
    try:
        currentListSize = len(my_quiz_dict)
        # loop through art question nested dictionary using deepcopy
        for currentQuestion in copy.deepcopy((my_quiz_dict)):
            # inner dictionary i.e 1:{question} ++
            print(my_quiz_dict[currentQuestion]['question'])
            answerGiven = input('Enter answer here: ').lower()
            user_answer = check_answer(
                my_quiz_dict, currentQuestion, answerGiven)

            # verify if user's answer was correct
            if user_answer:
                print('Correct!\n')
                correct_score += 1
                # del the current question from list
                del my_quiz_dict[currentQuestion]
            else:
                print(
                    f'Sorry that was incorrect. The correct answer we were looking for was {my_quiz_dict[currentQuestion]["answer"]}\n')
                del my_quiz_dict[currentQuestion]
            # verification purposes delete later
            # print(f'quize size is now {str(len(my_quiz_dict))}')

        print(f'You got {correct_score}/{str(currentListSize)} correct!')
        # overwrites dict and returns tuple
        return currentListSize, correct_score
    except TypeError as err:
        # update later
        print(f'Something went wrong in the quizQuestion() {err}')


# function that checks the answer for any given  questions
def check_answer(question_list, question, answer):
    try:
        # returns true if the answer matches
        if question_list[question]['answer'].lower() == answer:
            return True
        else:
            return False
    except Exception as err:
        # update later
        print(f'Something went wrong in check_answer() {err}')


# display score results
def display_result(quizList1, first_score, extra_quiz, extra_score, section):
    totalScore = first_score + extra_score
    total_questions = quizList1 + extra_quiz
    print('\n***RESULTS')
    print(
        f'You answered a total of {totalScore}/{total_questions} {section} questions correct')


def main():
    # topicList = ['art', 'space', 'sport']
    try:
        # Ask user for topic to be quized on
        print('****Welcome!***\nPut your knowledge to the test with this Ultimate Quiz Questions!')
        print("Note**Enter 'q' or 'quit' to quit the game!")

        quit_game = ""
        if quit_game == "q" or quit_game == "quit":
            print('Your quiz session has ended.')
            sys.exit()
        else:
            choose_topic(input(
                'Choose one of the following topics to be quizzed on:\tArt\tSpace\tSport.\nEnter Here: ').lower())

    except Exception as err:
        print(f'Something went wrong in main.{err}')  # update later


main()
