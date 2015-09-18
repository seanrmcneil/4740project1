#Random sentence generator
import random
import sys
import ast

def choose_word(dict1):
    max = 0
    best = [""] #String immutable in python so use a list
    for item in dict1:
        if dict1[item] > max:
            best[0] = item
    return best[0]


def bigram_random_sentence(sentence_gen_info, current_word, words_left, sentence): #Work on this later when I have a user interface to work with
	if words_left == 0:
		x = sentence[0]
		x = x[0].upper() + x[1:]
		sentence[0] = x
		return (" ".join(sentence)) + "."
	else:
		possible_words = sentence_gen_info[current_word]
		if not possible_words: #If it is empty
			new_word = random.choice(sentence_gen_info.keys())
			sentence.append(new_word)
			return bigram_random_sentence(sentence_gen_info,new_word,words_left-1,sentence)
		else:
			new_word=choose_word(possible_words) #Right now just pick the most commonly used word in the dictionary
			sentence.append(new_word)
			return bigram_random_sentence(sentence_gen_info,new_word,words_left-1,sentence)

def unigram_rand_sentence(sentence_gen_info, current_word, words_left, sentence):
		if words_left == 0:
			x = sentence[0]
			x = x[0].upper() + x[1:]
			sentence[0] = x
			return(" ".join(sentence)) + "."
		else:
			new_word = random.choice(sentence_gen_info.keys()) #Just pick a random word
			sentence.append(new_word)
			return unigram_rand_sentence(sentence_gen_info,new_word,words_left-1,sentence)



if __name__ == '__main__':
	try:
		sentence_length = raw_input("How long would you like the sentence to be?")
		uni_or_bi = raw_input("Unigram or Bigram? Please type U for uni, default is bigram")

		f = open(sys.argv[1],'r')
		bgram_info = ast.literal_eval(f.read())
		f.close()
		random_start = random.choice(bgram_info.keys()) #Pick a random place to start

		list1 = []
		list1.append(random_start)
		if uni_or_bi == "U":
			sentence = unigram_rand_sentence(bgram_info,random_start,int(sentence_length),list1)
			print sentence
		else:
			sentence= bigram_random_sentence(bgram_info,random_start,int(sentence_length),list1)
			print sentence
	except:
		print "Please run the function in the form: python word_gen.py [bigramfile], and enter a valid integer as the sentence length"