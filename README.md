# IR2 - AfD statement search
## Second attempt to develop a fully functioning search engine
### Data
Our data consists of scraped protocols of 109 sessions of the German Bundestag, beginning with session 1 on 24th of October 2017 and ending with session 109 on 24th of July, 2019. For each session, only speeches of members of the AfD are stored, together with interposed questions of other Bundestag members and comments of the Bundestags(vize)präsident.
Each speech has one entry in our json file. The file is structured like this:
~~~~
{
	"statements":
		{"dokument_id":"1 to 1459",
		 "name":"Max Mustermann",
		 "datum":"dd.mm.yyyy",
                 "sitzungsnummer":"1 to 109",
		 "rede":"full text speech",
		},
		{ ... next entry following the same scheme ...
		}
}
~~~~

The json file is assembled with the function `mkJson3()` in `crawl.py`. But since the assembled file is already in this repository, I commented that out.


### Indexing
The function `documents()` prepares the file to be indexed into elasticsearch. After executing this function, you need to go to kibana in your web browser (with elasticsearch running). Go to: `Connect to your Elasticsearch index`, then type in "new\_index2" in the search bar. The "new\_index" should be recommended. Click on it and follow the subsequent steps until you see all the fields with their assigned value types. To actually perform search requests on it, go to the dev tools console and write a query like:
~~~~
GET /new_index3/_doc/_search
{
  "query": {
    "match_phrase": {
      "rede": "Clara Zetkin"
    }
  }
}
~~~~

### Evaluation
As a useful tool for evaluating our search project, we used [Quepid](https://quepid.com/ "Quepid").
In order to get Quepid connecting to our Elasticsearch project, the `elasticsearch.yml` config file needs to be configurated. This file should be in the `config` folder. This folder is in the same directory as the `bin` folder is.
Leave all the commented stuff in `elasticsearch.yml` as it is and add to the end this uncommented stuff:
~~~~
http.cors:
  enabled: true
  allow-origin: /http://app.quepid.com/
~~~~
After you saved this change to the file, restart Elasticsearch if you had it running.
When setting up Quepid, after signing up to their site, you will be guided through a menu, where at one point you have to choose between Solr and Elasticsearch. Choose Elasticsearch, then provide the following url: `http://localhost:9200/new_index2/_doc/_search`. If you left everything else at the default setting, this should work. Elasticsearch and Kibana have to be active at this moment. Then go through all the next steps, and hopefully you are provided with good results for the relevance scoring!
