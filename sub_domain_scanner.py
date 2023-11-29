import requests
import time

#function to check status of sub domains for awesomeweb
def domain_scanner(subdomain_file):
	#opening the subdomains.txt
	with open(subdomain_file) as file:
		#reading all subdomains from sub_domains.txt file
		subdomains=file.readlines()
	#printing Table headers namely sub domain and status of sub domains
	print("Sub domain"+"	"+"Status")
	#looping over each sub domain and printing the return code if sub domain service is running or error message if unavailable.
	for i in range(len(subdomains)):
		try:
			r=requests.get('http://'+subdomains[i].replace('\n','.')+domain_name)
			print(subdomains[i].replace('\n','.')+domain_name+"	"+str(r.status_code))
		except requests.ConnectionError:
			print(subdomains[i].replace('\n','.')+domain_name+"     "+"Unable to reach sub domain.")
		
#setting domain as awesomeweb
domain_name='awesomeweb'

while True:

	#passing the file subdomains.txt to scan sub domains
	domain_scanner('subdomains.txt')
	#waiting for an interval of 1 minute to check next status of sub domains.
	time.sleep(60)
