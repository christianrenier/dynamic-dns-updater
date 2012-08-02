import ConfigParser
import os
import sys
import utils

# Load configuration options from config file
parser = ConfigParser.SafeConfigParser()
parser.read(os.path.dirname(__file__) + '/config.cfg')

# Create a Logger object to log chosen events
log_file_location = parser.get('general', 'log_file')
logger = utils.logger.Logger(log_file_location)

# Retrieve IP address stored from previous run
ip_cache_location = parser.get('general', 'ip_cache_file')
try:
	cacher = utils.cacher.Cacher(ip_cache_location)
except:
	logger.log_error('Problem reading from IP cache file.')
	sys.exit()
old_ip = cacher.get_ip()

# Retrieve current public facing IP address
site_list_location = os.path.dirname(__file__) + '/sitelist.txt'
checker = utils.checker.Checker(site_list_location)
try:
	current_ip = checker.get_ip()
except:
	logger.log_error('Problem checking your current IP address.')
	sys.exit()

# Exit this script if IP address has not changed
if old_ip == current_ip:
	# Log that the address was not updated if enabled in config
	if parser.getboolean('logging', 'log_no_changes'):
		logger.log_no_change(old_ip)
	sys.exit()

# Update Dynamic DNS service with current public IP
update_url = parser.get('general', 'update_url')
updater = utils.updater.Updater(update_url)
try:
	updater.update_dns()
except:
	logger.log_error('Problem updating your Dynamic DNS.')
	sys.exit()

# Store current public IP in the cache file
try:
	cacher.store_ip(current_ip)
except:
	logger.log_error('Problem writing to IP cache file.')
	sys.exit()
	
# Log that the address was updated if enabled in config
if parser.getboolean('logging', 'log_changes'):
	logger.log_change(old_ip, current_ip)
