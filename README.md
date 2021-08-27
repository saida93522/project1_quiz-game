<!--Refrence back to this when stuck. 
***remove comment later***
documentation/project outline:
1. create a seperate file for the all the topic quiz questions.
    -use dictionary to store the questions. 
    -create unique key for each question and answer.
        - use unique key to modify the question and answer dictionary.

2.split code into sub functions
    -create a function that allows users to choose from a list of topics.
    -verify user entered correct topic choice in any case. 
    -create those topic into their own small functions.
    -create a quizQuestion functions that should loop through ANY given quiz question and returns the result.
        -call check_answer() from this this function to check the answer for any given question 
        -this should help apply the DRY principle
    -create a function that displays total result.this should not effect any num of quiz question updates.

    --if done before due date,for more practice try refactoring code to OOP.
 -->
_______________________________________________

### This application is a trivia quiz program.
_______________________________________________


The challenge

**Users should be able to:**

    - Chooses a topic and is then asked to complete quiz questions about that topic.
    - A 'Correct!' message is showed if the user answers a question correctly,
    - otherwise a message with the correct answer.
    - After the user has completed all of the questions,
    - the number of questions successfully answered will be displayed.
![screenshot](/outputScreenshot.png)
_______________________
**What I learned so far**

I learned a lot about dictionaries/nested dictionaries.

- You can't change the size of dictionary during iteration.i.e add/remove entries in dict objects.
        
            quizQuestion = {  
                1:{'question':'The Olympics are held every how many years?',
                    answer:'4'},
                2:{'question':'What does MLB stand for? A: Major League Baseball?',
                    answer:'Major League Baseball'},
                3:{'question':'Which country has won the soccer world cup the most times?',
                    answer:'Brasil'}
                }

            //pseduo-code-ish 🥴
            for q in quizQuestion:
                if  question_list[q]['question'] == question_list[q]['answer']:
                    del current question
                    print('correct)
                else:
                    del current question
                    print('incorrect') 
            output//
            Runtimeerror: dictionary changed size during iteration
            in this scenerio i used the deepcopy which allowed me to del/update.


- Access tuple values by using index like my_tuple[int].
    Otherwise it will return `TypeError: tuple indices must be integers or slices, not str`.
    I had trouble figuring this part out. I was overwriting quiz dictionary with tuple and trying to access questions using a string.



