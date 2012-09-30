import requests, traceback, codecs
from lxml import etree
from lxml.html import soupparser
import re, time, urllib, urlparse

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14'

def get(url, timeout=10.0):
    if 'http' not in url:
        url = url.strip()
        if url[0] == '/':
            url = 'http://www.bing.com'+url
        else:
            url = 'http://www.bing.com/search/'+url
    return requests.get(url, timeout=timeout, headers={'User-Agent':UA})

def get_urls(q, tree, on_error=traceback.print_exc):
    "Extract result and cache urls from a parsed results page"
    template = r'http://cc.bingj.com/cache.aspx?q=%s&d=%s&mkt=en-US&setlang=en-US&w=%s'
    for tag in tree.xpath(r'//*[@class="sa_cc"]'):
        try:
            parts = tag.get('u').split('|')
            cache = template % (urllib.quote(q), parts[2], parts[3])
            href = tag.xpath(r'div/div/h3/a')[0].get('href')
            yield (href, cache)
        except:
            on_error()
    return res

def get_next(tree):
    "get 'next page' link from an lxml-parsed results page"
    return tree.xpath('//a[@class="sb_pagN"]')[0].get('href')

def parse(page):
    try:
        return etree.fromstring(page)
    except:
        return soupparser.fromstring(page)

def query_url(q):
    "Takes a query and returns the url of the results page for that query"
    q = urllib.quote(q)
    return 'http://www.bing.com/search?q=%s&go=&qs=n&form=QBLH&pq=%s&sc=8-41&sp=-1&sk=' % (q, q)

def search(q, retries=3):
    "Generator which takes a search query and yields (page_url, cache_url) pairs"
    search_page = query_url(q)
    fail = False
    while not fail:
        for i in xrange(retries):
            fail = False
            raw = get(search_page).text
            tree = parse(raw)
            try:
                search_page = get_next(tree)
            except:
                fail = True
                continue
            break
        for e in get_urls(q, tree)):
            yield e

def get_cache(url):
    url = url.strip()
    p = urlparse.urlparse(url)
    parts = re.split(r'[^a-zA-Z0-9]+', p.path)
    while len(parts) > 0:
        q = 'site:%s %s' % (p.netloc, ' '.join(parts))
        for res, cache in search(q):
            if res == url:
                return get(cache).text
        parts = parts[1:]
