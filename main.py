from tokenizer import tokenize1
from decimal import *
import random


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


def ngram_prob(dict):
	ngram_probabilities = {} #Returns a dictionary with each of the probabilities 
	for item in dict: 
		ngram_probabilities[item] = Decimal(dict[item])/Decimal(num_tokens)
	return ngram_probabilities

def ngram(Filename):
	tokens = tokenize1(Filename)
	num_tokens = 0
	num_bigrams = 0
	#works for unigrams and bigrams
	ngram_dict = {}
	for i,val in enumerate(tokens): #Get a dictionary with each word and the number of occurrences
		#unigram
		num_tokens += 1 #Counting the number of items in the list now instead of doing it later
		if val in ngram_dict:
			ngram_dict[val] += 1
		else:
			ngram_dict[val] = 1
		#bigram 
		#Make sure it is not in the last word so i+1 doesnt fail
		if val + ' ' + tokens[i + 1] in ngram_dict:
			ngram_dict[tokens[i] + ' ' + tokens[i + 1]] += 1
		else:
			ngram_dict[tokens[i] + ' ' + tokens[i + 1]] = 1
			
	#Get probability each word occurs (Unigram)
	probs = ngram_prob(dict)
	
	#Get probability each word occurs given the word before it. We have total occurances in unigram 
	print (ngram_dict)
	
	
def bigram(dict, text):
	bigram_final = {}
	bigram_probabilities = {}
	sentence_generator_info = {}
	for word in dict:
		temp_bgram = {}
		for index, second_word in enumerate(text): 
			if second_word == word:
				phrase = word + text[index+1] #Add the bigram to the temporary dictionary with the number of occurences
				if phrase in temp_bgram:
					temp_bgram[phrase] += 1
				else:
					temp_bgram[phrase] = 1
		for bgram in temp_bgram:
			bigram_final[bgram] = temp_bgram[bgram]
			bigram_probabilities = Decimal(temp_bgram[bgram])/Decimal(dict[word]) #Probability this combo happens given the number of times the first word happened
		sentence_generator_info[word] = temp_bgram #Store the temporary bigram dictionary as a reference for the words that come up after this one for a sentence generator 
		
		
		#Do the probability math here, given word 1 was said what is the probability that the second word was said
				
		

#create a list with the unigram/bigram and the probability that it appears in a second list at the corresponding index
#but to do this, we need to know whether each key is a unigram or bigram and the current dictionary won't tell us that
#possible hacky solution: 2 dictionaries

def bigram_random_sentence(sentence_gen_info, current_word, words_left, sentence): #Work on this later when I have a user interface to work with
	possible_words = sentence_gen_info[current_word]
	if not empty(possible_words):
		random.choice(sentence_gen_info.keys()) #Right now just pick a random word that could come after it
	else:
		random.choice(sentence_gen_info.keys())
	


ngram('test_tokenizer.txt')
#Use these in Main 
	#random_start = random.choice(sentence_gen_info.keys()) #Pick a random place to start
	#random_length = random.randint(5,20) #Pick a random setence length from 5 words to 20 words
	