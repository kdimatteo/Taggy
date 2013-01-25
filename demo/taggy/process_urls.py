#!/usr/bin/python

import fileinput
import os
import re
import simplejson
import sys
import urllib
import urllib2

from calais import Calais

API_KEY = os.environ['API_KEY']
calais = Calais(API_KEY, submitter="python-calais demo")


def topics_from_url(u):
    result = calais.analyze_url(u)
    return result.topics

def getTopics(filename):

    '''
    Simple script to process a pile of URLs (one per line) in an external file and dump topics, entities, or relations from OpenCalais.
    Useful for generating tags about a website, or a list of sites as illustrated http://twodotlol.blogspot.com/2012/01/whos-practicing-responsive-design.html
    '''
        
    for line in fileinput.input(filename):

    	try:
        	result = calais.analyze_url(line)
        
	        #print "--------"
        	result.print_topics()
        	#print "--------"
        	#result.print_entities()
        	#print "--------"
       	 	#result.print_relations()
        
	except:
        	print "something is broken"
	       	pass
    
    '''
    for item in result.entities:
            if not re.match(pattern, item['name']):
                #print "%s" % item['name']
                OUTPUT.append(item['name'])
                    
    for item in result.topics:
        if not re.match(pattern, item['categoryName']):
            #print "%s" % item['categoryName']
            OUTPUT.append(item['categoryName'])
            
    print ", ".join(OUTPUT)
    '''

if __name__ == "__main__":
    urlPile = sys.argv[1]
    getTopics(urlPile)
