#!/usr/bin/env python
import math
import sys
import ast
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
    print totals
    for i,matches in enumerate(totals):
        if matches > max_matches:
            max_matches = matches
            index = i
    return index #Returns the index of genre dict with the highest probability
        
        
        
 #PROBLEM: THe test corpa should be a BIGRAM model for the bigram one, so we can see the combinations of words since order is not maintained
 #in dictionaries       
        
        
if __name__ == '__main__':
    print "Please put the sample text UNIGRAM model in  first then the genre UNIGRAM models after"
    bi = []
    f = open(sys.argv[2],'r')
    dict0= ast.literal_eval(f.read())
    f.close()
    g = open(sys.argv[3],'r')
    dict1= ast.literal_eval(g.read())
    g.close()
    h = open(sys.argv[4],'r')
    dict2= ast.literal_eval(h.read())
    h.close()
    i = open(sys.argv[1],'r')
    sample= ast.literal_eval(i.read())
    i.close()
    bi.append(dict0)
    bi.append(dict1)
    bi.append(dict2)
    print "Starting test"
    print genre_classification(bi,sample)
        
        
        
        
        
        
        
        