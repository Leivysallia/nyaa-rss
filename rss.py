from urllib.request import urlopen
import re, os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
clear_console()

library =  set(open('S:/Codex/Documents/GitHub/python.testing/codex.lst').read().split())

def rss(bob):
    url = (bob)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<.*http.*torrent.*>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for match in match_results:
        link = re.sub("^.*?<.*?>", "", match)
        link = re.sub("<.*>$", '', link)
        if (link not in library):
            links = open("S:/Codex/Documents/GitHub/python.testing/links.lst", "a")
            print(link, file=links)
            print(link)
            links.close()
        else:
            print(link + ' is already accounted for...')

feeds = set(open('S:/Codex/Documents/GitHub/python.testing/feeds.lst').read().split()) # Open file on read mode

for bob in feeds:
    rss(bob)

input('all feeds processed...\npress enter to quit...')
