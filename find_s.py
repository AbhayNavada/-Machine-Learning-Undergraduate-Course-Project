#Implementation of the FIND-S algorithm

#Let h be the most specific hypothesis which does not accept any value
hypothesis = ['0','0','0','0','0','0']

#Define the training data as shown below
trainingData = [['Sunny','Warm','Normal','Strong','Warm','Same','+'],
      		['Sunny','Warm','High','Strong','Warm','Same','+'],
      		['Rainy','Cold','High','Strong','Warm','Change','-'],
      		['Sunny','Warm','High','Strong','Cool','Change','+'],
      		['Sunny','Warm','High','Strong','Cool','Same','+']
]

#Define a few testing data instanes as shown below
testingData = [['Sunny','Warm','Normal','Strong','Cool','Change'],
		['Rainy','Warm','High','Strong','Warm','Change']
]

#Check if the current training or testing example satisfies the current hypothesis
def isConsistent(hypothesis, data, isTrainingData):
    if ((isTrainingData == True and len(hypothesis) != len(data)-1) or (isTrainingData == False and len(hypothesis) != len(data))):
        print('Mismatch in the number of attributes. Please provide data in the correct format.')
        return False
    else:        
        attrMatched = 0        
        for i in range(len(hypothesis)):            
            if ((hypothesis[i] == data[i]) | (hypothesis[i] == '?')):
                attrMatched += 1   
        if attrMatched == len(hypothesis):
            return True
        else:
            return False

#Generalize the current hypothesis to accomodate the training example
def makeConsistent(hypothesis, data):    
    for i in range(len(hypothesis)):
        if((hypothesis[i] == '0')):
            hypothesis[i] = data[i]
        elif(hypothesis[i] != data[i]):
            hypothesis[i] = '?'
    return hypothesis

print('Most specific hypothesis: ', hypothesis)
print()

#Constructing the maximally specific hypothesis
for data in trainingData:    
    if data[len(data)-1] == '+':				#FIND-S only considers +ve training examples and ignores the -ve training examples
        if (isConsistent(hypothesis, data, True)):
            print("Training Data :", data)
            print('This instance is already consistent with the hypothesis. The unupdated hypothesis is: ', hypothesis)
        else:
            hypothesis = makeConsistent(hypothesis, data)
            print('Training data: ', data)
            print('Updated Hypothesis: ', hypothesis)
    elif data[len(data)-1] == '-':
    	print("Training Data :", data)
    	print("This instance has been ignored since it is a -ve instance")
    print()

print('Maximally specific hypothesis for the given training data found using FIND-S algorithm is:', hypothesis)
print()

#Classifying testing examples
for data in testingData:
	print("Testing data: ", data)
	if (isConsistent(hypothesis, data, False)):
		print("This instance has been classified as +ve")
	else:
		print("This instance has been classified as -ve")
	print()
