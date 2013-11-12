from decimal import Decimal
from fractions import Fraction
import random


class Question:

    def __init__(self, questionType):
        #The number of total answers
        numChoices = 6
        #Give us a random number representing the number of correct answers
        numCorrect = random.randint(2, 4)
        correctAnswers = []
        incorrectAnswers = []
        print numCorrect

        #break 1 into x amount of sections(number of correct answers)
        section = float(1) / float(numCorrect)

        #generate the correct answers (pulls out a chunk from section)
        for i in range(0, numCorrect):
            fraction = round(random.uniform(0.1, section), 2)
            correctAnswers.append(fraction)
            print(fraction)

        print correctAnswers

        #add correct answers together to get goal decimal
        goal = sum(correctAnswers)
        print goal

        #how many incorrect answers should we generate? (toal number of questions minus correct answers)
        dummyQuestions = numChoices - numCorrect
        print dummyQuestions

        #generate dummy questions
        for i in range(0, dummyQuestions):
            fraction = round(random.uniform(0.1, 0.9), 2)
            incorrectAnswers.append(fraction)

        print incorrectAnswers
