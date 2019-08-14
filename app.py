from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route('/',methods=["GET","POST"])
def index():
	q = request.args.get("q")
	if q is not None:
		resp = es.search(index="new_index",body={"query": {"match_phrase": {"rede": q}}}, size=5)
		return render_template("index.html", q=q, response=resp)
	return render_template("index.html", response=es.search(size=0))


if __name__ == "__main__":
	app.run(debug=True,port=8000)

# jinja ist zum Einbinden von Python in Html, django ist für das Management von Projekten
