#"Extract" module, to obtain data from the Stackoverflow questions
import requests

#this function contains all the functions of the Extract module
def Extract(url):
	return  (html := get_html_from_the_page(url))

#get the request text
def get_html_from_the_page(url):
	return (html_dirty := requests.get(url)).text[:-1]