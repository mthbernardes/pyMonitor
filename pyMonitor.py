from socket import gethostbyname

for ip in open('ips.txt'):
    ip = ip.strip()
    for bkl in open('blacklist.txt'):
        bkl = bkl.strip()
        try:
            gethostbyname('.'.join(ip.split('.')[::-1])+'.'+bkl)
            print '%s founded on the blacklist %s' %(ip,bkl)
        except:
            pass
    print
