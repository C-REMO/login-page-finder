#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# This was written for educational purpose only. Use it at your own risk.
# Author will not be responsible for any damage!

from sys import stdout
from signal import signal, getsignal, SIGINT
from urllib.request import Request, urlopen, URLError, HTTPError

class FindLoginPage():
	"""This class checks for login page"""
	def __init__ 	(
					self:'pointing to self',
					domain:'domain to search login page for',
					headers:'browser headers, some web sites require headers to open',
					sub_links:'sub links list for domain to search login page for',
					number_of_sub_links:'number of lines file linkovi.txt contains'
					):
						self.domain = domain
						self.headers = headers
						self.sub_links = sub_links
						self.number_of_sub_links = number_of_sub_links
						self.sub_link_counter = 0
						self.valid_number_of_links = 0
							
	def check (self):
		"""This function checks for valid login page if any exist"""
		for sub_link in self.sub_links:
			if not sub_link:
				break
			try:
				full_link = self.domain + '/' + sub_link.strip()
				request_link = Request(full_link, headers=self.headers)
				self.sub_link_counter+=1
				stdout.write("\r" + "Broj provjerenih linkova: %s/%s" %(self.sub_link_counter, self.number_of_sub_links))
				stdout.flush()
				response = urlopen(request_link)
			except HTTPError:
				pass
			except URLError:
				pass
			else:
				self.valid_number_of_links+=1
				print ("\nPronađen link: " + full_link)
		stdout.write("\n\n"+"Ukupan broj pronađenih validnih stranica: %s\n" %self.valid_number_of_links)

def load_data():
	"""This function sets all needed variables, checks if domain exists and loads file contests if file exist"""
	try:
		with open('linkovi.txt', 'r') as file:
			sub_links = (file.readlines())
			sub_link_count=len(sub_links)

		domain = input('Unesite link stranice u sledećem obliku \n(npr: stranica.com or www.stranica.com )>> ')
		headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64) Gecko/20071127 Firefox/2.0.0.11'}
		full_domain = 'http://' + domain
		domain_request = Request(full_domain, headers=headers)
		open_link = urlopen(domain_request)
		findloginpage = FindLoginPage 	(full_domain, headers, sub_links, sub_link_count)
		findloginpage.check()
	except URLError:
		print ("\nProvjerite unos, domena:", full_domain, "ne postoji.\n")
		return
	except HTTPError as greska:
		print ("\nStranica nije dostupna. Greška:", greska.code)
		return
	except IOError:
		print ("Greška: nije bilo moguće otvoriti datoteku 'linkovi.txt', provjerite da li postoji datoteka.")
		return

def credits	():
	"""Printing credits"""
	space(10); print ("\n\n")
	space(10); print ("#####################################")
	space(10); print ("#   Admin/Login Page Finder Script  #")
	space(10); print ("#     Skriptu doradio Omer Ramić    #")
	space(10); print ("#####################################")
	space(10); print ("\n\n")
		
def space (j):
	"""Making indentation for credit lines"""
	i = 1
	while i<=j:
		print (end=' ')
		i+=1

def Exit_gracefully(signum, frame):
	"""Used for clean exit if user abort with keyboard"""
	signal(SIGINT, original_sigint)
	try:
		if input("\n\nStvarno želite izaći? (d/n)> ").lower().startswith('d'):
			exit(1)
	except KeyboardInterrupt:
		print("\n\nOk ok, Izlazim")
		exit(1)
		
	signal(SIGINT, Exit_gracefully)

if __name__ == '__main__':
	original_sigint = getsignal(SIGINT)
	signal(SIGINT, Exit_gracefully)
	credits()
	load_data()

#Script made by Omer Ramić
#Best regards
