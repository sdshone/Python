import sys
import urllib2
import re
from bs4 import BeautifulSoup

if len(sys.argv)<2:
    print "Provide name."
    exit()
if len(sys.argv)>2:
    print "Provide name using \"\"."
    exit()


SEARCH_NAME = sys.argv[1]
#SEARCH_NAME += "age"
SEARCH_NAME =SEARCH_NAME.replace(" ",'+')

SEARCH_URL = "https://www.google.co.in/search?q="+SEARCH_NAME+"+smartprix"

#print SEARCH_URL

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = urllib2.Request(SEARCH_URL,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page,'html.parser')

smart =soup.find("cite", {"class":"iUh30"}).text.strip()
print smart

req = urllib2.Request(smart,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page,'html.parser')
#rating =soup.find_all("h1")
price=[]
rating =soup.find("div", {"id":"compare-prices"})
rating1 = rating.find_all("a", {"class":"_fll"})
price = rating.find_all("div", {"class":"_flr price"})
#print rating
storelist=[]
for r in rating1:
    storelist.append(r.attrs["title"])

for r,p in (zip(range(len(storelist)),price)):
    print storelist[r]+"  "+p.get_text()
#print storelist





#smart =rating[0].find("img")
#smart = smart.attrs['alt']
