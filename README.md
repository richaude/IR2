# IR2 - AfD statement search
## Second attempt to develop a fully functioning search engine
### Data
Our data consists of scraped protocols of 109 sessions of the German Bundestag, beginning with session 1 on 24th of October 2017 and ending with session 109 on 24th of July, 2019. For each session, only speeches of members of the AfD are stored, together with interposed questions of other Bundestag members and comments of the Bundestags(vize)präsident.
Each speech has one entry in our `protokolle.json` file. One entry is structured like this:
~~~~
{"rede_id (beginning with 1, 1459 in total)": 
{"name":"some name with a title, if present", 
"datum":"dd.mm.yyyy", 
"sitzungsnummer":"number of session (1 to 109)", 
"rede":"full text speech"}}
~~~~

The json file is assembled with `crawl.py`.
