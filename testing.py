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
            with open("S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst", "a") as links:
                print(link, file=links)
                print(link)
        else:
            print('Hash is already accounted for...')

clear_console()

open("S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst", "w")

with open('S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst', 'r') as f:
    codex = f.read().splitlines()
    
with open('S:/OneDrive/Documents/GitHub/nyaa-rss/feeds.lst', 'r') as feeds:
    feeds = feeds.read().splitlines()
    for feed in feeds:
        nyaa_rss(feed)

with open('S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst') as links:
    if links != []:
        with open("S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst", "a") as codex:
            clear_console()
            for line in links:
                codex.write(line)
                print(line)
    else:
        clear_console()
        print('there are no new items in the provided feeds')

input('all feeds processed...\npress enter to quit...')
