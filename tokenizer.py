import re


#takes the File of "raw text"
#makes everything lowercase
#removes \n
#need to ignore ' if in the case of don't, can't, won't .replace('\'','') makes it dont, cant, wont
def tokenize1(Filename):
	print(re.findall(r"[\w+]+|[.,\{\}()\[\]!?;:\\\/\"]",
					  open(Filename).read().replace('\\n', '').replace('\'', '').lower()))


tokenize1('test_tokenizer.txt')