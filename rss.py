import datetime
from datetime import timedelta
from urllib.request import urlopen
import re, os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def rss(bob):
    url = (bob)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    hashpattern = "<.*Hash.*Hash>"
    match_results = re.findall(hashpattern, html, re.IGNORECASE)
    for match in match_results:
        link = re.sub("^.*?<.*?>", "", match)
        link = re.sub("<.*>$", '', link)
        if (link not in library):
            hashset.add(link)
        else:
            print(link + ' is already accounted for...')
    linkpattern = "<.*http.*torrent.*>"
    match_results = re.findall(linkpattern, html, re.IGNORECASE)
    for match in match_results:
        link = re.sub("^.*?<.*?>", "", match)
        link = re.sub("<.*>$", '', link)
        if (link not in library):
            linkset.add(link)
        else:
            print(link + ' is already accounted for...')
    yield hashset
    yield linkset
def checkdate():
    curr = datetime.datetime.now()
    curr = curr.strftime('%Y%m%d')
    prev = str(open('S:/Codex/Documents/GitHub/nyaa-rss/.calc/prev.lst').read())
    calc = datetime.datetime.strptime(prev, '%Y%m%d')
    calc = calc + timedelta(days = 5)
    calc = calc.strftime('%Y%m%d')
    calc = int(calc)
    prev = int(prev)
    curr = int(curr)
    if curr >= calc: 
        log = open('S:/Codex/Documents/GitHub/nyaa-rss/.calc/prev.lst', 'w')
        print(curr, file=log)
        return 'one'
    else:
        return 'none'

clear_console()
isdo = checkdate()

if isdo == 'one':
    hashset = set()
    linkset = set()
    library = set(open('S:/Codex/Documents/GitHub/nyaa-rss/codex.lst').read().split())
    feeds = set(open('S:/Codex/Documents/GitHub/nyaa-rss/feeds.lst').read().split()) # Open file on read mode
    codexlst = open("S:/Codex/Documents/GitHub/nyaa-rss/codex.lst", "a")

    for bob in feeds:
        result = rss(bob)
        for hashs in next(result):
            print(hashs)
            print(hashs, file=codexlst)
        for links in next(result):
            print(links)
            print(links, file=codexlst)
    input('all feeds processed...\npress enter to quit...')
else:
    input('no feeds updated...\nto reduce trafic, try again later...\npress enter to quit...')

