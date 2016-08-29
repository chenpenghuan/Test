# encoding:UTF-8
import urllib.request
import re
from bs4 import BeautifulSoup


def getdata ( url="http://zeus.softweek.net/item-slt-1.html" ):
    try:
        data = urllib.request.urlopen ( url ).read ( )
        z_data = data.decode ( 'UTF-8' )
        soup = BeautifulSoup ( z_data , 'lxml' )
        a = soup.select ( '#OSC_Content > div.SpaceList > div > div.BlogContent > p > span > span > a' )
        urls = re.compile ( r'.*[\d]*\.txt' )
        for i in a:
            if i.get ( 'href' )[ -4: ] == '.txt':
                hosts_url = i.get ( 'href' )
                if urls.match ( hosts_url ):
                    break
        hosts = urllib.request.urlopen ( hosts_url ).read ( )
        hostsfile = open ( 'C:\WINDOWS\system32\drivers\etc\hosts' , 'wb' )
        hostsfile.write ( hosts )
        hostsfile.close ( )
        input ( '已更新HOSTS，按Enter键结束程序!' )
    except Exception as err:
        input ( str ( err ) )


getdata ( )
