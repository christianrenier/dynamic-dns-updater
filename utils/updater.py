import urllib

class Updater:

	"""Visits the update URL for a Dynamic DNS service."""

	def __init__(self, update_urls):
		
		# Make a list out of the string split by comma
		self.update_urls = update_urls.split(',')

	def update_dns(self):

		"""Connects to each update URL, then disconnects."""
		for url in self.update_urls:

			# Adds protocol if address does not contain it
			if 'http://' not in url: url = 'http://' + url

			request = urllib.urlopen(url)
			request.close()
		