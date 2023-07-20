# Copynright 2023 - Slowqzx

import os,  time, requests, sys, threading
PyVer = str(sys.version)

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
cls()

def xx(PROXY, url):
    try:
        s = requests.sion()
        s.proxies = {'http': PROXY}
        s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = s.get(url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 200:
            print (PROXY + '   Valid')
            with open('valid.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print (PROXY + '   Invalid')
    except:
        print (PROXY + '   Invalid')
def main():
    try:
        if '3.' in PyVer:
            try:
                fileproxy = input(' [+] File: ')
            except:
                print('  [-] Error : Enter Your Proxy List!')
                sys.exit()
        elif '2.' in PyVer:
            try:
                fileproxy = raw_input(' [+] File: ')
            except:
                print('  [-] Error : Enter Your Proxy List!')
                sys.exit()
        else:
            print(' Unknown Version!')
    except:
        pass
        sys.exit()
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://instagram.com'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for i in thread:
        i.join()
main()