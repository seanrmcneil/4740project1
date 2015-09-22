

#practice dictionary
d = {"one": 1, "oneagain": 1, "three": 3, "four": 4, "eight" : 8, "nine": 9}
dd = {"one one": 1, "one again": 1, "three three": 3, "four four": 4, "eight eight" : 8, "nine nine": 9}

#good turing smoothing for unigrams
def gt_unigram(unigram_dict):
	#if the count is less than 5 for that unigram apply good turing to it
	for key,value in unigram_dict.iteritems():
		if value <= 5:
			unigram_dict[key] = (value +1)

	return

#good turing smoothing for bigrams
def gt_bigram(unigram_dict, bigram_dict):

	N = count_bigrams(unigram_dict, bigram_dict)

	# if the count is less than 5 for that bigram, apply good turing to it
	for key,value in bigram_dict.iteritems():
		if value <= 5:
			bigram_dict[key] = (value+1)((N["N{0}".format(value+1)])/(N["N{0}".format(value)]))

	return

def count_bigrams(unigram_dict, bigram_dict):
	v = len(unigram_dict)
	seen = len(bigram_dict)
	N = {}
	# create a dictionary for number of times each bigram occurs
	for i in xrange(0, 5):
		if i == 0:
			#number of unseen bigrams or bigrams of count 0
			N["N{0}".format(i)] = (v * v) - seen
		else:
			N["N{0}".format(i)] = sum(1 for x in bigram_dict.values() if x == i)
	print N

count_bigrams(d, dd)