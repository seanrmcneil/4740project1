from tokenizer import tokenize1
from nltk import word_tokenize


def ngram(Filename):
	tokens = tokenize1(Filename)

	#works for unigrams and bigrams
	ngram_dict = {}
	for i in range(len(tokens)-1):
		if tokens[i] in ngram_dict:
			ngram_dict[tokens[i]] += 1
		else:
			ngram_dict[tokens[i]] = 1
		if tokens[i] + ' ' + tokens[i + 1] in ngram_dict:
			ngram_dict[tokens[i] + ' ' + tokens[i + 1]] += 1
		else:
			ngram_dict[tokens[i] + ' ' + tokens[i + 1]] = 1
	print (ngram_dict)

#create a list with the unigram/bigram and the probability that it appears in a second list at the corresponding index
#but to do this, we need to know whether each key is a unigram or bigram and the current dictionary won't tell us that
#possible hacky solution: 2 dictionaries



ngram('test_tokenizer.txt')