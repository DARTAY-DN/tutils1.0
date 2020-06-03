import requests
import datetime
import sys
import time
import argparse
import os
import colorama
import csv
import json
import vk
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import itertools
import threading
import time
import base64
import urllib.request
from bs4 import BeautifulSoup
import socket

#желтый
#\033[33m
#Зеленый
#\033[32m = g.c
#Красный
#\033[31m = r.c
#Темно голубой
#\033[34m = t.g.c

os.system('clear')
banner = """\033[32m
▒█▀█▀█▒█▒█▒█▀█▀█░▐██▒██░░░▒▄█▀▀█
░░▒█░░▒█▒█░░▒█░░─░█▌▒██░░░▒▀▀█▄▄
░▒▄█▄░▒▀▄▀░▒▄█▄░░▐██▒██▄▄█▒█▄▄█▀
  		Coded By DARTAY\033[32m"""

print(banner)
time.sleep(3)
while True:
	menu = 			input("""
\033[34m_________SmsBomer_________
\033[34m|\033[31m[\033[33m1\033[31m] - \033[32mSmsHam 
	\033[34m_________VkPermission_________
\033[34m|\033[31m[\033[33m2\033[31m] - \033[32mVkTool
\033[34m_________Hack_________
\033[34m|\033[31m[\033[33m3\033[31m] - \033[32mSherlock 
\033[34m|\033[31m[\033[33m4\033[31m] - \033[32mMailSpam """)
	if menu == ('1'):
		os.system('clear')
		print('\033[32mЗапуск SmsHam...')
		os.chdir('Utils')
		time.sleep(2)
		os.system('python smsham.py')
	elif menu == ('2'):
		os.system('clear')
		print('\033[32mЗапуск VkTool   ...')
		os.chdir('Utils')
		os.system('python n.py')
	elif menu == ('3'):
		os.system('clear')
		print('\033[32mЗапуск Sherlock...')
		os.chdir('Utils')
		os.system('python sherl.py')
	elif menu == ('4'):
		os.system('clear')
		os.chdir('Utils')
		os.system('python MailSpam.py')
