from decimal import Decimal
from fractions import Fraction
import random


class Question:

	def __init__(self,questionType):
		self.init();

	def init(self):
		self.numChoices = 5
		self.mixedAnswers = []
		self.goalFract = 0.1

<<<<<<< HEAD
		##generate the correct answers (pulls out a chunk from section)
		#for i in range(0, numCorrect):
			#fraction = round(random.uniform(0.1, section), 2)
			#correctAnswers.append(fraction)
			#print(fraction)

		#print correctAnswers

		##add correct answers together to get goal decimal
		#goal = sum(correctAnswers)
		#print goal

		##how many incorrect answers should we generate? (toal number of questions minus correct answers)
		#dummyQuestions = numChoices - numCorrect
		#print dummyQuestions

		##generate dummy questions
		#for i in range(0, dummyQuestions):
			#fraction = round(random.uniform(0.1, 0.9), 2)
			#incorrectAnswers.append(fraction)

		#print incorrectAnswers
=======
	def getNumCorrect(self, level):
		#lessen number of correct answers if level four (three?) or lower.
		if(level < 3) :return 2;
		return random.randint(2, 4)
>>>>>>> 205d1b70c28c7c35a1f5754d590f832b312bef39

	def makeAddQuest(self, level):
		#clear your answerSet and instantiate necessary temporary variables
		self.init()
		correctAnswers = []
		incorrectAnswers = []
		numCorrect = self.getNumCorrect(level)
		numIncorrect = self.numChoices - numCorrect
		remainingInCorrect = numCorrect
		
		#generate non-zero goal numerator
		goal = random.randint(8, 39)
		goalMod = goal % 2
		if(goalMod != 0) :
			goal = goal - 1
		
		#save the goal fraction's float value
		self.goalFract = float(goal) / 40.0
		
		#generate correct Answers that add up to goal
		for i in range(1,numCorrect + 1):
			#more temp variables (ones that are reset each round)
			value = 0
			valueMod = 0
			extra = 0
			denom = 40
			
			if(i != numCorrect) :
				#insure we don't have any fractions that are equal to zero and are at least reduce-able once 
				value = random.randint(2, (goal - (2 * (numCorrect - i))))
				valueMod = value % 2
				
				if(valueMod != 0) :
					value = value - 1
			else :
				value = goal
			
			#subtract our value from the goal before we change it to a fraction
			goal = goal - value
			
			#get a denominator and numerator value (maximum is fortieths)
			extra = 0
			cont = False
			
			while(cont == False) :
				#randomly leave fraction unreduced
				extra = random.randint(1,3)

				if(extra <= 2) :
					#is the value and the denominator divisible by five?
					valueMod = value % 5
					if(valueMod == 0) :
						valueMod = denom % 5
						if(valueMod == 0) :
							#both are divisible by 5. Reduce, then repeat the loop.
							value = value / 5
							denom = denom / 5
						else: 
							#check if they are divisible by two instead.
							valueMod = value % 2
							if(valueMod == 0) :
								valueMod = denom % 2
								if(valueMod == 0) :
									#both are divisible by two. Reduce, then repeat the loop.
									value = value / 2
									denom = denom / 2
								else: 
									# denominator not divisible by two. Can't be reduced further.
									cont = True
							else:
								#value not divisible by two. Can't be reduced further.
								cont = True
					else:
						#The value was not divisible by five. Check for divisible by two.
						valueMod = value % 2
						if(valueMod == 0) :
							valueMod = value % 2
							if(valueMod == 0) :
								# Both are divisible by two. Reduce and repeat loop.
								value = value / 2
								denom = denom / 2
							else:
								# denom not divisible by two. Can't be reduced further.
								cont = True
						else:
							# Value can't be divided by two. Can't be reduced further.
							cont = True
				else: cont = True
			
			#Now turn the denominator and value into a string for a fraction 
			tempString = str(value) + "/" + str(denom)
			correctAnswers.append(tempString)
			
		
		#generate potentially incorrect answers
		for i in range(1,numIncorrect + 1):
			#more temp variables (ones that are reset each round)
			value = 0
			valueMod = 0
			extra = 0
			denom = 40
			
			#make a fraction that is at least reduce-able once and not equal to zero
			value = random.randint(2, 39)
			valueMod = value % 2
			
			if(valueMod != 0) :
				value = value - 1
			
			#get a denominator and numerator value (maximum is fortieths)
			extra = 0
			cont = False
			
			while(cont == False) :
				#randomly leave fraction unreduced
				extra = random.randint(1,3)

				if(extra <= 2) :
					#is the value and the denominator divisible by five?
					valueMod = value % 5
					if(valueMod == 0) :
						valueMod = denom % 5
						if(valueMod == 0) :
							#both are divisible by 5. Reduce, then repeat the loop.
							value = value / 5
							denom = denom / 5
						else: 
							#check if they are divisible by two instead.
							valueMod = value % 2
							if(valueMod == 0) :
								valueMod = denom % 2
								if(valueMod == 0) :
									#both are divisible by two. Reduce, then repeat the loop.
									value = value / 2
									denom = denom / 2
								else: 
									# denominator not divisible by two. Can't be reduced further.
									cont = True
							else:
								#value not divisible by two. Can't be reduced further.
								cont = True
					else:
						#The value was not divisible by five. Check for divisible by two.
						valueMod = value % 2
						if(valueMod == 0) :
							valueMod = value % 2
							if(valueMod == 0) :
								# Both are divisible by two. Reduce and repeat loop.
								value = value / 2
								denom = denom / 2
							else:
								# denom not divisible by two. Can't be reduced further.
								cont = True
						else:
							# Value can't be divided by two. Can't be reduced further.
							cont = True
				else: cont = True
			
			#Now turn the denominator and value into a string for a fraction 
			tempString = str(value) + "/" + str(denom)
			incorrectAnswers.append(tempString)
		
		#Now mix the answers together to ensure that one can't guess based on order.
		remainingVars = self.numChoices
		for i in range(1,self.numChoices + 1):
			
			nextIndex = random.randint(1,remainingVars)
			
			if(nextIndex > remainingInCorrect) :
				nextIndex = nextIndex - (remainingInCorrect + 2)
				self.mixedAnswers.append(incorrectAnswers.pop(nextIndex))
			else:
				nextIndex = nextIndex - 1
				self.mixedAnswers.append(correctAnswers.pop(nextIndex))
				remainingInCorrect = remainingInCorrect - 1
				
			remainingVars = remainingVars - 1
		


#def __init__(self,questionType):
		##The number of total answers
		##Give us a random number representing the number of correct answers
		#numCorrect = random.randint(2, 4)
		#correctAnswers = []
		#incorrectAnswers = []
		#print numCorrect

		##break 1 into x amount of sections(number of correct answers)
		#section = float(1) / float(numCorrect)

		##generate the correct answers (pulls out a chunk from section)
		#for i in range(0, numCorrect):
			#fraction = round(random.uniform(0.1, section), 2)
			#correctAnswers.append(fraction)
			#print(fraction)

		#print correctAnswers

		##add correct answers together to get goal decimal
		#goal = sum(correctAnswers)
		#print goal

		##how many incorrect answers should we generate? (toal number of questions minus correct answers)
		#dummyQuestions = numChoices - numCorrect
		#print dummyQuestions

		##generate dummy questions
		#for i in range(0, dummyQuestions):
			#fraction = round(random.uniform(0.1, 0.9), 2)
			#incorrectAnswers.append(fraction)

		#print incorrectAnswers
