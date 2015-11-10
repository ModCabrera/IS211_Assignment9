#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Apple Stock loader"""

import requests
from bs4 import BeautifulSoup


def url_download(url):
    url_file = requests.get(url)
    return url_file.content

def get_table(webpage):
    soup_obj = BeautifulSoup(webpage, 'html.parser')
    header = []
    rows = []
    w_table = soup_obj.find_all('table', {'id':'obsTable'})
    counter = 0
    for row in w_table:
        header.append(row.find('tr').get_text())       
        row = row.find_all(class_ = 'wx-value')
        store = []
        for item in row:
            counter += 1
            store.append(item.text)
            if (counter % 19) == 0:
                rows.append(store)
                store = []
                continue
    print 'January 2015 Temperatures:', '\n', '-'*32
    output = 'High: {:^5}| Avg: {:^5}| Low:{:^5}'
    print '%s   %s   %s' % (header[0][1:5], header[0][6:10], header[0][11:16])
    day = 1
    for temp in rows:
        output = output.format(temp[0], temp[1], temp[2])
        print 'January', day, header[0][1:5], output
        day += 1


if __name__ == '__main__':
    link  = 'http://www.wunderground.com/history/airport/KNYC/2015/1/1/MonthlyHistory.html'
    webpage = url_download(link)
    table = get_table(webpage)
