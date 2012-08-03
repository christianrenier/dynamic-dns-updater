Dynamic DNS Updater
===================

Keep domain names in sync with your dynamic IP address.

Description
-----------

A tool for updating a Dynamic DNS service with your current IP if it has changed. Designed to be simple enough for the layperson to use, yet modular enough for easy implementation of rich features and support for disparate service providers.

#### Features

* Logging of events, as defined by the user.
* Logging of errors, as defined by the user.
* Updates any Dynamic DNS service which relies on simply requesting a URL.
* Usable under any operating system with Python installed.

Installation
------------

Set the folder to run recurrently with a job scheduling program such as Task Scheduler, Automator, or cron.

Example of cron set to run this tool every 15 minutes:

	*/15 * * * * python /home/user/Desktop/dynamic-dns-updater
	
Yup, that's it!

Usage
-----

All you need to do is add the update URL given to you by your Dynamic DNS service provider to the configuration file.

	config.cfg
	---------
	
	update_url = http://freedns.afraid.org/dynamic/update.php?yourUniqueUpdateUrl

#### Optional

You may set the location of your log file to be anywhere you wish. If it already exists, it will be appended to. If the file does not yet exist, one will automatically be created in the specified location.

	log_file = /home/user/Desktop/dnsupdater.log
	
You can also choose what events you want stored in the log file by marking them as 'true' or 'false'.

	[logging]
	log_errors = true
	log_changes = true
	log_no_changes = false
	


Contributing
------------

Please contact me with websites that return your public IP address, similar to those in the sitelist.txt file, so we can have a greater array of choices to use for this function. Also, let me know of any Dynamic DNS providers you would like to see supported and any features you would like to see added.