bing_fetcher
============

Simple Python library to get search results and cached pages from Bing

example
-------
    >> import bing_fetcher as f
    >> next(f.search('oranges'))
    ('http://en.wikipedia.org/wiki/Orange_(fruit)',
     'http://cc.bingj.com/cache.aspx?q=oranges&d=4632792985175077&mkt=en-US&setlang=en-US&w=697d91b8,38deda1d')
    >> f.get_cache('http://en.wikipedia.org/wiki/Orange_(fruit)')[:1000]
    u'<base href="http://en.wikipedia.org/wiki/Orange_(fruit)"/><meta http-equiv="content-type" content="text/html; charset=utf-8"/><!-- Banner:Start --><style type="text/css">#b_cpb{color: black; font: normal normal normal small normal arial,sans-serif} #b_cpb a{color: blue; text-decoration: underline; font-weight:normal}</style><!--LocalizedDate:9/27/2012--><!--InvariantDate:9/27/2012--><table width="100%" style="background-color:#fff; text-align:left;" border="1" bordercolor="#909090" cellpadding="5"><tr><td><span id="b_cpb"><!-- Title:Start --><div>You have reached the cached page for <strong><a href="http://en.wikipedia.org/wiki/Orange_(fruit)" h="ID=SERP,5003.1">http://en.wikipedia.org/wiki/Orange_(fruit)</a></strong></div><!-- Title:End --><!-- Content:Start --><div style="margin-top:1em;">Below is a snapshot of the Web page as it appeared on <strong>9/27/2012</strong> (the last time our crawler visited it). This is the version of the page that was used for ranking your search results'
