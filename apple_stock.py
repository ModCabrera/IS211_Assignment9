#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Apple Stock loader"""

import requests
from bs4 import BeautifulSoup


def url_download(url):
    get_url = requests.get(url)
    return get_url.content

def get_table(webpage):
    soup_obj = BeautifulSoup(webpage, 'html.parser')
    fhandler = soup_obj.find_all('tr')
    print '  -------  Apple Stock Data  --------'
    output = '|Date: {:^15} | Close Price: {:^10}|'
    for row in fhandler:
        row = row.find_all('td', {'class':'yfnc_tabledata1'})
        if len(row) == 7:
            print output.format(row[0].contents[0], row[6].contents[0])
        
    
if __name__ == '__main__':
    link  = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
    webpage = url_download(link)
    table = get_table(webpage)
