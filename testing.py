import os
import re

import requests

line_skip = {'https://sukebei.nyaa.si/', 'https://nyaa.si/'}

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def nyaa_rss(url):
    temp_list = []
    page = requests.get(url)
    html = page.text.splitlines()
    for func_line in html:
        parse_line = str(func_line)
        func_pattern = '.*<title.*title>'
        if re.match(func_pattern, parse_line):
            parsed = re.sub("^.*?<.*?>", "", parse_line)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            if parsed not in codex:
                temp_list.append(parsed)
        func_pattern = '.*<link.*link>'
        if re.match(func_pattern, parse_line):
            parsed = re.sub("^.*?<.*?>", "", parse_line)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            if parsed not in codex:
                temp_list.append(parsed)
        func_pattern = '.*<.*Hash.*Hash>'
        if re.match(func_pattern, parse_line):
            parsed = re.sub("^.*?<.*?>", "", parse_line)
            parsed = re.sub("<.*>$", '', parsed)
            parsed = re.sub('&#34;', "'", parsed)
            if parsed not in codex:
                temp_list.append(parsed)
    return temp_list

clear_console()

open("S:/OneDrive/Documents/GitHub/nyaa-rss/links.lst", "w", encoding='utf-8')

with open('S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst', 'r', encoding='utf-8') as codex_list:
    codex = codex_list.read().splitlines()
    
with open('S:/OneDrive/Documents/GitHub/nyaa-rss/feeds.lst', 'r', encoding='utf-8') as feeds:
    feeds = feeds.read().splitlines()
    pattern = r'.*Torrent File RSS'
    for uri in feeds:
        output = nyaa_rss(uri)
        for line in output:
            if line not in codex:
                if line not in line_skip:
                    if not re.match(pattern, line):
                        with open('S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst', 'a', encoding='utf-8') as codex_list:
                            codex_list.write(f"{line}\n")
                            print(line)
        print(f"---------------------")
input('all feeds processed...\npress enter to quit...')
