#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Football stats"""
import requests
from bs4 import BeautifulSoup

def url_download(url):
    url_file = requests.get(url)
    return url_file.content
    
def get_table(webpage):
    print '               ----Top 20 Players NFL----        '
    output = '|Player: {:^17} | Team: {:^3} | TouchDowns: {:^3}|'
    soup_obj = BeautifulSoup(webpage, 'html.parser')
    obj_table = soup_obj.find_all(class_ = {'row1','row2'})
    for row in obj_table:
        print output.format(row.contents[0].text, row.contents[2].text, row.contents[6].text)
        

if __name__ == '__main__':
    link  = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns'
    webpage = url_download(link)
    table = get_table(webpage)
