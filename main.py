from tokenizer import tokenize1


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





ngram('test_tokenizer.txt')