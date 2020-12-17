#"Transform" module, is responsible for transforming the data received from the Extract module
from bs4 import BeautifulSoup 
import json

#Principal function
def Transform(html):
	soup_html_dirty = BeautifulSoup(html, 'html.parser')

	html_user = get_html_with_attrs(soup_html_dirty, 'div', 'class', 'user-details')
	user = get_text_without_attrs(html_user, 'a')
	
	html_question_sumary = get_html_with_attrs(soup_html_dirty, 'div', 'class', 'question-summary')
	questions = get_text_without_attrs(html_question_sumary, 'h3')


	#I return the data in json format
	return json.dumps(dictionary_maker(user, questions), ensure_ascii=False)

#get the html that contains the tags that indicate
def get_html_with_attrs(soup_html_dirty, element, attrs_1, attrs_2):
	find_element = soup_html_dirty.findAll(element, attrs={attrs_1: attrs_2})
	return [iterated_element for iterated_element in find_element]

#get the text plane of the html
def get_text_without_attrs(soup_html_dirty, element):
	return [iterated_element.find(element).text for iterated_element in soup_html_dirty]

#generate the dictionary for the Load module
def dictionary_maker(user, questions):
	_dicc = []
	number_of_question = 1

	#I believe the dictionary
	for i in user:
		#stores the information of each question at the time they are saved
		temporary_dictionary = {
							'number_of_question': number_of_question,
							'user': i,
							'question': questions[number_of_question - 1]
						}

		_dicc.append(temporary_dictionary)
		number_of_question += 1

	return _dicc
