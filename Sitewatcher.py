# check an RSS url for changes against a known state
# if updated, send an email
# Wed 04 Aug 2021 02:23:45 PM EDT 


import requests
import yagmail
import json
import io
import BSRSS

# This is a Python 2/3 compatibility hack
try:
    to_unicode = unicode
except NameError:
    to_unicode = str



receiver = "xx"
NEWS_URL = "https://elk4bhkjweeo6lzwhcmh.noticeable.news/feed.rss"

yag = yagmail.SMTP("xx")
#yag.send(
#    to=receiver,
#    subject="Yagmail test",
#    contents=body,
#    attachments=filename,
#)

# pull in what we have seen before
try:
   with open(f"{(NEWS_URL.split('/')[2])}.json") as infile:
      known_news = json.load(infile)
except: 
   known_news = {}
news_now = BSRSS.news(NEWS_URL)
   

for guid in news_now.keys():
   if guid not in known_news.keys():
      body = str(guid) + "\n" + news_now[guid]['description']
      yag.send(to=receiver, subject="--Zoom App Changelog Updated--", contents=body)
      known_news[guid] = news_now[guid]

with io.open(f"{(NEWS_URL.split('/')[2])}.json", 'w', encoding='utf8') as outfile:
    str_ = json.dumps(known_news,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
