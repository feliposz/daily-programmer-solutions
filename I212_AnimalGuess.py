"""
[2015-04-29] Challenge #212 [Intermediate] Animal Guess Game

Description:

There exists a classic game which I knew by the name of "Animal". The computer would ask you to
think of an animal. If would then ask a bunch of questions that could be answered with a Yes or No.
It would then make a guess of what animal you are thinking of. If the computer was right the program
ended with smug satisfaction. If the program was wrong it would ask you type in a specific Yes/No
question about your Animal. It would then update its library of animals to include it. As it already
had a bunch of yes/no questions it would just add the final one to that animal. As you played this
game it would learn. The more you played the more animals it learned. it got better. You taught this
program. For today's challenge we will implement this game.

Input:

The program will display an intro message and then just ask a series of yes/no questions. How you
implement this interface I leave the design to you. It must prompt you with questions and you must
be able to answer yes/no.

Output:

The program will have an intro message welcoming you to the game and then ask you to think of an
animal and then proceed to start asking questions once you prompt you are ready. For this challenge
the exact design and text I leave for you to develop as part of the challenge. The computer will
continue to output questions for yes/no responses. Eventually the computer will take a guess. You
can then tell the computer by a yes/no if it was a correct guess. If the computer is correct you may
output a success message for the computer and exit. if the computer was wrong in the guess picked
you will be asked to enter your animal and a yes/no question string that would answer a "yes". The
computer program will prompt for this data and you must supply it. You are teaching the program.
Again exact design and words I leave to you to design. I give a rough example below in examples.

AI:

The requirements for this game is a learning game. Every time you play it must load contain all
previous game learning. You therefore must find a way to design and implement this. The tricky part
is what questions to ask. I leave it to you and your design to develop those initial or base
questions and then using the learned questions.

Example of Play 1:

Welcome to Animal Guess. Please think of an Animal and type "y" to proceed --> y

Is your animal a mammal? --> y
Is your animal a swimmer? --> y
Is your animal grey? --> y

I think your animal is a grey whale. Am I correct? --> n

Oh well. please help me learn. What is the name of your animal-> dolphin

What is a unique question that answers yes for dolphin -> Does your animal have high intelligence

Thank you for teaching me.

Example of Play 2:

Welcome to Animal Guess. Please think of an Animal and type "y" to proceed --> y

Is your animal a mammal? --> y
Is your animal a swimmer? --> n
Is your animal grey? --> y

I think your animal is an elephant. Am I correct? --> y

It is okay to feel bad you did not stump me. I am a computer. :)
Thank you for playing!
"""

import random
from pickle import Pickler, Unpickler

MEMORY_FILENAME = 'animal_memory.pickle'

#TODO: Generalize for a "ThingMemory"
class AnimalMemory(object):

    def __init__(self):
        """Initialize animal memory."""
        self.questions = {}

    def is_empty(self):
        """Check if memory is still empty."""
        return len(self.questions) == 0

    def guess_animal(self, question_list):
        """Try to guess an animal based on all the questions the user answered yes."""
        if len(question_list) == 0:
            return None
        candidates = set(self.questions[question_list[0]])
        for question_text in question_list:
            candidates = candidates.intersection(set(self.questions[question_text]))
            if len(candidates) < 2:
                break
        if len(candidates) == 1:
            return candidates.pop()
        return None

    def add_question(self, question_text):
        """Add a new question to the memory."""
        self.questions[question_text] = [] # TODO: Convert this to a set (need to change the pickle file saved)

    def add_animal(self, animal_name, yes_question_list):
        """Add an animal name to all the questions the player answered yes."""
        for question_text in yes_question_list:
            if animal_name not in self.questions[question_text]:
                self.questions[question_text].append(animal_name)

    def decribe_animal(self, animal_name):
        """Returns a raw description of the animal, with all the questions that answer yes for it."""
        description = []
        for question_text in self.questions:
            if animal_name in self.questions[question_text]:
                description.append(question_text)
        return description

    def other_yes_questions(self, question_answered):
        """Returns a list of questions that could also answer yes."""
        animals = set(self.questions[question_answered])
        other_list = []
        for question in self.questions:
            current_animals = set(self.questions[question])
            if animals.intersection(current_animals):
                other_list.append(question)
        return other_list

    def forget(self, animal_name, wrong_description):
        """Correct a wrong memory, removing animal name from all questions that doesn't answer yes."""
        for question in wrong_description:
            self.questions[question].remove(animal_name)

#TODO: Generalize for a "GeneralGuessingGame"
#TODO: Write docs for all methods
class AnimalGuessingGame(object):

    def __init__(self, memory):
        self.memory = memory

    def play(self):
        """Main animal guessing game loop."""
        print('Welcome to Animal Guess.')
        while True:
            welcome_answer = input('Please think of an Animal and type "y" to proceed --> ')
            if welcome_answer != 'y':
                break
            guess, yes_questions = self.try_to_guess()
            if guess:
                guess_answer = input('I think your animal is %s %s. Am I correct? --> ' % (get_article(guess), guess) )
                if guess_answer == 'y':
                    self.do_right_answer(guess, yes_questions)
                else:
                    self.do_wrong_answer(yes_questions)
            else:
                print('I have no idea what that is.')
                self.do_wrong_answer(yes_questions)

    def get_questions_to_ask(self):
        return list(self.memory.questions.keys())

    def filter_questions(self, question, questions_to_ask):
        other_questions = self.memory.other_yes_questions(question)
        questions_to_ask = list(set(questions_to_ask).intersection(set(other_questions)))
        return questions_to_ask

    def try_to_guess(self):
        guess = None
        yes_questions = []
        if not self.memory.is_empty():
            questions_to_ask = self.get_questions_to_ask()
            while len(questions_to_ask) > 0:
                rnd_question = random.randrange(len(questions_to_ask))
                question = questions_to_ask.pop(rnd_question)
                answer = input('%s? --> ' % question)
                if answer == 'y':
                    yes_questions.append(question)
                    guess = self.memory.guess_animal(yes_questions)
                    if guess:
                        break
                    questions_to_ask = self.filter_questions(question, questions_to_ask)
        return guess, yes_questions

    def do_right_answer(self, guess, yes_questions):
        self.memory.add_animal(guess, yes_questions)
        print('It is okay to feel bad you did not stump me. I am a computer. :)')
        print('Thank you for playing!')

    def do_wrong_answer(self, yes_questions):
        animal_name = input('Oh well. please help me learn. What is the name of your animal --> ').strip().lower()
        if animal_name:
            self.correct_me(animal_name)
            self.teach_me(animal_name, yes_questions)
        else:
            print("Ok, you're not sure either.")

    def correct_me(self, animal_name):
        description = self.memory.decribe_animal(animal_name)
        if description:
            print('As far as I know, %s is described as this:' % animal_name)
            for i, text in enumerate(description):
                print('(%i) %s? -> Yes' % (i, text))
            right = input('Are all of these right? -> ')
            if right == 'n':
                wrong = input('Which of them are wrong?').split()
                wrong_description = []
                for i in wrong:
                    wrong_description.append(description[int(i)])
                self.memory.forget(animal_name, wrong_description)
                print('Thank you for correcting me.')

    def teach_me(self, animal_name, yes_questions):
        question_text = input('What is a unique question that answers yes for %s -> ' % animal_name).capitalize().strip('?').strip()
        if question_text:
            yes_questions.append(question_text)
            self.memory.add_question(question_text)
            self.memory.add_animal(animal_name, yes_questions)
            print('Thank you for teaching me.')
        else:
            print("So you don't know it also.")


def get_article(noun):
    """Get the proper english article (a/an) for a noun."""
    if noun[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'


def load_memory():
    """Restores animal memory from a file (or create a new one if file not found)."""
    memory = None
    try:
        memory = Unpickler(open(MEMORY_FILENAME, 'rb')).load()
    except FileNotFoundError:
        memory = AnimalMemory()
    return memory


def save_memory(memory):
    """Saves current memory to a file."""
    Pickler(open(MEMORY_FILENAME, 'wb')).dump(memory)


def tests():
    test_memory()


def test_memory():
    """Run tests for the AnimalMemory object."""
    memory = AnimalMemory()
    assert memory.guess_animal([]) == None, 'Empty memory, empty guess list'
    memory.add_question('what?')
    assert memory.questions == {'what?': []}, 'One question added'
    memory.add_animal('it', ['what?'])
    assert memory.questions == {'what?': ['it']}, 'One question added with an animal'
    assert memory.guess_animal([]) == None, 'One animal memory, empty guess list'
    assert memory.guess_animal(['what?']) == 'it', 'One animal memory, one guess list, right answer'
    memory.add_question('when?')
    assert memory.questions['when?'] == [], 'Another question added'
    memory.add_animal('now', ['when?', 'what?'])
    assert memory.guess_animal(['when?', 'what?']) == 'now', 'Two animals, guess list, right answer'
    print('all tests passed')

#TODO: Write tests for AnimalGuessingGame
#TODO: Test inputs: with mock.patch('builtins.input', return_value='...') / mock.patch('builtins.input', side_effect=['abc', 'def'])


def main():
    memory = load_memory()
    AnimalGuessingGame(memory).play()
    save_memory(memory)


if __name__ == '__main__':
    main()
    #test()
