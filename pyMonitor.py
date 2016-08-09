from IPy import IP
from socket import gethostbyname

for ip in open('ips.txt'):
    ip = ip.strip()
    for bkl in open('blacklist.txt'):
        bkl = bkl.strip()
        try:
            gethostbyname(IP(ip).reverseNames()[0].split('.in')[0]+'.'+bkl)
            print '%s founded on the blacklist %s' %(ip,bkl)
        except:
            pass
    print
