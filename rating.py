import sys
import urllib2
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

SEARCH_URL = "https://www.google.co.in/search?q="+SEARCH_NAME

#print SEARCH_URL

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = urllib2.Request(SEARCH_URL,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page,'html.parser')
rating={}
rating =soup.find_all("span", {"class":"IZACzd"})
print "IMDb and Rotten Tomatoes ratings:"
for r in rating:
    print r.text.strip()
about =soup.find("div", {"class":"sthby kno-fb-ctx"})
print about.text.strip()
