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

	# works for bigrams
	ngram_dict2 = {}
	for i in range(len(tokens)-1):
		if tokens[i]+' '+tokens[i+1] in ngram_dict2:
			ngram_dict2[tokens[i]+' '+tokens[i+1]] += 1
		else:
			ngram_dict2[tokens[i]+' '+tokens[i+1]] = 1
	print (ngram_dict2)




ngram('test_tokenizer.txt')