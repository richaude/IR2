import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def chopping(filename, indexname):
	with open(filename, 'r') as file_handle:
		parsed_json = json.loads(file_handle.read())
		for document in parsed_json["statements"]:
			yield {
                "_index": indexname,
                "rede_id":document["dokument_id"],
                "name":document["name"],
                "datum":document["datum"],
                "sitzungsnummer":document["sitzungsnummer"],
                "rede":deleteHyphens(document["rede"]),
                #"rede":document["rede"],
                "paragraph1":searchParagraphs(document["rede"])[0],
                "otherParagraphs":searchParagraphs(document["rede"])[1],
                "_type": "_doc",
            }    

def searchParagraphs(text):
	paragraphs = text.split("\n\n")
	#print(paragraphs[0])
	if paragraphs is not None and len(paragraphs) >= 2:
		return [paragraphs[0],"\n\n".join(paragraphs[1:])] # es ist im Prinzip wie head und tail
	return [text, ""]
		
def replaceHyphens(text):
	return text.replace("-","_")

def replaceUnderscores(text):
	return text.replace("_","-")
	
def deleteHyphens(text):
	return text.replace("-","")

	
def createIndex(es, indexname):
	es.indices.create(indexname, body = {
  "settings": {
   "similarity": {
      "my_similarity": {
        "type": "BM25",
        "k1": 10,
        "b": 0
      }
    },
    "analysis": {
      "filter": {
		#"trigrams": {
        #  "type": "ngram",
        #  "min_gram": 3,
        #  "max_gram": 3
        #  },
        "german_stop": {
          "type":       "stop",
          "stopwords":  ["_german_", "for", "or", "and", "the", "is"]
        },
        #"german_keywords": {
        #  "type":       "keyword_marker"
          #"keywords":   ["Beispiel"] 
       # },
        "german_stemmer": {
          "type":       "stemmer",
          "language":   "light_german"
        },
        "synonym" : {
			"type" : "synonym",
			"synonyms" : [
			"sexualität => intersexuell, transsexuell, heterosexuell, bisexuell, lgbt, homosexuell, sexuell, gender",
			"g20, g-20, g 20",
			"islam => moschee, imam, muslime, moslems, koran",
			"flüchtlinge, migranten",
			"russland, russische föderation",
			"usa, vereinigte staaten",
			"wahlbeeinflussung, wahlbetrug",
			"antifaschismus => antifaschistisch",
			"rechtsextrem, rechtsradikal, rechtsextremismus",
			"linksextrem, linksradikal, linksextremismus",
			"no deal brexit => harter brexit, ungeordneter brexit",
			"merkel, bundeskanzlerin"
			#"linksgrün => links-grün, links grün"
			]
		}
      },
      "analyzer": {
        "rebuilt_german": {
          "tokenizer":  "standard",
          "filter": [
            "lowercase",
            #"trigrams",
            "synonym",
            #"trigrams",
            "german_stop",
            #"german_keywords",
            "german_normalization",
            "german_stemmer"
            #"synonym"
          ]
        }
      }
    }
  },
  "mappings": {
	"properties": {
		"rede_id": {
			"type": "integer"
		},
		"name": {
			"type": "text",
			"similarity": "my_similarity",
			"analyzer": "rebuilt_german"
      },
      "datum": {
		"type": "text"
      },
      "sitzungsnummer": {
      	"type": "text"
      },
      "rede": {
			"type": "text",
			"similarity": "my_similarity",
			"analyzer": "rebuilt_german"
      },
      "paragraph1": {
			"type": "text",
			"similarity": "my_similarity",
			"analyzer": "rebuilt_german"
      },
      "otherParagraphs": {
			"type": "text",
			"similarity": "my_similarity",
			"analyzer": "rebuilt_german"
      }
	}
  }
	})

es = Elasticsearch()
createIndex(es, "new_index")
bulk(es, chopping("protokolle5.json", "new_index"))
#curl -XDELETE 'http://localhost:9200/*' löscht alle Indizes

