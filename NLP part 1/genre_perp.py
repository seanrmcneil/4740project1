#!/usr/bin/env python
import math
#perplexity function

def unigram_perp(dict1, test): #dict1 is our language model and test is our test is a dictionary of the test document, with <unk> = unknown
    N = len(test)
    n_dict = len(dict1)
    total = 0.0
    for word in test:
        if word != "<unk>":
            prob = dict1[word]/ n_dict #Number of times this occured in the test divided by total number of words in the 
            total += math.log(prob)
        else:
            pass #Put probability handing for unknown words here
    e_to_n = math.exp(-total/N)
    return e_to_n


def bigram_perp(dict1,unigram_dict,test):#unigram dict just says how many times each word occurs
    N= len(test)
    n = len(dict1)
    prev_word = [] #List becuase they are mutable and strings are not
    total = 0.0
    for index,word in enumerate(test): #Are dictionaries enumerable?
        if index == 0: #Should this be the probability a word starts the sentence?
            prev_word[0] = word
        else:
            if word != "<unk>":
                if word in dict1[prev_word]: #This word has come after the prveious word before
                    total = len(dict1[prev_word[0]])
                    this = (dict1[prev_word[0]])[word] 
                    prob_this_given_prev = this/total #Probabilty this word would be said due to previous
                    prob_prev_word = unigram_dict[prev_word[0]]/n #Probabiltiy the previous word would have occured ever
                    conditional_probability = prob_this_given_prev/prob_prev_word #Double check I remember how probability works
                    total += math.log(conditional_probability)
                    prev_word[0]= word
                else:
                    prev_word[0]= word#What do you do if this word never came after the word before it in the bigram model?
            else:
                prev_word[0]= word #What to do if unknown word
    e_to_n = math.exp(-total/N)
    return e_to_n
        
                
#There are a number of ways to do this, right now I am just doing it linearly- 1 point per word match. one option I thought of 
#was to do it based on how rare the word is, but then that would catch extreme cases instead of 'rare words'. So I think the best bet
#is the ratio of how many times the word occurs in both things, but always max/min so the highest it could be is 1 if it is the same
#amount of times


def genere_classification(genre_list,test): #Genre list is a list of dictionaries in UNIGRAM form
    totals = []
    for genre_set in genre_list:
        totals.append(0) #Set it to 0 points
    for word in test: #Assume test is a dictionary of all the words in the test set
        for index,genre_dict in enumerate(genre_list):
            if word in genre_dict:
                if genre_dict[word] > test[word]:
                    totals[index] += test[word]/genre_dict[word]
                else:  
                    totals[index] += genre_dict[word]/test[word] #Calculating how similar the number of occurences are
    max_matches = 0
    for i,matches in enumerate(totals):
        if matches > max:
            max_matches = i
    return max_matches #Returns the index of genre dict with the highest probability
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        