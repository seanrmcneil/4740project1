#!/usr/bin/env python
import math
#perplexity function
from decimal import *


def uni_total_num_tokens(dict1):
    total = 0
    for item in dict1:
        total += dict1[item]
    return total

def bi_total_num_tokens(dict1):
    total = 1 #Start at 1 for the first word

    for item in dict1:
        for item2 in dict1[item]:
            total += dict1[item][item2]
    return total

def unigram_perp(dict1, test): #dict1 is our language model and test is our test is a dictionary of the test document, with <unk> = unknown
    N = float(uni_total_num_tokens(test))
    n_dict = float(uni_total_num_tokens(dict1))
    total = float(0)
    for word in test:
        if word in dict1:
            if word != "<unk>":
                prob = float(dict1[word])/float( n_dict) #Number of times this occured in the test divided by total number of words in the 
                total += -math.log(prob)
            else:
                pass #Put probability handing for unknown words here
        else:
            pass #What to do if not in lang model at all
    e_to_n = math.exp(float(total/N))
    return e_to_n



def bigram_perp(lang_model, test_model):
    lang_model_n = float(bi_total_num_tokens(lang_model))
    test_model_n = float(bi_total_num_tokens(test_model))
    final = 0
    for first_word in test_model:
        for second_word in test_model[first_word]:
            if first_word is "<unk>": #Unknown word
                pass
            elif first_word in lang_model and second_word in lang_model: #Bigram exists in model
                total = float(uni_total_num_tokens(lang_model[first_word])) #Total number times first word appears (besides last, maybe)
                this = float(lang_model[first_word][second_word]) #Number of times the second word comes after the first
                second_prob = this/total #Probability this word comes after the fist
                first_prob = total/lang_model_n #Probability the first word occured
                cond_prob = second_prob/first_prob #Conditional probability
                final += -math.log(cond_prob)
            elif first_word in lang_model and not second_word in lang_model: #Word exists in model, but not bigram
                pass
            else: #Word does not exist in model
                pass #
    e_to_n = math.exp(final/test_model_n)
    return e_to_n


                
#There are a number of ways to do this, right now I am just doing it linearly- 1 point per word match. one option I thought of 
#was to do it based on how rare the word is, but then that would catch extreme cases instead of 'rare words'. So I think the best bet
#is the ratio of how many times the word occurs in both things, but always max/min so the highest it could be is 1 if it is the same
#amount of times


#TESTED and WORKS

def genre_classification(genre_list,test): #Genre list is a list of dictionaries in UNIGRAM form
    totals = []
    for genre_set in genre_list:
        totals.append(0) #Set it to 0 points
    for word in test: #Assume test is a dictionary of all the words in the test set
        for index,genre_dict in enumerate(genre_list):
            if word in genre_dict:
                if genre_dict[word] > test[word]:
                    totals[index] += Decimal(test[word])/Decimal(genre_dict[word])
                else:  
                    totals[index] += Decimal(genre_dict[word])/Decimal(test[word]) #Calculating how similar the number of occurences are
    max_matches = 0
    index = 0
    for i,matches in enumerate(totals):
        if matches > max_matches:
            max_matches = matches
            index = i
    return index #Returns the index of genre dict with the highest probability
        
        
        
 #PROBLEM: THe test corpa should be a BIGRAM model for the bigram one, so we can see the combinations of words since order is not maintained
 #in dictionaries       
        
        
if __name__ == '__main__':
    dict1 = {"hi": 1, "hello":21, "molly": 3}
    test2 = {"hi": 1, "hello":21,"molly":3}
    test3 = {"heeey":9, "hi":1} 
    bi = {"hi":{"hey":1}}
    sample= {"hi": {"hey":3}, "hey":{"ho":3}}
    listy = []
    listy.append(dict1)
    listy.append(test2)
    listy.append(test3)
    print bigram_perp(sample,bi)
        
        
        
        
        
        
        
        