

#practice dictionary
d = {"one": 1, "oneagain": 1, "three": 3, "four": 4, "eight" : 8, "nine": 9}
dd = {"one one": 1, "one again": 1, "three three": 3, "four four": 4, "eight eight" : 8, "nine nine": 9}


def unknown_words(unigram_dict, bigram_dict):
	unigram_dict_unk = unigram_dict.copy()
	unigram_dict_unk["<UNK>"] = 0

	for key, value in unigram_dict.iteritems():
		if value == 1:
			del unigram_dict_unk[key]
			unigram_dict_unk["<UNK>"] = unigram_dict_unk["<UNK>"] + 1


	return unigram_dict_unk

	bigram_dict_unk = bigram_dict.copy()
	bigram_dict_unk["<UNK>"] = 0

	for key, value in bigram_dict.iteritems():
		if value == 1:
			del bigram_dict_unk[key]
			bigram_dict_unk["<UNK>"] = bigram_dict_unk["<UNK>"] + 1

	return bigram_dict_unk

unknown_words(d, dd)