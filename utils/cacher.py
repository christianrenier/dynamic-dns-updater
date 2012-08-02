import os

class Cacher:

	"""Reads and writes IP values to a cache file."""

	def __init__(self, cache_location):
		self.errors = []
		self.cache_location = cache_location
		self.ip = None
		self.init_ip()

	def init_ip(self):

		# If a cache file has already been created, set
		# the IP value to the value stored within it
		if os.path.exists(self.cache_location):
			file = open(self.cache_location, 'r')
			self.ip = file.read()
		# If a cache file has not been created, create
		# one and set IP value to an informative string
		else:
			file = open(self.cache_location, 'w')
			self.ip = 'initial state'
		file.close()

	def get_ip(self):

		# Returns the currently set IP value
		return self.ip

	def store_ip(self, ip):

		# Writes sent IP address to file
		file = open(self.cache_location, 'w')
		file.write(ip)
		file.close()

		# Sets the current IP value to the new, sent value
		self.ip = ip
