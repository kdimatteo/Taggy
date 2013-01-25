Taggy
=====

Taggy is an experiment in topic discovery which leverages a combination of Twitter and [OpenCalais][http://www.opencalais.com/] take a single term (or hash tag) and find related topics.


Demo: http://fierce-forest-5845.herokuapp.com/

Contains 2 Python Modules
* process_twitter_topic : Hit twitter for a key word and return related topics  
* process_urls : Parse through a bag of URLs and generate a bag of tags

Dependencies
------------

* OpenCalais -  The Python Lib
* An [API key from OpenCalais][http://www.opencalais.com/APIkey].

Usage
-----

	import taggy.process_twitter_topic as twitter_topic
	twitter_topic.getTweets("dubplate")

	import taggy.process_urls as url_topic
	url_topic.topics_from_url("http://oneinthejungle.com")


Todo
----
1. Split these into 2 projects, url_topic is really designed to handle a list of URLs, not a single URL
1. Implement more than just Calais.topics
1. Standardize output



  
