import copy
from tokenizer import *
#practice dictionary
d = {"one": 1, "oneagain": 1, "three": 3, "four": 4, "eight" : 8, "nine": 9}
sample= {"hi": {"hey":3}, "banana": {"monkey":2}, "hey":{"ho":3, "this":1}, "monkey":{"eat":6, "loves":1}}


#Test text is not yet bigrammed, just text
def unknown_words(unigram_dict, test_txt):
	txt = tokenize1(test_txt)
	for index,word in enumerate(txt):
		if not word in unigram_dict: # if its an unknown word
			txt[index]= "<UNK>"
	return txt



def unknown_bigrams(bigram_dict,test_dict):
	test_dict2 = copy.deepcopy(test_dict)
	for item in test_dict:
		if item in bigram_dict:
			for second in test_dict[item]:
				if second in bigram_dict[item]: #If this bigram exists
					pass
				else:
					if "<UNK>" in test_dict2[item]:
						test_dict2[item]["<UNK>"] += test_dict2[item][second]
					else:
						test_dict2[item]["<UNK>"] = test_dict2[item][second]
					del test_dict2[item][second] #Replace it with the word unk
		else:
			pass
	return test_dict2