from urllib.request import urlopen
import re, os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def nyaa_rss(bob):
    url = (bob)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<.*Hash.*Hash.*>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for match in match_results:
        link = re.sub("^.*?<.*?>", "", match)
        link = re.sub("<.*>$", '', link)
        if (link not in codex):
            links = open("S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst", "a")
            print(link, file=links)
            print(link)
        else:
            print('Hash is already accounted for...')

clear_console()

codex =  set(open('S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst').read().split())
links = open("S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst", "w")
links.close
print('',file=links)
feeds = set(open('S:/OneDrive/Documents/GitHub/nyaa-rss/feeds.lst').read().split())

for feed in feeds:
    nyaa_rss(feed)

links =  set(open('S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst').read().split())

if links != set():
    codex = open("S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst", "a")
    clear_console()
    for line in links:
        print(line, file=codex)
        print(line)
    codex.close
else:
    clear_console()
    print('there are no new items in the provided feeds')

try:
    codex.close
except:
    pass
try:
    links.close
except:
    pass
try:
    feeds.close
except:
    pass

input('all feeds processed...\npress enter to quit...')
