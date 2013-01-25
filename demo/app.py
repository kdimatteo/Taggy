
import flask
import os
#import logging
import sys
import taggy.process_twitter_topic as twitter_topic
import taggy.process_urls as url_topic
#import taggy.process_twitter_topic.py


app = flask.Flask(__name__)
#logging.basicConfig(stream=sys.stderr)

@app.route("/")
def index():
	return flask.send_from_directory("./", "index.html")

@app.route("/<path:filename>")
def passThrough(filename):
	return flask.send_from_directory("./", filename);





@app.route("/term/", methods=["GET"])
def getTerm():
	#term = flask.request.json["term"]
	term = flask.request.args["term"]
	#return ",".join(flask.request.args)
	results = {"response": twitter_topic.getTweets(term)}
	return flask.jsonify(results)
	#return ",".join(flask.request)


@app.route("/url/", methods=['GET'])
def getURL():
	term = flask.request.args["term"]
	results = {"response": url_topic.topics_from_url(term)}
	return flask.jsonify(results)

if __name__ == "__main__":
        # Bind to PORT if defined, otherwise default to 5000.
        port = int(os.environ.get('PORT', 5000))
        #app.run(host='127.0.0.1', port=port)
	app.run(host='0.0.0.0', port=port, debug=True)
