import ConfigParser
import os
import sys
import utils

parser = ConfigParser.SafeConfigParser()
parser.read(os.path.dirname(__file__) + '/config.cfg')

log_file_location = parser.get('general', 'log_file')
logger = utils.logger.Logger(log_file_location)

ip_cache_location = parser.get('general', 'ip_cache_file')
cacher = utils.cacher.Cacher(ip_cache_location)
old_ip = cacher.get_old_ip()

site_list_location = os.path.dirname(__file__) + '/sitelist.txt'
checker = utils.checker.Checker(site_list_location)
current_ip = checker.get_current_ip()

if old_ip == current_ip:
	sys.exit()

update_url = parser.get('general', 'update_url')
updater = utils.updater.Updater(update_url)
updater.update_dns()

cacher.store_new_ip(current_ip)
