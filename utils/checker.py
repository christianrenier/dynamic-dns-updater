import random
import urllib

class Checker:

	def __init__(self, list_location):
		self.errors = []
		self.list_location = list_location
		self.list = []
		self.init_list()

	def init_list(self):

		# Adds each line in the file to a list
		# with whitespace removed
		temp_list = open(self.list_location).readlines()
		for entry in temp_list:
			self.list.append(entry.strip())

	def get_ip(self):

		# Opens a connection to a random site
		# in the list
		random_site = random.choice(self.list)
		response = urllib.urlopen(random_site)

		# Sets a cleaned up version of the data
		# retrieved as the IP value
		temp_data = response.read()
		ip = self.clean_response(temp_data)

		return ip

	def clean_response(self, data_to_clean):

		# Removes whitespace from the data, if any
		# exists
		cleaner_data = data_to_clean.strip()

		# Removes the Pre html element from the data,
		# if any exists
		cleaner_data = cleaner_data.replace('<pre>', '')
		cleaner_data = cleaner_data.replace('</pre>', '')

		return cleaner_data

