import datetime

class Logger:

	def __init__(self, log_location):
		self.log_location = log_location

	def log_error(self, error_message):
		return

	def log_no_change(self, ip):
		now = datetime.datetime.now().ctime()
		message = "%s: %s remains unchanged.\n" % (now, ip)
		file = open(self.log_location, 'a')
		file.write(message)
		file.close()

	def log_change(self, previous_ip, new_ip):
		now = datetime.datetime.now().ctime()
		message = "%s: %s has been updated to %s.\n" % (now, previous_ip, new_ip)
		file = open(self.log_location, 'a')
		file.write(message)
		file.close()