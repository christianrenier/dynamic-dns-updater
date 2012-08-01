class Cacher:

	def __init__(self, cache_location):
		self.errors = []
		self.old_ip = None
		self.cache_location = cache_location

	def get_old_ip(self):
		file = open(self.cache_location, 'w+')
		self.old_ip = file.read()
		file.close()
		if not self.old_ip:
			self.old_ip = 'initial state'
		return self.old_ip

	def store_new_ip(self, ip):
		file = open(self.cache_location, 'w')
		file.write(ip)
		file.close()
