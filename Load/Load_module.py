# This module is used to save the information of the Extract module in a .csv file
import pandas as pd

def Load(data, path):
	'''
		If the file exists, it takes the information and combines it with the new information
		If the file does not exist, I create it and save the information
	'''
	if file_exists(path):
		print('existe')
	else:
		columns = ['number_of_question',
					'user',
					'question',
					'tags',
					'votes',
					'answers',
					'views',
					'link']

		# through list comprehension I get the data from the dictionaries
		data = {'number_of_question': [item['number_of_question'] for item in data],
				'user': [item['user'] for item in data],
				'question': [item['question'] for item in data],
				'tags': [item['tags'] for item in data],
				'votes': [item['stats']['votes'] for item in data],
				'answers': [item['stats']['answers'] for item in data],
				'views': [item['stats']['views'] for item in data],
				'link': [item['link'] for item in data]}

		#i create the .csv file
		df = pd.DataFrame(data, columns=columns)
		df.to_csv('{}/Stackoverflow_data.csv'.format(path))

# check if the file exists
def file_exists(path):
	try:
		df = pd.read_csv('{}/Stackoverflow_data.csv'.format(path))
		exists = True
	except:
		exists = False

	return exists