import subprocess
from pip._vendor.colorama import Fore
import threading
import time
import os
#import layn

subprocess.call('start https://discord.gg/akargang', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)

#diabloakar
bammer = '''

████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄  
███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███ 
███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███ 
███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███ 
███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███ 
████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀  
                                          ▀                    

'''
print()
print(Fore.RED+bammer)
print(Fore.WHITE+'|'+Fore.BLUE+'| >'+Fore.WHITE+' Coded By ')
print(Fore.WHITE+'|'+Fore.BLUE+'| >'+Fore.WHITE+' Diablo Akar & Yusuf Akar ')
print()
kadi = 'admin'
sifre = 'root'

kullaniciadi = input(Fore.WHITE+'|'+Fore.BLUE+'Kullanıcı adını giriniz'+Fore.WHITE+'| > ')

if kullaniciadi == kadi:
    print('Kullanıcı adı doğru sırada şifreniz var!')
    s1fre = input(Fore.WHITE+'|'+Fore.BLUE+'Şifrenizi giriniz'+Fore.WHITE+'| > ')
    if s1fre == sifre:
        print(Fore.GREEN+'Oturum başarıyla açıldı giriş yapılıyor')
        time.sleep(5) # Buradan sonra ekleyeceğiniz komutlar size bağlıdır iyi kodlamalar :)
if kullaniciadi != kadi: # yerine elsede kullanılabilir
    print('Yanlış kullanıcı adı veya şifre girdiniz program kendisini 5 saniye sonra kapatacaktır!')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print(Fore.RED+'PROGRAM KENDİNİ KAPATIYOR')
    time.sleep(3)
if s1fre != sifre:
    print('Yanlış kullanıcı adı veya şifre girdiniz program kendisini 5 saniye sonra kapatacaktır!')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print(Fore.RED+'PROGRAM KENDİNİ KAPATIYOR')
    time.sleep(3)