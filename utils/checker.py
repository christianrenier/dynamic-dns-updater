import random
import urllib

class Checker:

	def __init__(self, list_location):
		self.errors = []
		self.current_ip = None
		self.list_location = list_location
		self.list = []
		self.init_list()

	def init_list(self):
		temp_list = open(self.list_location).readlines()
		for entry in temp_list:
			self.list.append(entry.strip())

	def get_current_ip(self):
		random_site = random.choice(self.list)
		response = urllib.urlopen(random_site)
		temp_data = response.read()
		self.current_ip = self.clean_response(temp_data)
		return self.current_ip

	def clean_response(self, data_to_clean):
		data_to_clean = data_to_clean.strip()
		data_to_clean = data_to_clean.replace('<pre>', '')
		data_to_clean = data_to_clean.replace('</pre>', '')
		return data_to_clean

