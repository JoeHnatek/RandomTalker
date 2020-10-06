import sys
import re
import random

def main(N_GRAM_MODEL, NUM_GEN_SENT, listOfInputFiles):

	data = ""

	for i in range(len(listOfInputFiles)):

		with open(listOfInputFiles[i], 'r') as file:
			data += file.read()
	
	data = data.lower()
	
	data = re.sub(r'([.?!,]+)', r' \1', data)
	
	data = re.sub(r'([^a-z.?!,])', '\n', data)

	tokens = data.split()

	countSentences = 0

	while countSentences < NUM_GEN_SENT:
		
		word = random.choice(tokens)

		match = re.match(r'[.?!]', word)

		if match:
			countSentences += 1
			print(word)
		else:
			print(word, end = " ")
			

	"""
	unigramCount = {}
	
	for token in tokens:
		if token not in unigramCount:
			unigramCount[token] = 1
		else:
			unigramCount[token] += 1


	
	count = 0
	
	
	for key, value in sorted(unigramCount.items(), key=lambda x: x[1], reverse=True):
		print(key, " : ", value)
		count += value
	"""

	
	

if(__name__ == "__main__"):


	if(len(sys.argv) > 4):

		N_GRAM_MODEL = int(sys.argv[1])
		NUM_GEN_SENT = int(sys.argv[2])
		listOfInputFiles = sys.argv[3:]

		print(N_GRAM_MODEL)
		print(NUM_GEN_SENT)
		print(listOfInputFiles)
		
	else:
		print("Incorrect arguments: ngram sentences file1 file2 file...")
		exit()


	main(N_GRAM_MODEL, NUM_GEN_SENT, listOfInputFiles)
	
