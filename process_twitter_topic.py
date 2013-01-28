#!/usr/bin/python

import fileinput
import os
import simplejson
import urllib
import urllib2
import sys
import re

from calais import Calais

API_KEY =  os.environ['API_KEY']
calais = Calais(API_KEY, submitter="python-calais demo")


def getTweets(term, return_json=True, debug=False):
    '''
    Search Twitter for the provided hast_tag to generate a bag of words.
    Return entities and topics from OpenCalais
    '''
    
    if debug is True:
        print "Sanitized Search term: %s " % urllib.quote(term)
    
    u = 'http://search.twitter.com/search.json?lang=en&rpp=100&result_type=recent&q=%s' % urllib.quote_plus(term)
    result = urllib2.urlopen(u)
    o = simplejson.loads(result.read())
    content = ""
    L = []
    for tweet in o['results']:
        L.append(tweet['text'])

    entities = [] 
    topics = []
    relations = []

    pattern = '((mailto\:|(news|(ht|f)tp(s?))\://){1}\S+)'

    content = " ".join(L)
    content = content.encode("utf-8")

    try:
        result = calais.analyze(content)
        
        if debug is True:
            print "--------\nTopics:\n--------------------"
            result.print_topics()
            print "--------\nEntities:\n--------------------"
            result.print_entities()
            print "--------\nRelations:\n--------------------"
            result.print_relations()

    except:
        print "something is broken"
        pass

    try:
        for item in result.entities:
            if not re.match(pattern, item['name']) and ("RT" not in item["name"]):
                entities.append(item['name'])
    except:
        pass
        #print "no entities found"
                
    try:
        for item in result.topics:
            topics.append(item['categoryName'])
    except:
        pass
        #print "no topics found"

    '''

    # @todo need additional logic as key names are variable:
    # e.g.: 'careertype', 'instances', 'company', 'person', 'position', '__reference'
    try:
        for item in result.relations:
            for k, v in item:
                relations.append(item['relation'])
    except:
        pass
    '''

    o = {"calais_results":{"entities":entities, "topics":topics, "relations":relations}}

    if(return_json is True):
        for d in result.relations:
            print d.keys()
        return simplejson.dumps(o);
    else :
        return o


if __name__ == "__main__":
    var = sys.argv[1]
    o = getTweets(var, True, False)
    print o
    #print ", ".join(o)