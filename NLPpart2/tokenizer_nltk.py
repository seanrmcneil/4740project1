from nltk import word_tokenize

#takes the File of "raw text"
#makes everything lowercase
#
#need to ignore ' if in the case of don't, can't, won't .replace('\'','') makes it dont, cant, wont
def tokenize1(test):
	return (re.findall(r"[\w+]+|[.,\{\}()\[\]!?;:\\/\"]",
					  test.replace('\'', '').lower()))




