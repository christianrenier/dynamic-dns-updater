import datetime

class Logger:

	"""Writes events and time of occurrence to a log file."""

	def __init__(self, log_location):
		self.log_location = log_location
		self.test_log_file()

	def test_log_file(self):
		file = open(self.log_location, 'a')
		file.close()

	def get_datetime(self):
		return datetime.datetime.now().ctime()

	def append_message(self, log_message):
		file = open(self.log_location, 'a')
		file.write(log_message)
		file.close()

	def log_error(self, error_message):

		"""Adds the event of an error occurrence to the log file."""
		now = self.get_datetime()
		message = "%s: Error - %s\n" % (now, error_message)
		self.append_message(message)
		return

	def log_no_change(self, ip):

		"""Adds the event of no IP change to the log file."""
		now = self.get_datetime()
		message = "%s: %s remains unchanged.\n" % (now, ip)
		self.append_message(message)

	def log_change(self, previous_ip, new_ip):

		"""Adds the event of an IP update to the log file."""
		now = self.get_datetime()
		message = "%s: %s has been updated to %s.\n" % (now, previous_ip, new_ip)
		self.append_message(message)