#!/usr/bin/env python
# coding: utf8

# Program scrapes article text from www.computerbase.de and puts the data into a json file. Number of pages have to entered manually

import requests
import json
from bs4 import BeautifulSoup


# Function calls url and returns the parsed html. Format changes for more pages: url + str(n) + "/"

def get_page_data(url, page):
	if int(page) == 1:
		html = requests.get(url)
		soup = BeautifulSoup(html.content, "html.parser")
		return soup
	elif int(page) > 1:
		html = requests.get(url + str(page) + "/")
		soup = BeautifulSoup(html.content, "html.parser")
		return soup
		
# Function takes parsed html and returns tags (h1, h2, h3, p) and their content into a tupled list.

def get_article_page(soup): 
	tags = [(tag.name, tag.text) for tag in soup.article.find_all(["h1", "h2", "h3", "p"])]
	return tags
	
# Main function to call all pages, summarize tuples, convert it into a json structure and save it as a json file.

def get_cbarticle(url, pages):
	n = 1
	article = []
	while n <= pages:
		article.extend(get_article_page(get_page_data(url,n)))
		n += 1

	data = {n:{tag:text} for (n,(tag,text)) in enumerate(article)}

	with open('article.json', 'w') as file:
		json.dump(data, file, ensure_ascii=False)
		

url = str(input("Bitte geben Sie die URL ein: \n"))

# testing url = "https://www.computerbase.de/2019-01/asus-rog-phone-test-review/"

pages = int(input("Wieviele Seiten hat der Artikel? \n"))

get_cbarticle(url, pages)
		



	
	