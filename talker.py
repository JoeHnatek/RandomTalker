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
		newTokens = []

		for i in range(0, len(tokens), N_GRAM_MODEL):
			newTokens.append(' '.join(tokens[i : i + N_GRAM_MODEL]))
	
		return newTokens # Return for bigram and trigram

	return tokens # Return for unigram

def unigram(NUM_GEN_SENT, tokens):
	
	countSentences = 0

	while countSentences < NUM_GEN_SENT:

		word = random.choice(tokens)

		match = re.match(r'[.?!]', word)

		if match:
			countSentences += 1
			print(word)
		else:
			print(word, end = " ")
			


	unigramCount = {}
	
	for token in tokens:
		if token not in unigramCount:
			unigramCount[token] = 1
		else:
			unigramCount[token] += 1


	
	count = 0
	
	
	for key, value in sorted(unigramCount.items(), key=lambda x: x[1], reverse=True):
		#print(key, " : ", value)
		count += value
	
	print("Tokens: {}".format(count))


def nGram(NUM_GEN_SENT, tokens):

	ngramCount = {}

	for token in tokens:
		if token not in ngramCount:
			ngramCount[token] = 1
		else:
			ngramCount[token] += 1


	count = 0
	ncount = 0
	for key, value in sorted(ngramCount.items(), key = lambda x: x[1], reverse=True):
		print(key, " : ", value)
		count += value
		ncount += 1
		if ncount == 10:
			break

	print("Tokens: {}".format(count))
	
	countSentences = 0

	while countSentences < NUM_GEN_SENT:

		word = random.choice(tokens)

		match = re.match(r'[.?!]', word)

		if match:
			countSentences += 1
			print(word)
		else:
			print(word, end = " ")


def main(NUM_GEN_SENT, tokens):

	countSentences = 0

	while countSentences < NUM_GEN_SENT:
		word = random.choice(tokens)

		match = re.search(r'[.?!]+', word)

		if match:
			countSentences += 1
			print(word)
		else:
			print(word, end = " ")



if(__name__ == "__main__"):


	if(len(sys.argv) > 3):

		N_GRAM_MODEL = int(sys.argv[1])
		NUM_GEN_SENT = int(sys.argv[2])
		listOfInputFiles = sys.argv[3:]

		print(INTRO.format(NUM_GEN_SENT, N_GRAM_MODEL))

		data = getData(N_GRAM_MODEL, listOfInputFiles)
	
		if(N_GRAM_MODEL == 1):
			main(NUM_GEN_SENT, data)
		elif(N_GRAM_MODEL == 2):
			main(NUM_GEN_SENT, data)
		elif(N_GRAM_MODEL == 3):
			main(NUM_GEN_SENT, data)
		else:
			print("Incorrect arguments: (1, 2, 3) num_sentences file1 file2 file...")
			exit()
	else:
		print("Incorrect arguments: ngram sentences file1 file2 file...")
		exit()
