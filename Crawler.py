#"-*- coding: utf-8 -*-" 
import urllib2
import socket
import datetime
from TextPareser import *
import re
starttime = datetime.datetime.now()

url_seeds = set(["http://oilbeater.com"])
url_visited = set([])
urls = set([])
url2file = {"http://oilbeater.com":1}
globalindex = 1

key2url = {'oilbeater':set(['oilbeater.com'])}
while len(url_seeds) > 0 and len(urls) < 1000:
    source = url_seeds.pop()
    try:
        f = urllib2.urlopen(source,None,3)
        text =  unicode(f.read(),'utf-8')
        wf = open(str(globalindex),'w')
        wf.write(text.encode('utf-8'))
        wf.close()
        url2file[source] = str(globalindex)
        globalindex = globalindex + 1
        url_visited.add(source)
    except (urllib2.HTTPError,urllib2.URLError,socket.timeout):
        text = ''
    finds = re.findall(r'href=["\']([^"\']*)["\'][^>]*>([^<]*)<',text,re.I)
    for x in finds:
        trimedUrl = trimUrl(x[0],"http://oilbeater.com")
        if  trimedUrl not in url_visited:
            if trimedUrl and trimedUrl.startswith("http://oilbeater.com") and trimedUrl.find("/css") == -1:
                urls.add(trimedUrl)
                if trimedUrl not in url_seeds:
                    url_seeds.add(trimedUrl)
                trimedKey = trimKey(x[1])
                if trimedKey:
                    if not key2url.has_key(trimedKey):
                        key2url[trimedKey] = set([])
                    key2url[trimedKey].add(trimedUrl)
endtime = datetime.datetime.now()
interval=(endtime - starttime).seconds
