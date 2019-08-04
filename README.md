# IR2 - AfD statement search
## Second attempt to develop a fully functioning search engine
### Data
Our data consists of scraped protocols of 109 sessions of the German Bundestag, beginning with session 1 on 24th of October 2017 and ending with session 109 on 24th of July, 2019. For each session, only speeches of members of the AfD are stored, together with interposed questions of other Bundestag members and comments of the Bundestags(vize)präsident.
Each speech has one entry in our `protokolle3.json` file. The file is structured like this:
~~~~
{
	"statements":
		{"name":"Max Mustermann",
		 "datum":"dd.mm.yyyy",
                 "sitzungsnummer":"1 to 109",
		 "rede":"full text speech",
		},
		{ ... next entry following the same scheme ...
		}
}
~~~~

The json file is assembled with the function `mkJson2()` in `crawl.py`. But since the assembled file is already in this repository, I commented that out.


### Indexing
The function `documents()` prepares the file to be indexed into elasticsearch. After executing this function, you need to go to kibana in your web browser (with elasticsearch running). Go to: `Connect to your Elasticsearch index`, then type in "new\_index" in the search bar. The "new\_index" should be recommended. Click on it and follow the subsequent steps until you see all the fields with their assigned value types. To actually perform search requests on it, go to the dev tools console and write a query like:
~~~~
GET /new_index/_doc/_search
{
  "query": {
    "match_phrase": {
      "rede": "Clara Zetkin"
    }
  }
}
~~~~
