import urllib2
import datetime
from TextPareser import trimUrl
import re
starttime = datetime.datetime.now()

url_seeds = set(["http://oilbeater.com"])
url_visited = set([])
urls = set([])
while len(url_seeds) > 0 and len(urls) < 50:
    source = url_seeds.pop()
    try:
        url_visited.add(source)
        f = urllib2.urlopen(source,None,15)
        text =  f.read()
    except (urllib2.HTTPError,urllib2.URLError):
        text = ''
    finds = re.findall(r'href=["\']([^"\']*)["\'][^>]*>(?:[^<]*)<',text,re.I)
    for x in finds:
        if  x not in url_visited:
            trimedUrl = trimUrl(x,source)
            if trimedUrl:
                urls.add(trimedUrl)
                url_seeds.add(trimedUrl)

endtime = datetime.datetime.now()
interval=(endtime - starttime).seconds
