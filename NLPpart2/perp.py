import sys
import ast

from gram_maker import *

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
            elif first_word in lang_model and second_word in lang_model[first_word]: #Bigram exists in model
                total = float(uni_total_num_tokens(lang_model[first_word])) #Total number times first word appears (besides last, maybe)
                this = float(lang_model[first_word][second_word]) #Number of times the second word comes after the first
                second_prob = this/total #Probability this word comes after the fist
                final += -math.log(second_prob)
            elif first_word in lang_model and not second_word in lang_model[first_word]: #Word exists in model, but not bigram
                pass
            else: #Word does not exist in model
                pass #
    e_to_n = math.exp(final/test_model_n)
    return e_to_n


if __name__ == '__main__':
    print "Returning the perplexity"
    f = open(sys.argv[1],'r')
    lang_model= ast.literal_eval(f.read())
    f.close()
    g = open(sys.argv[2],'r')
    text= g.read()
    g.close()
    test_model = ngram(text,{},{})
    print bigram_perp(lang_model,test_model[1])