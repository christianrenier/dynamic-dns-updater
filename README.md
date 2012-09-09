Dynamic DNS Updater
===================

Keep domain names in sync with your dynamic IP address.

Avoid paying your Internet service provider for a static IP or increase your privacy by avoiding the need to use an IP that doesn't change.

Description
-----------

A tool for updating a Dynamic DNS service when your IP changes. Designed to be simple and forgiving enough for the layperson, yet feature rich enough for advanced users' needs.

#### Features

* User enabled logging of events.
* User enabled logging of errors.
* User enabled emailing of errors.
* User enabled emailing of IP address changes.
* Updates any Dynamic DNS service which relies on visiting a URL.
* Usable under any operating system with Python installed.
* Supports multiple update URLs.
* Supports sending to multiple email addresses.
* No local mail server required.
* Extremely forgiving of user mistakes.
* Tries to give feedback no matter where or how it's run, or what errors occur.

Usage
-----

All you have to do is add your information to `config.cfg`, then set the folder to run through Python with a job scheduling program, such as Task Scheduler, Automator, or cron.

*Example of cron set to run this tool every 15 minutes on OS X:*

	*/15 * * * * python /Users/username/Desktop/dynamic-dns-updater

Configuration
-----

Edit `config.cfg` with the following:

#### Your update URL

Copy and paste the update URL given to you by your Dynamic DNS provider.

	update_urls = http://freedns.afraid.org/dynamic/update.php?yourUniqueUpdateUrl
	
Multiple URLs should all be on the same line, separated only by a comma.

	update_urls = http://freedns.afraid.org/dynamic/update.php?yourUniqueUpdateUrl,http://www.example.com/anotherUpdateUrl

#### File locations

You may set the location of your log file to anywhere you wish. If it already exists, it will be appended to. If the file does not exist, it will automatically be created at the location you specify.

*Example of setting the log file in Linux:*

	log_file = /home/username/Desktop/dnsupdater.log
	
The IP cache file simply stores your current IP address between runs. It will automatically be created at the location you specify as well.

*Example of setting the IP cache file in Windows:*
	
	ip_cache_file = C:\Users\username\Desktop\ipcache
	
#### Logging choices

Choose what events you want written to the log file by marking them as true or false. `log_errors` will write any errors that occurred, `log_changes` will write any changes to your IP, and `log_unchanged` will write any time the program is run at all.

	[logging]
	log_errors = true
	log_changes = true
	log_unchanged = false
	
#### Gmail account

If you would like to send emails on certain events, fill in your Gmail login details. This is the account that mail will be sent *from*.

	[gmail_account]
	gmail_user = coolguy2000
	gmail_password = mysecretpass123
	
#### Mailing choices

Fill in `mail_receivers` with the email address you want mail sent *to*. The address can be the same as your Gmail account or a completely different one altogether. Then choose what events to mail out. `send_errors` sends an email if any errors occur and `send_changes` sends an email if your IP address changes.

	[mailing]
	mail_receivers = coolguy2000@gmail.com
	send_errors = true
	send_changes = false
	
You can also send to multiple email addresses by adding them all on one line, separated only by a comma.

	mail_receivers = coolguy2000@gmail.com,admin01@yahoo.com,joeschmoe@example.net


Contributing
------------

Contact me with websites that return your public IP address, similar to those in `sitelist.txt`, so they can be added. Also, let me know of any Dynamic DNS providers you would like to see supported, bugs you find, or features you want added.