#!/usr/bin/python

import fileinput
import simplejson
import urllib
import urllib2
import sys
import re

from calais import Calais

API_KEY =  os.environ['API_KEY']
calais = Calais(API_KEY, submitter="python-calais demo")


def getTweets(hash_tag):
    '''
    Search Twitter for the provided hast_tag to generate a bag of words.
    Return entities and topics from OpenCalais
    '''
    #print urllib.quote(hash_tag)
    u = 'http://search.twitter.com/search.json?lang=en&rpp=100&result_type=recent&q=%s' % urllib.quote_plus(hash_tag)
    result = urllib2.urlopen(u)
    o = simplejson.loads(result.read())
    content = ""
    L = []
    for tweet in o['results']:
        L.append(tweet['text'])
    
    OUTPUT = []
    pattern = '((mailto\:|(news|(ht|f)tp(s?))\://){1}\S+)'

    content = " ".join(L)
    content = content.encode("utf-8")
    
    try:
        result = calais.analyze(content)
        
        '''
        print "--------"
        result.print_topics()
        print "--------"
        result.print_entities()
        print "--------"
        result.print_relations()
        '''
        
    except:
        print "something is broken"
        pass

    for item in result.entities:
            if not re.match(pattern, item['name']):
                #print "%s" % item['name']
                OUTPUT.append(item['name'])
                
    for item in result.topics:
        if not re.match(pattern, item['categoryName']):
            #print "%s" % item['categoryName']
            OUTPUT.append(item['categoryName'])
            
    print ", ".join(OUTPUT)

var = sys.argv[1]
getTweets(var)
