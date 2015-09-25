from tokenizer import tokenize1
from decimal import *
import random
import sys
import math


def good_turring_bigram(bigram_dict):
	Nb = count_bigrams(bigram_dict)
	# if the count is less than 5 for that bigram, apply good turing to it
	for key,dict2 in bigram_dict.iteritems():
		for name, value in dict2.iteritems():
			if value <= 5:
				dict2[name] = (float(value)+float(1))*(float(Nb["Nb{0}".format(value+1)])/float(Nb["Nb{0}".format(value)]))

	return bigram_dict


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



def ngram_prob(dict1, num_tokens):
	ngram_probabilities = {} #Returns a dictionary with each of the probabilities 
	for item in dict1: 
		ngram_probabilities[item] = Decimal(dict1[item])/Decimal(num_tokens)
	return ngram_probabilities

def ngram_test_file(Filename, ngram_dict,bgram_dict): #Takes in list so we dont need to retokenize
	tokens = Filename
	num_tokens = 0
	num_bigrams = 0
	#works for unigrams and bigrams
	for i,val1 in enumerate(tokens): #Get a dictionary with each word and the number of occurrences
		try:
			val = str(val1)
			num_tokens += 1 #Counting the number of items in the list now instead of doing it later
			if val in ngram_dict:
				ngram_dict[val] += 1
			else:
				ngram_dict[val] = 1
			if i == 0: #If it its the first word
					pass
			else:
				first_word = tokens[i-1]
				if first_word in bgram_dict:
					if val in bgram_dict[first_word]: #if the value is in the dictionary of bigrams
						bgram_dict[first_word][val] += 1
					else:
						bgram_dict[first_word][val] = 1
				else:
					bgram_dict[first_word] = {}
					bgram_dict[first_word][val] = 1
		except:
			print "Non-string parsable value; skipping"

	probs = ngram_prob(ngram_dict,num_tokens)
	
	unigram_dict = ngram_dict
	bigram_dict = good_turring_bigram(bgram_dict)

	return [unigram_dict, bigram_dict]
	
	
def get_grams(grams, index, num_files):
	if index > number_of_files -2:
		return grams
	else:
		f = open(sys.argv[index+1],'r')
		text = f.read()
		f.close()
		dict1 = ngram(text, grams[0], grams[1])
		return get_grams(dict1,index+1,num_files)