#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup

def news(xml_news_url):

    parse_xml_url = urlopen(xml_news_url)
    xml_page = parse_xml_url.read()
    parse_xml_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    feed = {}
    for getfeed in news_list:
        feed[getfeed.guid.text] = {'title' : getfeed.title.text, 'pubDate' : getfeed.pubDate.text, 'description' : getfeed.description.text}
        # print("\n")
        # print('\033[1;33m %s \033[1;m' %getfeed.title.text)
        # print('\033[1;32m %s \033[1;m' %getfeed.guid.text)
        # print('\033[1;35m %s \033[1;m' %getfeed.pubDate.text)
        # print("\n")
    return feed

