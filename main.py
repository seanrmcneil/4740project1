from tokenizer import tokenize1


def ngram(Filename):
	tokens = tokenize1(Filename)

	#works for unigrams
	ngram_dict = {}
	for i in tokens:
		if i in ngram_dict:
			ngram_dict[i] += 1
		else:
			ngram_dict[i] = 1
	print (ngram_dict)





ngram('test_tokenizer.txt')