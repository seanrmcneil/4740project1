import re


#takes the File of "raw text"
#check to make sure /n issues work
def tokenize(Filename):
	return re.findall(r"[\w+]+|[.,\{\}()\[\]!?;:\\\"]",
					  open(Filename).read().replace('\\n', '').replace('\'', '')) #.replace to take care of /n issues