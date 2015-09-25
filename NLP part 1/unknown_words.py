

#practice dictionary
d = {"one": 1, "oneagain": 1, "three": 3, "four": 4, "eight" : 8, "nine": 9}
sample= {"hi": {"hey":3}, "banana": {"monkey":2}, "hey":{"ho":3, "this":1, "is":1}, "monkey":{"eat":6, "loves":1}}



def unknown_words_uni(unigram_dict):
	unigram_dict_unk = unigram_dict.copy()
	unigram_dict_unk["<UNK>"] = 0

	for key, value in unigram_dict.iteritems():
		if value == 1:
			del unigram_dict_unk[key]
			unigram_dict_unk["<UNK>"] = unigram_dict_unk["<UNK>"] + 1

	return unigram_dict_unk

def unknown_words_bi(bigram_dict):
	bigram_dict_unk = bigram_dict.copy()
	bigram_dict_unk["<UNK>"] = {"<UNK>": 0}

	for key, dict2 in bigram_dict.iteritems():
		#bigram_dict_unk[key]["<UNK>"] = 0
		for name, value in dict2.items():
			if value == 1:
				del bigram_dict_unk[key][name]
				#bigram_dict_unk[key]["<UNK>"] =  bigram_dict_unk[key]["<UNK>"] + 1
				bigram_dict_unk["<UNK>"]["<UNK>"] = bigram_dict_unk["<UNK>"]["<UNK>"] + 1


	print bigram_dict_unk


unknown_words_bi(sample)