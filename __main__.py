import ConfigParser
import os
import sys
import utils

# Load configuration options from config file
parser = ConfigParser.SafeConfigParser()
parser.read(os.path.dirname(__file__) + '/config.cfg')
write_errors = parser.getboolean('logging', 'log_errors')

# Create a Logger object to log chosen events
log_file_location = parser.get('general', 'log_file')
logger = utils.logger.Logger(log_file_location)

# Retrieve IP address stored from previous run
ip_cache_location = parser.get('general', 'ip_cache_file')
try:
	cacher = utils.cacher.Cacher(ip_cache_location)
except:
	if write_errors: logger.log_error('read_cache')
	sys.exit()
old_ip = cacher.get_ip()

# Retrieve current public facing IP address
site_list_location = os.path.dirname(__file__) + '/sitelist.txt'
checker = utils.checker.Checker(site_list_location)
try:
	current_ip = checker.get_ip()
except:
	if write_errors: logger.log_error('check_ip')
	sys.exit()

# Exit this script if IP address has not changed
if old_ip == current_ip:
	# Log that the address was not updated if enabled in config
	if parser.getboolean('logging', 'log_no_changes'):
		logger.log_no_change(old_ip)
	sys.exit()

# Update Dynamic DNS service with current public IP
update_urls = parser.get('general', 'update_urls')
updater = utils.updater.Updater(update_urls)
try:
	updater.update_dns()
except:
	if write_errors: logger.log_error('update_dns')
	sys.exit()

# Store current public IP in the cache file
try:
	cacher.store_ip(current_ip)
except:
	if write_errors: logger.log_error('write_cache')
	sys.exit()
	
# Log that the address was updated if enabled in config
if parser.getboolean('logging', 'log_changes'):
	logger.log_change(old_ip, current_ip)
