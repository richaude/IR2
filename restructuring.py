import json

def chopping(filename):
	with open(filename, 'r') as file_handle:
		parsed_json = json.loads(file_handle.read())
		for document in parsed_json["statements"]:
			#print(searchParagraphs(document["rede"]))
			print(screwItLikeATweet(document["rede"]))
			print("\n\n")

def searchParagraphs(text):
	paragraphs = text.split("\n\n")
	#print(paragraphs[0])
	if paragraphs is not None and len(paragraphs) >= 2:
		return paragraphs[0]
	return text
	
def screwItLikeATweet(text):
	if text is not None:
		if len(text) >= 280:
			return text[:280]
		else: return text
	
#print(searchParagraphs("Halllo ihr \n\n wie geht es euch \n seid ihr gut drauf?? \n\n ich auch!"))
chopping("protokolle5.json")
