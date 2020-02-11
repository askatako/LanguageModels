
import numpy as np

class Dependency:

    def __init__(self, filepath):

        text = readFile(filepath)
        self._mat, self._tokens = makeTokens(text)
        
    def getTokens(self):
        return self._tokens
    
    def getMat(self):
        return self._mat


def makeTokens(doc):

    n = len(doc)
    d = getlength(doc[0].split())

    mat = np.zeros((n,d))
    tokens = {}

    for idx, item in enumerate(doc):
        vecs = item.split()
        tokens[idx] = vecs[0]
        mat[idx, :] = np.array(vecs[1:])

    return mat, tokens



def getlength(lstOfWords):

    return(len(lstOfWords)-1)


def readFile(filepath):

    with open(filepath, "r", encoding = "utf-8") as fp:
        text = fp.readlines()

    return text

 
def main():

    filepath = 'deps.words'
    
    m = Dependency(filepath)
    tokens = m.getTokens()
    matrix m.getMat()


if __name__ == '__main__':
    main()





