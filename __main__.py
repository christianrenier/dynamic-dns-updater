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
cacher = utils.cacher.Cacher(ip_cache_location)
old_ip = cacher.get_ip()

# Retrieve current public facing IP address
site_list_location = os.path.dirname(__file__) + '/sitelist.txt'
checker = utils.checker.Checker(site_list_location)
current_ip = checker.get_ip()

# Exit this script if IP address has not changed
if old_ip == current_ip:
	sys.exit()

# Update Dynamic DNS service with current public IP
update_url = parser.get('general', 'update_url')
updater = utils.updater.Updater(update_url)
updater.update_dns()

# Store current public IP in the cache file
cacher.store_ip(current_ip)
