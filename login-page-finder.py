#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!

import signal, time, sys
from urllib2 import Request, urlopen, URLError, HTTPError

def Izadji_graciozno(signum, frame):
    	signal.signal(signal.SIGINT, original_sigint)
    	try:
        	if raw_input("\n\nStvarno želite izaći? (d/n)> ").lower().startswith('d'):
            		sys.exit(1)
    	except KeyboardInterrupt:
        	print("\n\nOk ok, Izlazim")
        	sys.exit(1)
    	signal.signal(signal.SIGINT, Izadji_graciozno)

def PronadjiAdmina():
	try:
		datoteka = open("linkovi.txt","r")
		link = raw_input("Unesite link stranice u sledećem obliku \n(npr: stranica.com or www.stranica.com )>> ")
		link = "http://"+link
		test_zahtjev = Request(link)
		otvori = urlopen(test_zahtjev)
	except URLError:
        	print "\nUnijeli ste pogrešan link, link:", link, "nije dostupan.\n"
		return
	except HTTPError :
		print "\nStranica nije dostupna. Greška:", greska.code
		return
	except IOError:
        	print("Greška: nije bilo moguce otvoriti datoteku 'linkovi.txt', provjerite da li postoji datoteka.")
		return

	pokusano=0
	ispravno=0
	broj_linija = sum(1 for line in open("linkovi.txt","r"))
	print "\n\nUkupan broj učitanih linkova za provjeru iznosi:", broj_linija,"\n"

	while True:
		pod_link = datoteka.readline()
		if not pod_link:
			break
		zahtjev_linka = link+"/"+pod_link
		zahtjev = Request(zahtjev_linka)
		pokusano+=1
    		sys.stdout.write("\r" + "Broj provjerenih linkova: %s/%s" %(pokusano, broj_linija))
   		sys.stdout.flush()
		try:
			odgovor = urlopen(zahtjev)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			ispravno+=1
			print "\nPronađen link: ",zahtjev_linka,
	sys.stdout.write("\n\n"+"Ukupan broj pronađenih validnih stranica: %s\n" %ispravno)

def ZahvaleIdu():
	Odmakni(10); print "\n\n"
	Odmakni(10); print "#####################################"
	Odmakni(10); print "#   Admin/Login Page Finder Script  #"
	Odmakni(10); print "#     Skriptu doradio Omer Ramić    #"
	Odmakni(10); print "#####################################"
	Odmakni(10); print "\n\n"

def Odmakni(j):
	i = 1
	while i<=j:
		print " ",
		i+=1

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, Izadji_graciozno)

ZahvaleIdu()
PronadjiAdmina()
