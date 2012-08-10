import ConfigParser
import os
import sys
import utils



## Create global names and functions ##

# Load file locations and configuration options
site_list_location = os.path.dirname(__file__) + '/sitelist.txt'
parser = ConfigParser.RawConfigParser()
parser.read(os.path.dirname(__file__) + '/config.cfg')
general = dict(parser.items('general'))
gmail_account = dict(parser.items('gmail_account'))
write_error = parser.getboolean('logging', 'log_errors')
write_change = parser.getboolean('logging', 'log_changes')
write_unchanged = parser.getboolean('logging', 'log_unchanged')
receiver = parser.get('mailing', 'mail_receivers')
mail_error = parser.getboolean('mailing', 'send_errors')
mail_change = parser.getboolean('mailing', 'send_changes')

# Name of this tool
tool_name = 'Dynamic DNS Updater'
# Tracks if a logger was created
logger = False
# Tracks if a mailer was created
mailer = False

# Dictionary of error codes and their corresponding messages
error_messages = {
			'invalid_login' : 'Your Gmail username or password is incorrect.',
			'logger_missing' : 'Problem writing to log file.',
			'read_cache' : 'Problem reading from IP cache.',
			'read_sitelist' : 'Problem reading the sitelist.',
			'empty_url' : 'You have not provided an update URL.',
			'check_ip' : 'Problem checking your IP address.',
			'update_dns' : 'Problem updating your Dynamic DNS.'
			}

# Handles logging and mailing of errors, as enabled by the user
def error_processor(code):
	if write_error and logger: logger.log_error(error_messages[code])
	if mail_error and mailer:
		mailer.send_error(receiver, error_messages[code])
	print '%s: Error - %s' % (tool_name, error_messages[code])
	sys.exit()



## Create instances of utility classes ##

# Only create logger object if the user has chosen to log an event
if write_error or write_change or write_unchanged:
	try: logger = utils.logger.Logger(general['log_file'])
	except: logger = False
# Only create mailer object if user has chosen to mail an event
if mail_error or mail_change:
	try: mailer = utils.mailer.Mailer(
		gmail_account['gmail_user'],
		gmail_account['gmail_password'])
	except: error_processor('invalid_login')
# Notify user by mail that initializing a logger has failed, if they
# enabled any logging of events
if not logger and mailer:
	if write_error or write_change or write_unchanged:
		error_processor('logger_missing')

try: cacher = utils.cacher.Cacher(general['ip_cache_file'])
except: error_processor('read_cache')
try: checker = utils.checker.Checker(site_list_location)
except: error_processor('read_sitelist')
try: updater = utils.updater.Updater(general['update_urls'])
except: error_processor('empty_url')



## Main ##

old_ip = cacher.get_ip()

try: current_ip = checker.get_ip()
except: error_processor('check_ip')

# If IP has not changed, exit the program
if old_ip == current_ip:
	if write_unchanged:
		logger.log_no_change(old_ip)
		print '%s: %s remains unchanged.' % (tool_name, old_ip)
		sys.exit()

try: updater.update_dns()
except: error_processor('update_dns')

cacher.store_ip(current_ip)
print '%s: %s has been updated to %s' % (tool_name, old_ip, current_ip)
if write_change: logger.log_change(old_ip, current_ip)
if mail_change and mailer:
	mailer.send_change(receiver, old_ip, current_ip)
