#Random sentence generator
import random
import sys
import ast


def bigram_random_sentence(sentence_gen_info, current_word, words_left, sentence): #Work on this later when I have a user interface to work with
	if words_left == 0:
		x = sentence[0]
		x = x[0].upper() + x[1:]
		sentence[0] = x
		return (" ".join(sentence)) + "."
	else:
		possible_words = sentence_gen_info[current_word]
		if not possible_words: #If it is empty
			new_word=random.choice(possible_words.keys()) #Right now just pick a random word that could come after it
			sentence.append(new_word)
			return bigram_random_sentence(sentence_gen_info,new_word,words_left-1,sentence)
		else:

			#HERE PUT PROBABILIY LOGIC FOR PICKING NEXT WORD 
			new_word = random.choice(sentence_gen_info.keys())
			sentence.append(new_word)
			return bigram_random_sentence(sentence_gen_info,new_word,words_left-1,sentence)



if __name__ == '__main__':
	try:
		sentence_length = raw_input("How long would you like the sentence to be?")

		f = open(sys.argv[1],'r')
		bgram_info = ast.literal_eval(f.read())
		f.close()
		random_start = random.choice(bgram_info.keys()) #Pick a random place to start

		list1 = []
		list1.append(random_start)
		sentence= bigram_random_sentence(bgram_info,random_start,int(sentence_length),list1)
		print sentence
	except:
		print "Please run the function in the form: python sentencegen.py [bigramfile], and enter a valid integer as the sentence length"