#"-*- coding: utf-8 -*-" 
print u"中无奈"
import urllib2
import datetime
from TextPareser import *
import re
starttime = datetime.datetime.now()

url_seeds = set(["http://oilbeater.com"])
url_visited = set([])
urls = set([])
key2url = {'oilbeater':set(['oilbeater.com'])}
while len(url_seeds) > 0 and len(urls) < 50:
    source = url_seeds.pop()
    try:
        url_visited.add(source)
        f = urllib2.urlopen(source,None,15)
        text =  unicode(f.read(),'utf-8')
    except (urllib2.HTTPError,urllib2.URLError):
        text = ''
    finds = re.findall(r'href=["\']([^"\']*)["\'][^>]*>([^<]*)<',text,re.I)
    for x in finds:
        if  x[0] not in url_visited:
            trimedUrl = trimUrl(x[0],source)
            if trimedUrl:
                urls.add(trimedUrl)
                url_seeds.add(trimedUrl)
                trimedKey = trimKey(x[1])
                if trimedKey:
                    if not key2url.has_key(trimedKey):
                        key2url[trimedKey] = set([])
                    key2url[trimedKey].add(trimedUrl)
endtime = datetime.datetime.now()
interval=(endtime - starttime).seconds
