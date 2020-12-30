# This module is used to save the information of the Extract module in a .csv file
import pandas as pd

def Load(data, path):
	'''
		If the file exists, it takes the information and combines it with the new information
		If the file does not exist, I create it and save the information
	'''
	columns = ['number_of_question',
				'user',
				'question',
				'tags',
				'votes',
				'answers',
				'views',
				'link']	

	if file_exists(path):
		# load the csv file and select the columns saved in the variable "columns"
		load_df = pd.read_csv('{}/Stackoverflow_data.csv'.format(path))
		load_df = load_df.loc[:, columns]
		
		# create the dataframe that contains the new information
		data_dictionary = create_data_dictionary(data)
		create_df = pd.DataFrame(data_dictionary, columns=columns)

		# I concatenate the two dataframes and save this new df to a csv
		new_df = pd.concat([load_df, create_df], axis=0)
		new_df.to_csv('{}/Stackoverflow_data.csv'.format(path))

	else:
		data_dictionary = create_data_dictionary(data)
		df = pd.DataFrame(data_dictionary, columns=columns)

		#i create the .csv file
		df.to_csv('{}/Stackoverflow_data.csv'.format(path))

# check if the file exists
def file_exists(path):
	try:
		df = pd.read_csv('{}/Stackoverflow_data.csv'.format(path))
		exists = True
	except FileNotFoundError:
		exists = False

	return exists

# function that creates data dictionary and create the csv file
def create_data_dictionary(data):
	# through list comprehension I get the data from the dictionaries
	data_dictionary = {'number_of_question': [item['number_of_question'] for item in data],
						'user': [item['user'] for item in data],
						'question': [item['question'] for item in data],
						'tags': [item['tags'] for item in data],
						'votes': [item['stats']['votes'] for item in data],
						'answers': [item['stats']['answers'] for item in data],
						'views': [item['stats']['views'] for item in data],
						'link': [item['link'] for item in data]}

	return data_dictionary