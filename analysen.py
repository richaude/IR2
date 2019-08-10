# häufigste Wörter finden
import operator, json

def listeWoerter(text, dictionary):
	wordlist = text.split()
	for word in wordlist:
		word = word.lower()
		#print(word)
		if word != None and (word[0] not in "!?,.„“:;"):
			while word[-1] in ".“„:;,!?":
				word = word[:-1]
			if word[0] == "„":
				word = word[1:]
			if word not in dictionary:
				dictionary[word] = 1
			else:
				dictionary[word] = dictionary[word]+1

def readFile(filename, dictionary):
	with open(filename, 'r') as file_handle:
		parsed_json = json.loads(file_handle.read())
		for document in parsed_json["statements"]:
			listeWoerter(document["rede"], dictionary)
	return dictionary
	
myDict = {}
fullDict = readFile("protokolle5.json", myDict)
sortedDictionary = sorted(fullDict.items(), key=operator.itemgetter(1), reverse = True)
i = 0
for k,v in sortedDictionary:
	print(k)
	i += 1
	if i > 99:
		break
