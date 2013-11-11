from decimal import Decimal
from fractions import Fraction
import random


class Question:

    def __init__(self, questionType):
        numChoices = 6
        numCorrect = random.randint(2, 4)
        correctAnswers = []
        incorrectAnswers = []
        print numCorrect

        section = float(1) / float(numCorrect)

        for i in range(0, numCorrect):
            fraction = round(random.uniform(0.1, section), 2)
            correctAnswers.append(fraction)
            print(fraction)

        print correctAnswers

        goal = sum(correctAnswers)
        print goal

        dummyQuestions = numChoices - numCorrect
        print dummyQuestions

        for i in range(0, dummyQuestions):
            fraction = round(random.uniform(0.1, 0.9), 2)
            incorrectAnswers.append(fraction)

        print incorrectAnswers
