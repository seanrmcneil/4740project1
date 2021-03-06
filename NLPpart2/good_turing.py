#Simply replaces the counts of ngrams that occur infrequently using the good turing method
# good_turing_unigram() takes in unigram_dict which is a dictionary of unigram counts for the corpus
# good_turing_bigram() takes in a bigram)_dict which is a nested dictionary of bigram counts for the corpus

#practice dictionaries
#d = {"one": 1, "oneagain": 1, "three": 3, "four": 4, "eight" : 8, "nine": 9}
#dd = {"one one": 1, "one again": 1, "three three": 3, "four four": 4, "eight eight" : 8, "nine nine": 9}
#sample= {"hi": {"hey":3}, "banana": {"monkey":2}, "hey":{"ho":3, "this":1}, "monkey":{"eat":6, "loves":1}}

import sys
import ast
#good turing smoothing for bigrams
def good_turring_bigram(bigram_dict):
	Nb = count_bigrams(bigram_dict)
	# if the count is less than 5 for that bigram, apply good turing to it
	for key,dict2 in bigram_dict.iteritems():
		for name, value in dict2.iteritems():
			if value <= 5:
				dict2[name] = (float(value)+float(1))*(float(Nb["Nb{0}".format(value+1)])/float(Nb["Nb{0}".format(value)]))

	return bigram_dict

def good_turring_unigram(unigram_dict):
	Nu = count_unigrams(unigram_dict)

	# if the count is less than 5 for that unigram, apply good turing to it
	for key,value in unigram_dict.iteritems():
		if value <= 5:
			unigram_dict[key] = float((value+1)*((Nu["Nu{0}".format(value+1)])/(Nu["Nu{0}".format(value)])))

	return unigram_dict



def bi_total_num_tokens(dict1):
    total = 1 #Start at 1 for the first word

    for item in dict1:
        for item2 in dict1[item]:
            total += dict1[item][item2]
    return total



def count_bigrams(bigram_dict):
	#vocabulary +1 for last entry
#	print bigram_dict
	v = len(bigram_dict) + 1
	seen = bi_total_num_tokens(bigram_dict)

	Nb = {"Nb0":0, "Nb1":0, "Nb2":0, "Nb3":0, "Nb4":0, "Nb5":0, "Nb6":0}
	# create a dictionary for number of times each bigram occurs
	for i in xrange(0, 6):
		if i == 0:
			#number of unseen bigrams or bigrams of count 0
			Nb["Nb{0}".format(i)] = (v * v) - seen
		else:
			#number of bigrams of count is
			for key, dict2 in bigram_dict.iteritems():
				for name,value in dict2.iteritems():
					if value == i:
						Nb["Nb{0}".format(i)] += 1

	return Nb

def count_unigrams(unigram_dict):
	v = len(unigram_dict)
	Nu = {}
	# create a dictionary for number of times each unigram occurs
	#there are no unseen unigrams, just unknown words
	for i in xrange(1, 6):
		Nu["Nu{0}".format(i)] = sum(1 for x in unigram_dict.values() if x == i)
	return Nu

#count_bigrams(sample)
#good_turring_bigram(sample)
# good_turring_unigram(d)
if __name__ == '__main__':
	print "Making a good turning dict (Only bigrams for now)"
	f = open(sys.argv[1],'r')
	text= ast.literal_eval(f.read())
	f.close()
	#unigram_name = raw_input("What would you like to name the unigram file?")
	bigram_name = str(sys.argv[1] ) + "_SMOOTH"
	dict1= good_turring_bigram(dict(text))
	y = open(bigram_name,"w")
	y.write(str(dict1))
	y.close()
	print "Done!"