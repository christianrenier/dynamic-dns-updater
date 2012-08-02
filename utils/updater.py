import urllib

class Updater:

	"""Visits the update URL for a Dynamic DNS service."""

	def __init__(self, update_url):
		self.update_url = update_url

	def update_dns(self):

		"""Connects to the update URL, then disconnects."""
		request = urllib.urlopen(self.update_url)
		request.close()
		