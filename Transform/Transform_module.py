#"Transform" module, is responsible for transforming the data received from the Extract module
from bs4 import BeautifulSoup

#Principal function
def Transform(html):
	soup_html_dirty = BeautifulSoup(html, 'html.parser')
	html_question_sumary = get_html_sumary_question(soup_html_dirty)
	questions = get_question(html_question_sumary)

	return questions

#get the html containing a summary for each question
def get_html_sumary_question(soup_html_dirty):
	find_sumary = soup_html_dirty.findAll('div', attrs={'class': 'question-summary'})
	return [sumary_html for sumary_html in find_sumary]

#get the text plane of the html questions
def get_question(html_question_sumary):
	return [question.find('h3').text for question in html_question_sumary]