import atexit, datetime, os, re, requests, sys
from datetime import timedelta
from os.path import expanduser

def debug():
    atexit.register(lambda: input("Press Enter To Quit."))
def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def file_not_found():
    sys.exit()
def check_files():
    if not os.path.exists(codexlst):
        file = open(codexlst, 'w')
        file.close
    if not os.path.exists(prevlst):
        file = open(prevlst, 'w')
        print('19700101', file=file)
        file.close()
    if not os.path.exists(feedslst):
        file = open(feedslst, 'w')
        file.close
        print('there are no feeds specified in feeds.lst\nplease find the feeds.lst in ' + feedslst + '\nremember that the only feeds that are currently supported are ones from sukebei.nyaa.si and nyaa.si\nthank you.')
        file_not_found()
def read_rss(url):
    page = requests.get(url)
    html = page.text.splitlines()
    for line in html:
        parseline = str(line)
        pattern = '.*<title.*title>'
        if re.match(pattern, parseline):
            parsed = re.sub("^.*?<.*?>", "", parseline)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            templist.append(parsed)
        pattern = '.*<link.*link>'
        if re.match(pattern, parseline):
            parsed = re.sub("^.*?<.*?>", "", parseline)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            templist.append(parsed)
        pattern = '.*<.*Hash.*Hash>'
        if re.match(pattern, parseline):
            parsed = re.sub("^.*?<.*?>", "", parseline)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            templist.append(parsed)
    return templist
def check_date():
    curr = datetime.datetime.now()
    curr = curr.strftime('%Y%m%d')
    prev = str(open(prevlst).read().split())
    calc = datetime.datetime.strptime(prev, "['%Y%m%d']")
    calc = calc + timedelta(days = 5)
    calc = calc.strftime('%Y%m%d')
    if curr >= calc:
        log = open(prevlst, 'w')
        print(curr, file=log)
        return 'run'
    else:
        force = input('it is not time to run program.\nwould you like to force update anyway?\ntype run to force update: ')
        return force

home = expanduser('~')
data = '/.config/nyaa-rss/'
codexlst = str(home + data + 'codex.lst').replace('\\', '/')
feedslst = str(home + data + 'feeds.lst').replace('\\', '/')
prevlst = str(home + data + 'prev.lst').replace('\\', '/')

debug()
clear_console()
check_files()
run = check_date()
templist = []

if run == 'run':
    library = set(open(codexlst).read().split())
    feeds = set(open(feedslst).read().split())
    codex = open(codexlst, "a", encoding="utf-8")
    pattern = r'Nyaa.*Torrent File RSS'
    for uri in feeds:
        output = read_rss(uri)
        for line in output:
            if line not in library:
                if line != 'https://nyaa.si/':
                    if not re.match(pattern, line):
                        print(line, file=codex)
                        print(line)
    input('all feeds processed.\npress enter to quit.')
else:
    input('|:NO FEEDS UPDATED:|\npress enter to quit.')
