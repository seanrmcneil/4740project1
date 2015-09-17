import re
import nltk

#takes the File of "raw text"
#makes everything lowercase
#
#need to ignore ' if in the case of don't, can't, won't .replace('\'','') makes it dont, cant, wont
def tokenize1(Filename):
	return (re.findall(r"[\w+]+|[.,\{\}()\[\]!?;:\\/\"]",
					  open(Filename).read().replace('\'', '').lower()))


