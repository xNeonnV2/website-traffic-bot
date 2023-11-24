import random
import threading
import requests

lock = threading.Lock()
request_count = 0

os_list = ["Windows", "MacOS", "Linux", "J2ME/MIDP", "Macintosh", "Android", "Linux i686", "iPad", "ArchLinux", "HTC", "iOS", "Ubuntu", "Fedora", "Chrome OS", "BlackBerry OS", "Windows Phone", "FreeBSD", "Solaris", "Unix", "IBM OS/2", "Tizen", "KaiOS", "Raspbian", "Debian", "CentOS", "openSUSE", "Mageia", "Gentoo", "Slackware", "Red Hat Enterprise Linux", "Sailfish OS", "Alpine Linux", "Lubuntu", "Xubuntu", "Kubuntu", "Zorin OS", "Manjaro", "Linux Mint", "Deepin", "Puppy Linux", "Fedora Silverblue", "Clear Linux", "Chromium OS", "ReactOS", "Haiku", "OpenBSD", "NetBSD", "DragonFly BSD", "AIX", "HP-UX", "IRIX", "QNX", "AmigaOS", "MorphOS", "Plan 9", "Inferno", "Symbian OS", "Windows Mobile", "WebOS"]
browser_list = ["Safari", "Firefox", "Chrome", "InternetExplorer", "Opera", "Edge", "Brave", "Vivaldi", "UCBrowser", "Maxthon", "Dolphin", "Pale Moon", "Avant Browser", "Torch Browser", "Epic Browser", "Konqueror", "Midori", "Waterfox", "SeaMonkey", "Yandex Browser", "Slimjet", "Cent Browser", "Blisk", "Comodo Dragon", "Citrio", "SRWare Iron", "Qutebrowser", "Netscape Navigator", "Lunascape", "Flock", "IceDragon", "Orbitum", "GreenBrowser", "Rockmelt", "Sleipnir", "Coowon", "Superbird", "Basilisk", "Otter Browser", "Cyberfox", "QupZilla", "Gnuzilla", "Browzar", "Dooble", "Elinks", "Falkon", "Galeon", "K-Meleon", "Lynx", "NetSurf", "Puffin", "Rekonq", "Surf", "Uzbl", "Beaker", "Dillo", "Epic Privacy Browser", "Fennec", "GNOME Web", "Hv3", "iCab", "Iceape", "Kazehakase", "Links", "Min", "Netsurf", "OmniWeb", "Pale Moon", "Qutebrowser", "QupZilla", "Rekonq", "Sleipnir", "Surf", "Uzbl", "Vimprobable", "W3m", "Xombrero", "Yandex Browser"]
referral_list = ["https://www.google.com", "https://www.yahoo.com", "https://www.bing.com", "https://www.google.co.za", "https://www.google.ae", "https://www.google.ad", "https://www.google.ac", "https://www.google.com.af", "https://www.google.com.ag", "https://www.google.com.ai", "https://www.google.al", "https://www.google.am", "https://www.google.co.ao", "https://www.google.com.ar", "https://www.google.as", "https://www.google.at", "https://www.google.com.au", "https://www.google.az", "https://www.google.ba", "https://www.google.com.bd", "https://www.google.be", "https://www.google.bf", "https://www.google.bg", "https://www.google.com.bh", "https://www.google.bi", "https://www.google.bj", "https://www.google.com.bn", "https://www.google.bo", "https://www.google.com.br", "https://www.google.bs", "https://www.google.bt", "https://www.google.co.bw", "https://www.google.by", "https://www.google.com.bz", "https://www.google.ca", "https://www.google.cd", "https://www.google.cf", "https://www.google.cg", "https://www.google.ch", "https://www.google.ci", "https://www.google.co.ck", "https://www.google.cl", "https://www.google.cm", "https://www.google.cn", "https://www.google.com.co", "https://www.google.co.cr", "https://www.google.com.cu", "https://www.google.cv", "https://www.google.com.cy", "https://www.google.cz", "https://www.google.de", "https://www.google.dj", "https://www.google.dk", "https://www.google.dm", "https://www.google.com.do", "https://www.google.dz", "https://www.google.com.ec", "https://www.google.ee", "https://www.google.com.eg", "https://www.google.es", "https://www.google.com.et", "https://www.google.fi", "https://www.google.com.fj", "https://www.google.fm", "https://www.google.fr", "https://www.google.ga", "https://www.google.ge", "https://www.google.gg", "https://www.google.com.gh", "https://www.google.com.gi", "https://www.google.gl", "https://www.google.gm", "https://www.google.gp", "https://www.google.gr", "https://www.google.com.gt", "https://www.google.gy", "https://www.google.com.hk", "https://www.google.hn", "https://www.google.hr", "https://www.google.ht", "https://www.google.hu", "https://www.google.co.id", "https://www.google.ie", "https://www.google.co.il", "https://www.google.im", "https://www.google.co.in", "https://www.google.iq", "https://www.google.is", "https://www.google.it", "https://www.google.je", "https://www.google.com.jm", "https://www.google.jo", "https://www.google.co.jp", "https://www.google.co.ke", "https://www.google.com.kh", "https://www.google.ki", "https://www.google.kg", "https://www.google.co.kr", "https://www.google.com.kw", "https://www.google.kz", "https://www.google.la", "https://www.google.com.lb", "https://www.google.li", "https://www.google.lk", "https://www.google.co.ls", "https://www.google.lt", "https://www.google.lu", "https://www.google.lv", "https://www.google.com.ly", "https://www.google.co.ma", "https://www.google.md", "https://www.google.me", "https://www.google.mg", "https://www.google.mk", "https://www.google.ml", "https://www.google.com.mm", "https://www.google.mn", "https://www.google.ms", "https://www.google.com.mt", "https://www.google.mu", "https://www.google.mv", "https://www.google.mw", "https://www.google.com.mx", "https://www.google.com.my", "https://www.google.co.mz", "https://www.google.com.na", "https://www.google.com.nf", "https://www.google.com.ng", "https://www.google.com.ni", "https://www.google.ne", "https://www.google.nl", "https://www.google.no"]

def send_request(url):
    global request_count
    headers = {
        'User-Agent': f'{random.choice(os_list)}/{random.choice(browser_list)}',
        'Referrer': random.choice(referral_list),
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with lock:
            request_count += 1
            print(f'\033[92mSuccess \033[0m| Requests Sent: {request_count} | Ref: {headers["Referrer"]} | OS: {headers["User-Agent"].split("/")[0]}\033[0m')

def start_traffic(url, threads):
    while True:
        for _ in range(threads):
            threading.Thread(target=send_request, args=(url,)).start()

def main():
    print('''
    
                                                    
                              ,...  ,...,,          
MMP""MM""YMM                .d' "".d' ""db          
P'   MM   `7                dM`   dM`               
     MM  `7Mb,od8 ,6"Yb.   mMMmm mMMmm`7MM  ,p6"bo  
     MM    MM' "'8)   MM    MM    MM    MM 6M'  OO  
     MM    MM     ,pm9MM    MM    MM    MM 8M       
     MM    MM    8M   MM    MM    MM    MM YM.    , 
   .JMML..JMML.  `Moo9^Yo..JMML..JMML..JMML.YMbmd' 
   
================- - - Made By xNeonn - - -===================                                                 
                                                    
    
    ''')

    url = input('> [xNeonn] • Enter the URL: ')
    threads = int(input('> [xNeonn] • Enter the number of threads: '))

    start_traffic(url, threads)

if __name__ == '__main__':
    main()
