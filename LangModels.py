"""
This python script constructs a unigram language model and then calculates the 
probabilities for the unigram language model
"""

import math 

BEGINNING_OF_SENTENCE = "<s>"
END_OF_SENTENCE = "</s>"

class UnigramLM:
	
	def __init__(self, corpus):

		sentences = readFile(corpus)
		self._tokens, self._num_words = makeUnigramTokens(sentences)

	def calculateWordProb(self, word):

		"""
		This function calculates the log probability of a word relative
		to the corpus.

		Input
		------
		- word: the word that the probability is to be determined

		Output
		------
		- prob: the probability of the word

		"""

		if word not in self._tokens:
			return(0)

		value = self._tokens.get(word) + self._tokens.get(addStopper(word), 0) \
		+ self._tokens.get(addStarter(word), 0)

		return value/self._num_words



	def generateRandomUnigramSentences(self, seed):
		pass


#probabilities should be in the log space


#random sentence generator

#unigram
#Choose a random value between 0 and 1 and print the word whose interval includes
#this value. Keep choosing words until we generate sentence stopper



class BigramLM(UnigramLM):
	
	def __init__(self, corpus):

		super().__init__(corpus)

		#make bigram tokens

		sentences = readFile(corpus)
		self._bigrams = makeBigrams(sentences)


	def calculateBigramProb(self, bigram):
		"""
		This function calculates the probability of a bigram relative
		to all the bigrams that share the same start word.

		Input
		------
		- bigram: the bigram that the probability is to be determined

		Output
		------
		- prob: the probability of the bigram

		"""

		if bigram not in self._bigrams:
			return(0)

		value = self._bigrams[bigram]

		firstWord = bigram.split()[0]
		den = self._tokens[firstWord] + self._tokens.get(addStarter(firstWord),0) \
		+ self._tokens.get(addStopper(firstWord),0)

		return value/den




## COUNT OF BEG AND END NOT IN ORIGINAL DICT


def readFile(file):

	"""
	Reads a text file and returns a list of paragraphs
	"""

	with open(file, "r") as fp:
		text = fp.readlines()

	return text


def addStarter(word):
	
	"""
	Returns a start word with start word symbol appended
	"""

	return BEGINNING_OF_SENTENCE + word


def addStopper(word):

	"""
	Returns a stop word with stop word symbol appended
	"""
	
	return word + END_OF_SENTENCE

def makeUnigramTokens(sentences):

	tokens = {BEGINNING_OF_SENTENCE:0, END_OF_SENTENCE:0}
	numWords = 0

	for line in sentences:

		words = line.split()
		n = len(words)
		numWords += n

		words[0] = addStarter(words[0])
		words[n-1] = addStopper(words[n-1])

		for word in words:

			if word not in tokens:
				tokens[word] = 1
			else:
				tokens[word] += 1

		tokens[BEGINNING_OF_SENTENCE] += 1
		tokens[END_OF_SENTENCE] += 1

	return tokens, numWords



def makeBigrams(sentences):

	pairs = {}

	for line in sentences:

		words = line.split()

		words.insert(0, BEGINNING_OF_SENTENCE)
		words.insert(len(words), END_OF_SENTENCE)

		for i in range(len(words[:-1])):

			bigram = "{} {}".format(words[i], words[i+1])

			if bigram not in pairs:
				pairs[bigram] = 1
			else:
				pairs[bigram] += 1

	return pairs



def main():
	file = "analogy_test.txt"
	tt = BigramLM(file)
	print(tt.calculateBigramProb("his her"))





if __name__ == "__main__":
	main()













