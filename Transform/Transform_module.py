#"Transform" module, is responsible for transforming the data received from the Extract module
from bs4 import BeautifulSoup 
import json, re

#Principal function
def Transform(html):
	soup_html_dirty = BeautifulSoup(html, 'html.parser')

	html_user = get_html_with_attrs(soup_html_dirty, 'div', 'class', 'user-details')
	user = get_text_without_attrs(html_user, 'a')
	
	html_question_sumary = get_html_with_attrs(soup_html_dirty, 'div', 'class', 'question-summary')
	questions = get_text_without_attrs(html_question_sumary, 'h3')

	tags = get_tags_list(html_question_sumary, 'div', 'class', 'tags')

	html_stats = get_html_with_attrs(soup_html_dirty,'div', 'class', 'statscontainer')

	'''
		I create and save the dictionary where the stats of the questions are contained.
		The dictionary is separated by 3 keys, "votes", "answer" and "views",
		and since the data is dirty, use a regular expression to get only the numbers.
	'''
	stats_dictionary = make_stats_dictionary(html_stats, 
			list_votes := [re.findall(r'\d+', i)[0] for i in find_with_attrs(html_stats,'div', 'class', 'vote')], 
			list_answers := [re.findall(r'\d+', i)[0] for i in find_with_attrs(html_stats,'div', 'class', 'status')], 
			list_views := [re.findall(r'\d+', i)[0] for i in find_with_attrs(html_stats,'div', 'class', 'views')]
		)

	#I return the data in json format
	return json.dumps(dictionary_maker(user, questions, tags, stats_dictionary), ensure_ascii=False)

#get the html that contains the tags that indicate
def get_html_with_attrs(soup_html_dirty, element, attrs_1, attrs_2):
	find_element = soup_html_dirty.findAll(element, attrs={attrs_1: attrs_2})
	return [iterated_element for iterated_element in find_element]

#get the text plane of the html
def get_text_without_attrs(soup_html_dirty, element):
	return [iterated_element.find(element).text for iterated_element in soup_html_dirty]

'''
	This function is responsible for obtaining the labels in text format,
	and to separate each tag and save them in a list
	
	Get each html tag in "java mysql jsp" format,
	later, through a comprehension list, I split these tags and return a list, 
	for example  ["java", "mysql", "jsp"]
'''
def get_tags_list(html_question_sumary, element, attrs_1, attrs_2):
	tags_list = []
	for tags in html_question_sumary:
		tags_text = tags.find(element, attrs={attrs_1: attrs_2}).text.replace("\n", "")
		tags_list.append(tags_text)

	return [i.split() for i in tags_list]

def find_with_attrs(html_stats, element, attrs_1, attrs_2):
	return [iterated_element.find(element, attrs={attrs_1: attrs_2}).text for iterated_element in html_stats]

'''
	"make_stats_dictionary" its operation is that it goes through the 3 arrays of view numbers, votes, etc, 
	And it is creating dictionaries with that information, 
	and adding them in a list containing all these dictionaries. 
	So when I return the data of each answer the stats are in dictionary form
'''
def make_stats_dictionary(html_stats, vote, answer, views):
	list_stats = []
	cont = 0
	for i in vote:
		stats_dictionary = {
			"votes": i,
			"answers": answer[cont],
			"views": views[cont],
		}
		list_stats.append(stats_dictionary)
		cont += 1

	return list_stats

#generate the dictionary for the Load module
def dictionary_maker(user, questions, tags, stats):
	_dicc = []
	number_of_question = 1

	#I believe the dictionary
	for i in user:
		#stores the information of each question at the time they are saved
		temporary_dictionary = {
							'number_of_question': number_of_question,
							'user': i,
							'question': questions[number_of_question - 1],
							'tags': tags[number_of_question - 1],
							'stats': stats[number_of_question - 1]
						}

		_dicc.append(temporary_dictionary)
		number_of_question += 1

	return _dicc
