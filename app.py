from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
#import re

app = Flask(__name__)
es = Elasticsearch()

@app.route('/',methods=["GET","POST"])
def index():
	q = request.args.get("q")
	if q is not None:
		#resp = es.search(index="new_index2",body={"query": {"match_phrase": {"rede": q}}}, size=5)
		resp = es.search(index="new_index4",body = {
			"query": {
				"multi_match": {
					"query": q, "fields" : [ "paragraph1^3", "otherParagraphs", "rede^2", "name^5" ]
				}
			}, "highlight": {
					"pre_tags": ["<mark>"], "post_tags": ["</mark>"],"fields": {
						"paragraph1": {
							"number_of_fragments": 2
						}, "otherParagraphs": {
								"number_of_fragments": 2
							}
					}
				}
		}, size=1435)
		# size ist nun die Anzahl aller Dokumente im Korpus
		return render_template("index.html", q=q, response=resp)
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True,port=8000)

# jinja ist zum Einbinden von Python in Html, django ist für das Management von Projekten
# stemming
