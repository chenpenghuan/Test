#!/usr/bin/env python
import urllib.request
import re
from bs4 import BeautifulSoup


def getdata(url="https://github.com/racaljk/hosts/blob/master/hosts"):
    try:
        data = urllib.request.urlopen(url).read()
        z_data = data.decode('UTF-8')
        soup = BeautifulSoup(z_data, 'lxml')
        a = soup.select(
            'table > tr > td')
        hostsfile = open('/etc/hosts', 'w', newline='')
        for i in a:
            hostsfile.write(i.get_text() + "\n")
        hostsbak = open('/etc/hosts.bak', 'r')
        hostsfile.write(hostsbak.read())
        hostsfile.close()
        hostsbak.close()
        print('hosts刷新成功')

    except Exception as err:
        print(str(err))

if __name__=="__main__":
	getdata()
