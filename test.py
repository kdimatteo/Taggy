#!/usr/bin/python
import os
import process_twitter_topic
import process_urls

#print os.environ
#print os.environ['API_KEY']

fail = False

def test_env_vars():

	if(os.environ['API_KEY'] is not None):
		print "\n\nTESTING ENV\nAPI KEY env var is defined"
	else :
		print "[ERROR] API KEY not defined"
		fail = True


def test_twitter(term):
	print "\n\nTESTING TWEETS: %s \n" % term
	print process_twitter_topic.getTweets(term)


def test_url(u):
	print "\n\nTESTING URL: %s \n" % u
	print process_urls.topics_from_url(u)




test_env_vars()
test_twitter("cash")
test_url("http://cnet.com")