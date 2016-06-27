
import nltk
import re
import string
import unicodedata
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from langdetect import detect

class Tweet:
	'This class is for storage of Tweet data'

	def __init__(self, id=None, timestamp=None, text=None, retweet_count=None, \
				user_friends_count=None, user_followers_count=None, \
				user_statuses_count=None, topicid = None):
		self.id = id
		self.timestamp = timestamp
		self.text = text
		self.retweet_count = retweet_count
		self.user_friends_count = user_friends_count
		self.user_followers_count = user_followers_count
		self.user_statuses_count = user_statuses_count
		self.topicid = topicid

	def __str__(self):
		return self.text

	#TODO
	def similarity1(TweetA, TweetB):
		'A static method for measuring the similarity between two tweets'
		pass

	#Detect is a string all ascii
	def is_all_ascii(self, s):
    		return all(ord(c) < 128 for c in s)

    #Detect is this tweet a English tweet
	def isEnglish(self):
		
		s = self.text
		#remove non-ascii char
		#can tolerate some emoji or special symbol (the Threshold is 0.8)
		clean_s = s.encode('ascii','ignore')
		if float(len(clean_s))/float(len(s)) < 0.8:
			return False


		#langdetect
		if detect(s) != u'en':
			return False


		#detect stopwords
		'''
		language_ratios = {}

		tokens = nltk.wordpunct_tokenize(clean_s)
		words = [word.lower() for word in tokens]

		for language in stopwords.fileids():
			stopwords_set = set(stopwords.words(language))
			words_set = set(words)
			common_elements = words_set.intersection(stopwords_set)

			language_ratios[language] = len(common_elements)

		most_rated_language = max(language_ratios, key = language_ratios.get)
		most_rated_score = language_ratios[most_rated_language]
		if most_rated_language != 'english' or most_rated_score == 0:
			return False
		'''

		return True

	def isRT(self):
		if self.text[0:4] == 'RT @':
			return True
		else:
			return False

	def hasUrl(self):
		if 'http://' in self.text or 'https://' in self.text:
			return True
		else:
			return False

	def urlCount(self):
		return self.text.count('http')

	def hasHashtag(self):
		if '#' in self.text:
			return True
		else:
			return False

	def hashtagCount(self):
		return self.text.count('#')

	def remove_hyperlink(self):
		self.text = re.sub(r'http\S+', '', self.text)
		return self

	def ascii_encode(self):
		self.text = unicodedata.normalize('NFKD', self.text).encode('ascii','ignore')
		return self
	
	def remove_punctuation(self):
		self.text = self.ascii_encode().text.translate(None, string.punctuation)
		return self

	def remove_username(self):
		self.text = re.sub(r'@[^\s]+', '', self.text)
		return self

	def stem(self):
		stemmer = SnowballStemmer("english")
		self.remove_username().remove_hyperlink()
		wordlist = []
		for sentence in nltk.sent_tokenize(self.remove_punctuation().text):
			for word in nltk.word_tokenize(sentence):
				wordlist.append(stemmer.stem(word))

		return wordlist






































