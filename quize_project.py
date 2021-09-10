"""This application is a trivia quiz program.
The user chooses a topic and is then asked to complete quiz questions about that topic.
A 'Correct!' message is showed if the user answers a question correctly,
otherwise
a message with the correct answer.
After the user has completed all of the questions,
the number of questions successfully answered will be displayed."""

from quiz_questions import questions


def main():
    # try:
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
                # sys.exit()  # Avoid sys.exit - better to break out of the while loop to stop te quiz.
                break
            elif topic in questions:
                quiz_questions(questions[topic])
            else:
                print('Not a valid topic, please try again.\n')

    # except KeyError as key_err:   # What is causing key errors? These are errors you can prevent in code 
    #     # by checking if a key is in a dictionary before trying to read it, or using get and checking if you 
    #     # get a value or None. 
    #     #  https://docs.python.org/3/library/stdtypes.html?highlight=dictionaries#dict.get
    #     print(f'key error {key_err}')


def welcome_banner():
    """ This function introduces the user to the quiz game """
    print('\t*' * 10)
    print('\t\tWelcome!')
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('\t*' * 10)
    print()


def quiz_questions(topic):
        """this function loops through set of questions based on chosen topic 
        This function doesn't return anything - make sure docstrings accurately describe the code. """
    # try:

        # calculate size of quiz question (the len function returns the size, but this function doesn't)
        current_list_size = len(topic)  # topic is a dictionary, not a list. Is current_list_size misleading? how about number_of_questions? 
        score = 0
        # loops through the passed topic questions list
        # you dont need to make a copy. If you don't modify topic, you can use the original.
        for question, answer in topic.items():  # use a more descriptive variable name. Using .items allows access to keys and values 
            print(question)
            user = input('Enter here:\t').lower()
            # return correct if the given key question matches the its corresponding value i.e users answer
            if topic[question].lower() == user:
                print('Correct\n')
                score += 1
            else:
                print(
                    f'Sorry that was incorrect. The correct answer I was looking for was {answer}\n')  # if not correct display the correct answer
                # del questions[topic][i]   # Remove unused code 

        if score == current_list_size:  # check to see if they answered all the questions correctly
            print('Nice! you got all the answers correct!')
        else:
            # otherwise return score.
            print(f'You got {score}/{current_list_size} correct!')  # str not needed in an f string
    
    # except KeyError:   # This shouldn't happen, remove. Write your logic to avoid key errors, and test code to make sure they don't happen
    #     print('Something went wrong in quiz_questions(), check logic')


main()
