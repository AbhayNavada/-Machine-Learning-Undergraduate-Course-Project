#Implementation of Naive Bayes classifier for Text classification

#Define the training data as shown below
trainingData = [['the movie was fantastic','+'],
      		['the movie was good and engaging','+'],
      		['the movie was very good','+'],
      		['acting was nice','+'],
      		['movie was fantastic and acting was good','+'],
      		['the movie was terrible','-'],
      		['the movie was very bad','-'],
      		['the acting was bad','-'],
      		['the acting was substandard and bad','-'],
      		['the movie was not engaging enough','-']
]

#Testing data samples
test1 = ['the movie was good']
test2 = ['the movie was bad']

#Generate the vocabulary i.e the list of distinct words in the testing data
vocabulary = []

for data in trainingData:
	words = data[0].split()
	for word in words:
		wordExists = False
		for x in vocabulary:
			if(x == word):
				wordExists = True
				break
		if(wordExists == False):
			vocabulary.append(word)
print("The Vocabulary is:\n",vocabulary)

#Calculate the prior probablility of the classes
totalTrainingData = len(trainingData)
numPositive = 0
for data in trainingData:
	if (data[1] == '+'):
		numPositive += 1
numNegative = totalTrainingData - numPositive

priorProbPositive = numPositive / totalTrainingData
priorProbNegative = numNegative / totalTrainingData

print("\nPrior probability of the positive class is: ",priorProbPositive,"\nPrior probability of the negative class is: ", priorProbNegative)

#Creating positive and negative documents
positiveText = []
negativeText = []
for data in trainingData:
	words = data[0].split()
	for word in words:
		if (data[1] == '+'):
			positiveText.append(word)
		else:
			negativeText.append(word)
		
print("\nThe text belonging to the positive class is:\n",positiveText)
print("\nThe text belonging to the negative class is:\n",negativeText,"\n")

#Calculate the number of words in the positive and negative text
positiveNumber = len(positiveText)
negativeNumber = len(negativeText)

#Calculate the number of times each of the words in the vocabulary occur in the positive and negative texts
nPositive = []
nNegative = []
for x in vocabulary:
	nPositive.append(0)
	nNegative.append(0)
	for text in positiveText:
		if (x == text):
			nPositive[vocabulary.index(x)] += 1
	for text in negativeText:
		if (x == text):
			nNegative[vocabulary.index(x)] += 1
print("The number of times each word occurs in the positive document: ")
print(nPositive)
print("The number of times each word occurs in the negative document: ")
print(nNegative)

#Probabilities of the words in the vocabulary given that they belong to the +ve or -ve class
positiveProbabilities = []
negativeProbabilities = []
for x in vocabulary:
	probPos = (nPositive[vocabulary.index(x)] + 1) / (positiveNumber + len(vocabulary))
	probNeg = (nNegative[vocabulary.index(x)] + 1) / (negativeNumber + len(vocabulary))
	positiveProbabilities.append(probPos)
	negativeProbabilities.append(probNeg)
print("The probability of each word occuring in the positive document: ")
print(positiveProbabilities)
print("The probability of each word occuring in the negative document: ")
print(negativeProbabilities)

#Classifying the test example test1
testWords1 = test1[0].split()
posProb = priorProbPositive
negProb = priorProbNegative
for word in testWords1:
	for x in vocabulary:
		if(word == x):
			posProb = posProb * positiveProbabilities[vocabulary.index(word)]
			negProb = negProb * negativeProbabilities[vocabulary.index(word)]
			break
if(posProb > negProb):
	print("\n'", test1[0],"' belongs to + class\n")
else:
	print("\n'", test1[0],"' belongs to - class\n")

#Classifying the test example test2
testWords2 = test2[0].split()
posProb = priorProbPositive
negProb = priorProbNegative
for word in testWords2:
	for x in vocabulary:
		if(word == x):
			posProb = posProb * positiveProbabilities[vocabulary.index(word)]
			negProb = negProb * negativeProbabilities[vocabulary.index(word)]
			break
if(posProb > negProb):
	print("'", test2[0],"' belongs to +ve class\n")
else:
	print("'", test2[0],"' belongs to -ve class\n")
