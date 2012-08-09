import smtplib
from email.mime.text import MIMEText

class Mailer:

	"""Sends alerts via e-mail."""

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.from_address = username + '@gmail.com'

	def send_change(self, receiver, old_ip, new_ip):

		"""Mails the event of an IP address change to the receiver."""
		
		# Construct RFC-2822 message
		message = MIMEText("%s has been updated to %s." % (old_ip, new_ip))
		message['Subject'] = 'Dynamic-DNS Updater: Your IP address has changed.'
		message['From'] = self.from_address
		message['To'] = receiver
		
		# Connect to Gmail and send e-mail
		server = smtplib.SMTP('smtp.gmail.com:587')  
		server.starttls()  
		server.login(self.username, self.password)  
		server.sendmail(self.from_address, receiver, message.as_string())  
		server.quit()

	def send_error(self, receiver, error_message):

		"""Mails the event of an error to the receiver."""

		# Construct RFC-2822 message
		message = MIMEText(error_message)
		message['Subject'] = 'Dynamic-DNS Updater: An error has occurred.'
		message['From'] = self.from_address
		message['To'] = receiver

		# Connect to Gmail and send e-mail
		server = smtplib.SMTP('smtp.gmail.com:587')  
		server.starttls()  
		server.login(self.username, self.password)  
		server.sendmail(self.from_address, receiver, message.as_string())  
		server.quit() 