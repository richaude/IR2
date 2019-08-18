from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter, get_page_args
from elasticsearch import Elasticsearch
#import re

app = Flask(__name__)
es = Elasticsearch()

def getResults(results, offset=0, per_page=10):
	return results[offset: offset + per_page]

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
		search=False
		#page = request.args.get(get_page_parameter(), type=int, default=1)
		#pagination = Pagination(page=page, total=users.count(), search=search, record_name='users')
		page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
		pagination_results = getResults(offset=offset, per_page=per_page, results=resp["hits"]["hits"])
		pagination = Pagination(page=page, per_page=per_page, total=resp["hits"]["total"]["value"], search=search, css_framework='bootstrap4')
		#print(pagination_results)
		return render_template("index.html", 
								q=q, 
								response=resp,
								page=page,
								per_page=per_page,
								results = pagination_results, 
								pagination=pagination
								)
	return render_template("index.html", pagination=None)

"""
def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]


@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
"""

if __name__ == "__main__":
	app.run(debug=True,port=8000)

# jinja ist zum Einbinden von Python in Html, django ist für das Management von Projekten
# stemming
