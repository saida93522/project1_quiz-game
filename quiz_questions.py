# Question and Answer

# Makes a lot of sense to separate the data into a different file. This would be useful for version 2 
# if we upgraded to a database, or queried an API for the questions. 

questions = {

    # Remove the \t characters. Whatever presents this data to the user can handle any formatting or
    # alignment considerations. Perhaps you'll upgrade to a web app and then the questions would be displayed differently.
    'art': {
        'Who painted the Mona Lisa?': 'Leonardo da Vinci',
        'What precious stone is used to make the artist\'s pigment ultramarine?\t': 'Lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'
    },

    'space': {
        'Which planet is closest to the sun?': 'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
        'How many moons does Mars have?': '2'
    },
    'sport': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after? \t': 'Simone Biles',
        'Which country has won the soccer world cup the most times?\t': 'Brasil',
        'What does MLB stand for?\t': 'Major League Baseball',
    }

}
