#!/usr/bin/env python2.7

from bs4 import BeautifulSoup
import urllib
import requests
import sys

print >> sys.stderr, 'Remember: If you abuse, bing will ban you IP'
if len(sys.argv) == 2:
	dork = sys.argv[1]
	goOn = True
	res = []
	i = 0
	while goOn:
		r = requests.get("http://www.bing.com/search?q={}&first={}".format(dork, i*10))
		soup = BeautifulSoup(r.text, 'html.parser')
		nc = 0
		for link in soup.find_all('cite'):
			print link.get_text()
			nc+=1
		if nc < 10:
			goOn = False	
		i += 1
		
else:
	print "Usage: bingscan.py DORK"
	print "URL Extractor"
