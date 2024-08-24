

import requests 
import sys
import pyfiglet
 
ascii_banner = pyfiglet.figlet_format("Jok3r Cyber Security")
print(ascii_banner)


dir_listesi = open("dir.txt").read() 
directories = dir_listesi.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:"  ,dir_enum)



		                #C*#
#dir.py ile dir.txt dosyası aynı dizinde bulunmak zorundadır.

#Örnek kullanım : python3 dir.py HEDEFSİTE.COM veya IP ADRESİ.

#dir.txt = directory listesinin bulunduğu metin belgesi.

#dir.txt dosyasının içeriğini hedef ve amacınıza göre istediğiniz gibi değiştirebilirsiniz...

#Jok3r
