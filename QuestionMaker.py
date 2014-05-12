from decimal import Decimal
from fractions import Fraction
import random


class QuestionMaker:

	def __init__(self,questionType):
		self.init();

	def init(self):
		self.numChoices = 3
		self.mixedAnswers = []
		self.correctAnswerSet = []
		self.goalFractFraction = []

	def genNumCorrect(self, level):
		#lessen number of correct answers if level four (three?) or lower.
		if(level < 3) :return 1;
		return random.randint(1, 3)
		
	def getChoices(self):
		return self.mixedAnswers
	
	def getAnswers(self):
		return self.correctAnswerSet
		
	def getAnswerNum(self):
		return self.goalFractFraction

	def makeNextQuestion(self, level):
		#clear your answerSet and instantiate necessary temporary variables
		self.init()
		self.correctAnswerSet = []
		correctAnswers = []
		incorrectAnswers = []
		numCorrect = self.genNumCorrect(level)
		numIncorrect = self.numChoices - numCorrect
		remainingInCorrect = numCorrect
		
		#generate non-zero goal numerator
		goal = random.randint(6, 39)
		goalMod = goal % 2
		if(goalMod != 0) :
			goal = goal - 1
		
		#Turn goal into a fraction, and reduce it an arbitrary amount.
		cont = False
		extra = 0
		goalNumer = goal
		goalDenom = 40
		goalMod = 0
		
		while(cont == False) :
			# randomly leave fraction unreduced
			extra = random.randint(1,3)
			if(extra <= 2) :
				#is the value and the denominator divisible by five?
				goalMod = goalNumer % 5
				if(goalMod == 0) :
					goalMod = denom % 5
					if(goalMod == 0) :
						#both are divisible by 5. Reduce, then repeat the loop.
						goalNumer = goalNumer / 5
						goalDenom = goalDenom / 5
					else: 
						#check if they are divisible by two instead.
						goalMod = goalNumer % 2
						if(goalMod == 0) :
							goalMod = goalDenom % 2
							if(goalMod == 0) :
								#both are divisible by two. Reduce, then repeat the loop.
								goalNumer = goalNumer / 2
								goalDenom = goalDenom / 2
							else: 
								# denominator not divisible by two. Can't be reduced further.
								cont = True
						else:
							#value not divisible by two. Can't be reduced further.
							cont = True
				else:
					#The value was not divisible by five. Check for divisible by two.
					goalMod = goalNumer % 2
					if(goalMod == 0) :
						goalMod = goalNumer % 2
						if(goalMod == 0) :
							# Both are divisible by two. Reduce and repeat loop.
							goalNumer = goalNumer / 2
							goalDenom = goalDenom / 2
						else:
							# denom not divisible by two. Can't be reduced further.
							cont = True
					else:
						# Value can't be divided by two. Can't be reduced further.
						cont = True
			else: cont = True
		
		
		
		#save the goal fraction
		self.goalFractFraction.append(goalNumer)
		self.goalFractFraction.append(goalDenom)
		#self.goalFract = float(goal) / 40.0
		
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
			
			#Now turn the denominator and value into a pair.
			tempArray = []
			tempArray.append(value)
			tempArray.append(denom)
			#tempArray = str(value) + "/" + str(denom)
			correctAnswers.append(tempArray)
			
		
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
			tempArray = []
			tempArray.append(value)
			tempArray.append(denom)
			#tempString = str(value) + "/" + str(denom)
			incorrectAnswers.append(tempArray)
		
		#self.correctAnswerSet.extend(correctAnswers) 
		#Now mix the answers together to ensure that one can't guess based on order.
		remainingVars = self.numChoices
		intendedAnsArray = []
		for i in range(1,self.numChoices + 1):
			
			nextIndex = random.randint(1,remainingVars)
			
			if(nextIndex > remainingInCorrect) :
				# use an incorrect Answer
				nextIndex = nextIndex - (remainingInCorrect + 2)
				intendedAnsArray.append(False)
				self.mixedAnswers.append(incorrectAnswers.pop(nextIndex))
			else:
				# use a correct Answer
				nextIndex = nextIndex - 1
				intendedAnsArray.append(True)
				self.mixedAnswers.append(correctAnswers.pop(nextIndex))
				remainingInCorrect = remainingInCorrect - 1
				
			remainingVars = remainingVars - 1
		
		self.correctAnswerSet.append(intendedAnsArray)
		


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
