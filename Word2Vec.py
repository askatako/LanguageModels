import gensim
from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
from numpy import linalg as LA


class Word2Vec:

	def __init__(self, filepath, w2vbin):

        text = readFile(filepath)


        #text = readFile(filepath)

        self._tokens = set(word_tokenize(text))
        print(self._tokens)
        self._model = gensim.models.KeyedVectors.load_word2vec_format(w2vbin, binary=True)
        break

	def getWordVector(self, word):

        vec = self._model

        return(vec)   



    def computeVec2(self, doc):

        index_to_sting = {}
        mat = np.zeroes((len(doc), 300))

        for ind, line in enumerate(doc):

            x = line.split()

            alphabets = ["A", "B", "C"]
            vecs = {}

            for idx, word in enumerate(x[:-1]):
                vecs[alphabets[idx]] = getWordVector(word)

            index_to_sting[ind] = " ".join((words[:-1]))
            combined = vecs["B"] - vecs["A"] + vecs["C"]
            print(combined)
            break
            mat[ind, :] = combined









def getCosineSims(self, doc):


	#cosineSims = 
    	for line in doc:

    		words = line.split()
    		alphabets = ["A", "B", "C", "D"]
    		n = 0

    		vecs = {}

    		for word in words:

    			vecs[alphabets[n]] = self.getWordVector(word)
    			n +=1



def cosineSim(vec1, vec2):


	val = np.dot(vec1,vec2.T)/(LA.norm(vec1)*LA.norm(vec2))
	return val


def readFile(filepath):

    with open(filepath, "r", encoding = "utf-8") as fp:
        text = fp.read()

    return text


def readFile2(filepath):

    with open(filepath, "r", encoding = "utf-8") as fp:
        text = fp.readlines()

    return text


def main():

	filepath = 'analogy_test.txt'
	w2vbin = 'GoogleNews-vectors-negative300.bin.gz'
    m = Word2Vec(filepath, w2vbin)



if __name__ == '__main__':
	main()






