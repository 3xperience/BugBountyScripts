import re, socket, sys, requests

class HTTPInformation():
	def __init__(self, host):
		self.ip, self.domain = self.resolveDNS(host)
		self.serverInfo()
	def serverInfo(self):
		r = requests.get('http://'+self.domain)
		self.server = r.headers['server']
		self.content = r.text
		print(self.content)
	def resolveDNS(self,host):
		if(re.match('[0-9]{1,3}(\.[0-9]{1,3}){3}',host)):
			domain = socket.gethostbyaddr(host)
			ip = host
		elif(re.match('[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,4}',host)):
			ip = socket.gethostbyname(host)
			domain = (host)
		else:
			help()
			sys.exit(1)
		return ip, domain


def help():
	print("Usage: BasicRecon.py -h google.ca")
	print("-h\t|\tDefines the host")


	# 192.168.0.1 || google.com

if __name__ == '__main__':
	args = sys.argv
	numIn = len(args)
	# print(args, numIn)
	info = HTTPInformation(args[1])

	# Argument handling