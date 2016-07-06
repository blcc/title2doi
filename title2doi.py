#!/usr/bin/python
import bs4,sys
from termcolor import colored
import urllib

puredoi = True
reverse_print_order = True

# http://search.crossref.org/?q=tropical+cyclone+in+warming
#s = bs4.BeautifulSoup(open("example.html","r").read(),'lxml')

searchurl = 'http://search.crossref.org/?q='
keywords = "+".join(sys.argv[1:])

requrl = searchurl+keywords
s = bs4.BeautifulSoup(urllib.urlopen(requrl).read(),'lxml')
itemsList = s.findAll('td',{'class':'item-data'})

# find('p',{'class':'lead'}).text.strip()
titles = [ i.find('p',{'class':'lead'}).text.strip() for i in itemsList ]
extras = [ " ".join(i.find('p',{'class':'extra'}).text.split()) for i in itemsList ]
doiurls = [ i.find('div',{'class':'item-links'}).find('a')['href'] for i in itemsList]
authors = [ i.find('p',{'class':'expand'}) for i in itemsList]

if puredoi: doiurls = [ i.replace("http://dx.doi.org/","") for i in doiurls ] 

numlist = range(len(titles))
if reverse_print_order: numlist = numlist[::-1]



print '==================='
for i in numlist:
    print titles[i]
    if authors[i]: print colored(authors[i].text,"yellow")
    print colored(extras[i],"green")
    print colored(doiurls[i],"blue")
    print '==================='
