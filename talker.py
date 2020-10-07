import sys
import re
import random

INTRO = "This program generates {} random sentence(s) based on a {}-gram model. CS4242 by Joseph Hnatek"

def getData(N_GRAM_MODEL, listOfInputFiles):
	
	data = ""

	for i in range(len(listOfInputFiles)):

		with open(listOfInputFiles[i], 'r') as file:
			data += file.read()

	data = data.lower()

	data = re.sub(r'([.?!,]+)', r' \1', data)

	data = re.sub(r'([^a-z.?!,])', '\n', data)

	tokens = data.split()

	if(N_GRAM_MODEL == 2 or N_GRAM_MODEL == 3):

		if N_GRAM_MODEL == 2:
			step = N_GRAM_MODEL - 1
		else:
			step = N_GRAM_MODEL - 2

		newTokens = []

		for i in range(0, len(tokens), step):
			newTokens.append(' '.join(tokens[i : i + N_GRAM_MODEL]))
	
		return newTokens # Return for bigram and trigram

	return tokens # Return for unigram

def getNgramCounts(tokens):

	ngramCount = {}

	for token in tokens:
		token = token.split()
		id = ' '.join(token[:-1])
		next = token[-1]

		if id not in ngramCount:
			ngramCount[id] = {}
		
		if next not in ngramCount[id]:
			ngramCount[id][next] = 1
		else:
			ngramCount[id][next] += 1

	#print(ngramCount)

	return ngramCount

def getNumberOfTokens(tokens):
	ngramCount = {}
	
	for token in tokens:
		if token not in ngramCount:
			ngramCount[token] = 1
		else:
			ngramCount[token] += 1

	count = 0
	
	for key, value in sorted(ngramCount.items(), key=lambda x: x[1], reverse=True):
		#print(key, " : ", value)
		count += value
	
	#print("Tokens: {}".format(count))

	return count

def ngram(N_GRAM_MODEL, NUM_GEN_SENT, tokens, ngram):

	countSentences = 0

	word = random.choice(list(ngram.keys()))
	
	if N_GRAM_MODEL == 3:
		temp = word 
	else: 
		temp = None

	while countSentences < NUM_GEN_SENT:

		punctionMatch = re.search(r'[.?!]+', word)

		if punctionMatch:
			countSentences += 1
			print(word)
		else:
			print(word, end = " ")
			
			
		if N_GRAM_MODEL == 1:
			word = random.choice(tokens)

		elif N_GRAM_MODEL == 2:
			word = random.choice(list(ngram[word].keys())) # Next word

		elif N_GRAM_MODEL == 3:

			word = random.choice(list(ngram[temp].keys()))
			temp = temp.split()[1] + " " + word
			
		else:
			print("What did you just do...")
			exit()




if(__name__ == "__main__"):


	if(len(sys.argv) > 3):

		N_GRAM_MODEL = int(sys.argv[1])
		NUM_GEN_SENT = int(sys.argv[2])
		listOfInputFiles = sys.argv[3:]

		print(INTRO.format(NUM_GEN_SENT, N_GRAM_MODEL))

		data = getData(N_GRAM_MODEL, listOfInputFiles)
		
		getNumberOfTokens(data)
		
		ngramCount = getNgramCounts(data)

		if(N_GRAM_MODEL == 1):
			ngram(N_GRAM_MODEL, NUM_GEN_SENT, data, ngramCount)
		elif(N_GRAM_MODEL == 2):
			ngram(N_GRAM_MODEL, NUM_GEN_SENT, data, ngramCount)
		elif(N_GRAM_MODEL == 3):
			ngram(N_GRAM_MODEL, NUM_GEN_SENT, data, ngramCount)
		else:
			print("Incorrect arguments: (1, 2, 3) num_sentences file1 file2 file...")
			exit()
	else:
		print("Incorrect arguments: ngram sentences file1 file2 file...")
		exit()
