import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def chopping(filename, indexname):
	with open(filename, 'r') as file_handle:
		parsed_json = json.loads(file_handle.read())
		for document in parsed_json["statements"]:
			#print(searchParagraphs(document["rede"]))
			#print(screwItLikeATweet(document["rede"]))
			#print("\n\n")
			yield {
                "_index": indexname,
                "rede_id":document["dokument_id"],
                "name":document["name"],
                "datum":document["datum"],
                "sitzungsnummer":document["sitzungsnummer"],
                "rede":deleteHyphens(document["rede"]),
                "paragraph1":searchParagraphs(document["rede"])[0],
                "otherParagraphs":searchParagraphs(document["rede"])[1],
                "preview":screwItLikeATweet(document["rede"])[0],
                "rest":screwItLikeATweet(document["rede"])[1],
                "_type": "_doc",
            }    

def searchParagraphs(text):
	paragraphs = text.split("\n\n")
	#print(paragraphs[0])
	if paragraphs is not None and len(paragraphs) >= 2:
		return [paragraphs[0],"\n\n".join(paragraphs[1:])] # es ist im Prinzip wie head und tail
	return [text, ""]
	
def screwItLikeATweet(text):
	if text is not None:
		if len(text) >= 280:
			return [text[:280], text[280:]]
		else: return [text, text]
		
def replaceHyphens(text):
	return text.replace("-","_")

def replaceUnderscores(text):
	return text.replace("_","-")
	
def deleteHyphens(text):
	return text.replace("-","")
	
def zahlen(text):
	for word in text.split():
		pass
	
#print(searchParagraphs("Halllo ihr \n\n wie geht es euch \n seid ihr gut drauf?? \n\n ich auch!"))
es = Elasticsearch()
bulk(es, chopping("protokolle5.json", "new_index4"))
