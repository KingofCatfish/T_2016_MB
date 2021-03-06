import json
import nltk
from nltk.stem.snowball import SnowballStemmer

class Early_detection():

	def __init__(self):
		f = open('./detection/'+'203_terms_stem.txt')
		"""
		 NO stop word 
		 All stem
		 All lower
		 Maybe Maybe Maybe All from title
		"""
		terms = json.loads(f.read())
		f.close()
		self.terms_set = set(terms)
		self.tknz = nltk.word_tokenize

		self.stemmer = SnowballStemmer('english')
		

	def early_topic_detection(self, text):
		tokens = self.tknz(text)

		tokens_text = [self.stemmer.stem(token) for token in tokens]
		for token in tokens_text:
			if token in self.terms_set:
				return True, token
		return False, None

if __name__ == '__main__':
	ed = Early_detection()

	print ed.early_topic_detection(" mother impact drought ttt california's kobe daily")
	

		