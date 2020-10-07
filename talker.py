"""
Written by: Joseph Hnatek
Date: Oct. 5, 2020

== OVERALL ==
The ngram generates random words to create a sentence.
Ngram is given the model, number of sentences to generate, tokens, and ngram counts.
The program will then output words based on the model and probabilities.

== EXAMPLE ==
talker.py 3 2 data/1399-0.txt data/2554-0.txt data/2600-0.txt

> This program generates 2 random sentence(s) based on a 3-gram model. CS4242 by Joseph Hnatek
> russian regiment preparing for bed .
> often levin had , or all this suggested an advance nor a single division .


== ALGORITHM ==
Read the file(s) given from the user.
Note the ngram model and number of sentences to generate.
Based on the ngram model, tokenize, then create the ngram count dictionary.
Based on the ngram model, generate the words and output them to create a sentence.
Once the number of sentences have been met, end program.
"""


import sys
import re
import random

INTRO = "This program generates {} random sentence(s) based on a {}-gram model. CS4242 by Joseph Hnatek"

def getData(N_GRAM_MODEL, listOfInputFiles):
	"""
		getData returns the token list from the inputted files.
	"""
	
	data = "" # Set our data string to empty string

	for i in range(len(listOfInputFiles)): # For 0 to length of list of files minus 1

		with open(listOfInputFiles[i], 'r') as file: # Open the file
			data += file.read() # Concatenate the files into the data string

	data = data.lower()	# Lower the tokens.

	data = re.sub(r'([.?!,]+)', r' \1', data) 	# Add a space before punctuation.

	data = re.sub(r'([^a-z.?!,])', '\n', data)	# Replace anything that is not a alphabetic letter and punctuation to a newline.
	tokens = data.split()	# Split the data into single tokens : ["the green dog"] -> ["the", "green", "dog"]

	if(N_GRAM_MODEL == 2 or N_GRAM_MODEL == 3):	# If the ngram model is not unigram.

		if N_GRAM_MODEL == 2:
			step = N_GRAM_MODEL - 1 # Set step to 1 if bigram
		else:
			step = N_GRAM_MODEL - 2 # Set step to 2 if trigram

		newTokens = [] # List to handle the new tokens if not unigram

		for i in range(0, len(tokens), step):	# Slide across the data based on the step to gather the ngram model.

			# join the bigram or trigram model data to create a new token list
			# ex) input -> "The red fox jumped."
			# If bigram: ["The red", "red fox", "fox jumped", "jumped ."]
			# If trigram: ["The red fox", "red fox jumped", "fox jumped ."]

			newTokens.append(' '.join(tokens[i : i + N_GRAM_MODEL]))
			
	
		return newTokens # Return for bigram and trigram

	return tokens # Return for unigram

def getNgramCounts(tokens):
	"""
		getNgramCounts returns the complete dictionary of frequencies of the ngram model
		ngram structure = {"the": {"green":1, "red":1, "fox":2}, "red": {"fox":1}}
	"""
	ngramCount = {}	# Our ngram dictionary (hashmap)

	for token in tokens:	# For each token
		token = token.split()	# Split the token: ["the green"] -> ["the", "green"]
		id = ' '.join(token[:-1]) # The identifier is based on the ngram model. if ["the green"] -> id = "the"
		next = token[-1]	# Next is the word that is associated with the id for frequency.

		if id not in ngramCount:	# If ID is not in the dictionary, then add it.
			ngramCount[id] = {}
		
		if next not in ngramCount[id]:	# If the next word has not been associated with the ID, add it
			ngramCount[id][next] = 1
		else:
			ngramCount[id][next] += 1	# If the next word has been associated, add one to the count for frequency count.

	#print(ngramCount)

	return ngramCount

def getNumberOfTokens(tokens): #
	"""
		Debug code to count how many tokens we have
	"""

	ngramCount = {}
	
	for token in tokens:			# For each token, if the token is not in ngramCount, add it and set its value to 1.
		if token not in ngramCount:	# If the token is in ngramCount, add 1 to the value.
			ngramCount[token] = 1
		else:
			ngramCount[token] += 1

	count = 0
	
	for key, value in sorted(ngramCount.items(), key=lambda x: x[1], reverse=True): # Print out the dictionary in sorted order. Python does not have sorted dictionarys (Hash maps)
		#print(key, " : ", value)
		count += value
	
	print("Tokens: {}".format(count))

	return count

def ngram(N_GRAM_MODEL, NUM_GEN_SENT, tokens, ngram):
	"""
		Ngram takes in the ngram model, number of sentences, token list, and ngram count dict.
		Based on the ngram model, we generate random words based on the probability of the ngram model inside ngram count.

		ngram structure = {"the": {"green":1, "red":1, "fox":2}, "red": {"fox":1}}
	"""
	countSentences = 0

	word = random.choice(list(ngram.keys())) # Choose a random word from ngram count to start.
	
	if N_GRAM_MODEL > 2:
		prevWord = word # prevWord allows us to keep track of what words we already printed so that we don't duplicate the last word.
	else: 
		prevWord = None

	while countSentences < NUM_GEN_SENT: # While there are more sentences to generate

		punctionMatch = re.search(r'[.?!]+', word) # Check if the word contains an ending punctuation (. ? !).

		if punctionMatch: # If there is a ending punctuation.
			countSentences += 1 # Add 1 to the number of sentences generated.
			print(word)
		else:
			print(word, end = " ") # Print with no newline (\n)
			
			
		if N_GRAM_MODEL == 1:
			word = random.choice(tokens) # Choose from a random token.

		elif N_GRAM_MODEL == 2:
			word = random.choice(list(ngram[word].keys())) # Next word in bigram model

		elif N_GRAM_MODEL == 3:

			word = random.choice(list(ngram[prevWord].keys())) # store the word to output in the sentence.
			prevWord = prevWord.split()[1] + " " + word # store the previous word so we don't duplicate the last word in the output.
			
		else:
			print("What did you just do...") # This would be impossible to reach...
			exit()




if(__name__ == "__main__"):


	if(len(sys.argv) > 3): # Check if we have the right number of args.

		N_GRAM_MODEL = int(sys.argv[1]) # Set the ngram model.
		NUM_GEN_SENT = int(sys.argv[2])	# Set the number of sentences to be generated.
		listOfInputFiles = sys.argv[3:] # Set the files to a list, so we can open each one.

		print(INTRO.format(NUM_GEN_SENT, N_GRAM_MODEL), "\n") # Print intro statement.

		data = getData(N_GRAM_MODEL, listOfInputFiles) # Data contains the tokens of the input files.
		
		#getNumberOfTokens(data) # Debug code to see how many tokens we have.
		
		ngramCount = getNgramCounts(data) # Generate the ngram model count so we can randomly generate sentences.

		ngram(N_GRAM_MODEL, NUM_GEN_SENT, data, ngramCount) # Run the main function to generate the sentences.

	else:
		print("Incorrect arguments: ngram sentences file1 file2 file...") # Error handling.
		exit()
