import datetime

class Logger:

	"""Writes events and time of occurrence to a log file."""

	def __init__(self, log_location):
		self.log_location = log_location
		self.error_messages = {
			'read_cache' : 'Problem reading from IP cache.',
			'check_ip' : 'Problem checking your IP address.',
			'update_dns' : 'Problem updating your Dynamic DNS.',
			'write_cache' : 'Problem writing to IP cache.'
		}

	def get_datetime(self):
		return datetime.datetime.now().ctime()

	def append_message(self, log_message):
		file = open(self.log_location, 'a')
		file.write(log_message)
		file.close()

	def log_error(self, code):

		"""Adds the event of an error occurrence to the log file."""
		now = self.get_datetime()
		message = "%s: Error - %s\n" % (now, self.error_messages[code])
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