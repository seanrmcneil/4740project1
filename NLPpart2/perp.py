import sys
import ast

from gram_maker import *
from unknown_words import *


def number_unks(bigram):
    if len(bigram["<UNK>"]) == 0:
        return 1
    else:
        counter =0
        for item in bigram["<UNK>"]:
            counter += bigram['<UNK>'][item]
        return counter

def total_non_unk(lang_model, word, second):
    counter = 0
    for item in second:
        if lang_model[word][second]: #If this bigram exits
            counter += 1
    return counter

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
    unk_count = float(test["<UNK>"])/N
    n_dict = float(uni_total_num_tokens(dict1))
    total = float(0)
    for word in test:
        if word in dict1:
            if word != "<UNK>":
                prob = float(dict1[word])/float( n_dict) #Number of times this occured in the test divided by total number of words in the 
                total += -math.log(prob)
            else:
                prob = (float(dict1[word])/float( n_dict) ) / unk_count
        else:
            pass #Will never be here because it will be UNK if it wasnt in dict 1
    e_to_n = math.exp(float(total/N))
    return e_to_n



def bigram_perp(lang_model, test_model):
    lang_model_n = float(bi_total_num_tokens(lang_model))
    test_model_n = float(bi_total_num_tokens(test_model))
    unk_count = float(number_unks(test_model)) /test_model_n
    final = 0
    for first_word in test_model:
        for second_word in test_model[first_word]:
            if first_word is "<UNK>": #Unknown word
                if test_model['<UNK>']['<UNK']:
                    this = test_model[first_word][second_word]
                    total = float(uni_total_num_tokens(lang_model[first_word]))
                    second_prob = this/total #Probability this word comes after the fist
                    unk_adj = second_prob * unk_count
                    final += -math.log(unk_adj)
            elif first_word in lang_model and second_word != "<UNK>": #Bigram exists in model
                total = float(uni_total_num_tokens(lang_model[first_word])) #Total number times first word appears (besides last, maybe)
                this = float(lang_model[first_word][second_word]) #Number of times the second word comes after the first
                second_prob = this/total #Probability this word comes after the fist
                print second_prob
                final += -math.log(second_prob)
            elif first_word in lang_model and  second_word == "<UNK>": #Word exists in model, but not bigram1
                this = test_model[first_word][second_word]
                total = float(uni_total_num_tokens(lang_model[first_word]))


                second_prob = this/total #Probability this word comes after the fist
                unk_adj = second_prob * unk_count
                final += -math.log(unk_adj)
            else: #Word does not exist in model
                pass #
    e_to_n = math.exp(final/test_model_n)
    return e_to_n


if __name__ == '__main__':

    #Get the ngrams
    #Run good turing on them (included in makin them!)
    #Get the text, replace unknown words
    #Get bigram model of text
    #run this
    print "Reading the files"
    f = open(sys.argv[1],'r')
    lang_model= ast.literal_eval(f.read())
    f.close()
    g = open(sys.argv[2],'r')
    text= g.read()
    g.close()
    print "Replacing unknown words"
    unked = unknown_words(lang_model,text)
    print "Getting ngram model of test"
    test_model = ngram_test_file(unked,{},{})
    print "Replacing unknown bigrams with UNK"
    final = unknown_bigrams(lang_model,test_model[1])
    print "Perplexity:"
    print bigram_perp(lang_model,final)