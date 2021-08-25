"""This application is a trivia quiz program.
The user chooses a topic and is then asked to complete quiz questions about that topic.
A 'Correct!' message is showed if the user answers a question correctly,
otherwise
a message with the correct answer.
After the user has completed all of the questions,
the number of questions successfully answered will be displayed."""
import sys
# import topic Questions
from quiz_questions import art_questions

# global score variable that adds total questions answered for ALL topics
total_quize_score = 0

# ** quize topic functions**

# asks user art questions


def artQuestions():
    try:
        # local score that keeps track of ONLY art questions
        art_score = 0
        # loop though  art question nested dictionary
        for currQuestion in art_questions:
            # inner dictionary 1:{question} ++
            print(art_questions[currQuestion]['question'])
            answerGiven = input('Enter your answere here: ').lower()
            # verify if user's answer was correct or incorrect
            user_answer = check_answer(
                art_questions, currQuestion, answerGiven)
            if user_answer:
                print('Correct!')
                art_score += 1
                # total_quize_score += 1
            else:
                print(
                    f'Sorry that was incorrect.The correct answer is {art_questions[currQuestion]["answer"]}')
        print(f'You got {art_score}/{str(len(art_questions))}')
        print('')

        # ask if they want more art question else call function send them

    except Exception:
        print('Something went wrong in artQuestion function')
# ** end quiz topic functions


# chosen topic
def choose_topic(topic):
    try:
        if topic == "q" or topic == "quit":
            print('Your quiz session has ended.')
            sys.exit()

        while topic != 'quit':
            if topic == 'art':
                print(f'Chosen topic: {topic.capitalize()}')
                artQuestions()

                # elif topic == 'Space':
                #     spaceQuestion()
                # elif topic == 'Sport' or topic == 'Sports':
                #     sportQuestions()
            else:
                print(
                    'Unfortunetly we dont have any questions ready for that topic yet')
                choose_topic(topic)

    except Exception:
        print('something went wrong in choosing a topic')

# function that checks answers for any given list of questions


def check_answer(question_list, question, answer):
    if question_list[question]['answer'].lower() == answer:
        return True
    else:
        return False


# Main
def main():
    try:
        # Ask user for topic to be quized on
        print("Enter 'q' or 'quit' anytime you want to quit the game!")
        print('****Welcome!***\nPut your knowledge to the test with this Ultimate Quiz Questions!')

        # topicList = ['art', 'space', 'sport']

        choose_topic(input(
            'Choose one of the following topics to be quizzed on:\tArt\tSpace\tSport.\nEnter Here: ').lower())

    except Exception:
        print('Something went wrong in main.')


main()
