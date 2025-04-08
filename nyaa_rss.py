import os
import re

import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)

line_skip = {'https://sukebei.nyaa.si/', 'https://nyaa.si/'}

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def nyaa_rss(url):
    temp_list = []
    hash_list = []
    link_list = []
    title_list = []
    csv_set = set([])
    title = ''
    info_hash = ''
    link = ''
    page = requests.get(url, verify=False)
    html = page.text.splitlines()
    for func_line in html:
        parse_line = str(func_line)
        func_pattern = '.*<title.*title>'
        if re.match(func_pattern, parse_line):
            title = re.sub("^.*?<.*?>", "", parse_line)
            title = re.sub("<.*>$", '', title)
            title = re.sub('&#34;', "'", title)
            if title not in codex:
                temp_list.append(title)
                title_list.append(title)
        func_pattern = '.*<link.*link>'
        if re.match(func_pattern, parse_line):
            link = re.sub("^.*?<.*?>", "", parse_line)
            link = re.sub("<.*>$", '', link)
            link = re.sub('&#34;', "'", link)
            if link not in codex:
                temp_list.append(link)
                link_list.append(link)
        func_pattern = '.*<.*Hash.*Hash>'
        if re.match(func_pattern, parse_line):
            info_hash = re.sub("^.*?<.*?>", "", parse_line)
            info_hash = re.sub("<.*>$", '', info_hash)
            info_hash = re.sub('&#34;', "'", info_hash)
            if info_hash not in codex:
                temp_list.append(info_hash)
                hash_list.append(info_hash)
        if title != '' and link != '' and info_hash != '':
            csv_line = f'{title};{link};{info_hash}'
            link = info_hash = title = ''
            csv_set.add(csv_line)
    return temp_list, title_list, link_list, hash_list, csv_set

clear_console()

#codex_csv = "S:/OneDrive/Documents/GitHub/nyaa-rss/codex.csv"
#codex_lst = "S:/OneDrive/Documents/GitHub/nyaa-rss/codex.lst"
#link_lst = "S:/OneDrive/Documents/GitHub/nyaa-rss/link.lst"
#hash_lst = "S:/OneDrive/Documents/GitHub/nyaa-rss/hash.lst"

open("links.lst", "w", encoding='utf-8')

file_path_set = {"hash.lst", "link.lst", "codex.lst", "codex.csv"}

for path in file_path_set:
    if not os.path.exists(path):
        open(path, 'w', encoding='utf-8')

with open('codex.lst', 'r', encoding='utf-8') as codex_list:
    codex = codex_list.read().splitlines()

with open('codex.csv', 'r', encoding='utf-8') as codex_csv:
    csv = codex_csv.read().splitlines()

with open('hash.lst', 'r', encoding='utf-8') as hash_:
    hash_file = hash_.read().splitlines()

with open('link.lst', 'r', encoding='utf-8') as link_:
    link_file = link_.read().splitlines()

with open('feeds.lst', 'r', encoding='utf-8') as feeds:
    feeds = feeds.read().splitlines()
    pattern = r'.*Torrent File RSS'
    for uri in feeds:
        output, output_title, output_link, output_hash, output_csv = nyaa_rss(uri)
        for line in output:
            if line not in codex:
                if line not in line_skip:
                    if not re.match(pattern, line):
                        with open('codex.lst', 'a', encoding='utf-8') as codex_list:
                            codex_list.write(f"{line}\n")
                            print(line)
        for line in output_csv:
            if line not in csv:
                with open('codex.csv', 'a', encoding='utf-8') as csv_list:
                    csv_list.write(f"{line}\n")
        for line in output_hash:
            if line not in hash_file:
                with open('hash.lst', 'a', encoding='utf-8') as hash_list:
                    hash_list.write(f"{line}\n")
        for line in output_link:
            if line not in link_file:
                with open('link.lst', 'a', encoding='utf-8') as link_list:
                    link_list.write(f"{line}\n")
        print(f"---------------------")
#input('all feeds processed...\npress enter to quit...')
