from tokenizer import tokenize1
from decimal import *
import random
import sys

#NGram Model
#Molly Higgins and Sean Mcneil
#We have two dictionaries for the unigram, one containing the word and the number of occurences, 
#and the second containing the word and the probability it will occur, based on the total number 
#of words in the corpus and the number of times this word occurs only. 

#For the bigram model, we have three data structures:  The first is a dictionary with all the 
#bigrams and the number of times they occur. The second is a dictionary with the probability 
#each bigram will occur, given that the first word occurs (Number of times the first word occurs/number
#of times this word comes after it. The last data structure is a dictionary containing each word
#and as the value pair a second dictionary with each pair of words following it, and the number of times
#that pair happens in the corpus. This will be used in our sentence generator because it will pick a 
#starting word, look up in this layered dictionary the word and choose one of the other options based on 
#how frequently they occur. 
#For example, this may look like: { 'a' : {'a car' : 1, 'a bike' :2}, 'apple' : {'apple pie': 1, 'apple tree' : 3}}
#Thinking heavily about changing this for simplicity to instead of saying the bigram just the second word 


def ngram_prob(dict1, num_tokens):
	ngram_probabilities = {} #Returns a dictionary with each of the probabilities 
	for item in dict1: 
		ngram_probabilities[item] = Decimal(dict1[item])/Decimal(num_tokens)
	return ngram_probabilities

def ngram(Filename):
	tokens = tokenize1(Filename)
	num_tokens = 0

	num_bigrams = 0

	ngram_dict = {}
	bgram_dict = {}
	for i,val in enumerate(tokens): #Get a dictionary with each word and the number of occurrences
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

	probs = ngram_prob(ngram_dict,num_tokens)
	
	#Get probability each word occurs given the word before it. We have total occurances in unigram 
	return [ngram_dict, bgram_dict]


if __name__ == '__main__':
	try:
		unigram_name = raw_input("What would you like to name the unigram file?")
		bigram_name = raw_input("What would you like to name the bigram file?")
		f = open(sys.argv[1],'r')
		text = f.read()
		f.close()

		dict1 = ngram(text)
		z = open(unigram_name,"w")
		z.write(str(dict1[0]))
		z.close()
		y = open(bigram_name,"w")
		y.write(str(dict1[1]))
		y.close()
	except:
		print ("Please run the file in the form 'python main.py [text_file]', and please enter valid filenames")

	

