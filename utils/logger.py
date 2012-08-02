import datetime

class Logger:

	def __init__(self, log_location):
		self.log_location = log_location

	def get_datetime(self):
		return datetime.datetime.now().ctime()

	def append_message(self, log_message):
		file = open(self.log_location, 'a')
		file.write(log_message)
		file.close()

	def log_error(self, error_message):
		return

	def log_no_change(self, ip):
		now = self.get_datetime()
		message = "%s: %s remains unchanged.\n" % (now, ip)
		self.append_message(message)

	def log_change(self, previous_ip, new_ip):
		now = self.get_datetime()
		message = "%s: %s has been updated to %s.\n" % (now, previous_ip, new_ip)
		self.append_message(message)