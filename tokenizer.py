from nltk import word_tokenize

#takes the File of "raw text"
#makes everything lowercase
#
#need to ignore ' if in the case of don't, can't, won't .replace('\'','') makes it dont, cant, wont
def tokenize1(Filename):
	document = open(Filename)
	test = document.read()
	tokens = word_tokenize(test.lower())
	print (tokens)

