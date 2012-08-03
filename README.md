Dynamic DNS Updater
===================

Keep domain names in sync with your dynamic IP address.

Description
-----------

A tool for updating a Dynamic DNS service if your IP has changed. Designed to be simple enough for the layperson to use, yet modular enough for easy implementation of rich features and support for disparate service providers.

#### Features

* Logging of events, as defined by the user.
* Logging of errors, as defined by the user.
* Updates any Dynamic DNS service which relies on simply visiting a URL.
* Usable under any operating system with Python installed.

Installation
------------

Set the folder to run recurrently with a job scheduling program such as Task Scheduler, Automator, or cron.

*Example of cron set to run this tool every 15 minutes:*

	*/15 * * * * python /home/user/Desktop/dynamic-dns-updater

Configuration
-----

Edit `config.cfg` with the following:

#### Your update URL

	update_url = http://freedns.afraid.org/dynamic/update.php?yourUniqueUpdateUrl

#### File locations

You may set the location of your log file to anywhere you wish. If it already exists, it will be appended to. If the file does not exist, it will automatically be created at the location you specify:

	log_file = /home/user/Desktop/dnsupdater.log
	
The ip cache file simply stores your current IP address between runs. It will automatically be created at the location you specify as well:
	
	ip_cache_file = /home/user/Desktop/ipcache
	
#### Logging

You can also choose what events you want written to the log file by marking them as true or false. `log_errors` will write any errors that occurred, `log_changes` will write any time your IP has changed, and `log_no_changes` will write any time the program is run at all.

	[logging]
	log_errors = true
	log_changes = true
	log_no_changes = false


Contributing
------------

Please contact me with websites that return your public IP address, similar to those in `sitelist.txt`, so we can have a greater array of choices to use for this function. Also, let me know of any Dynamic DNS providers you would like to see supported and any features you would like to see added.