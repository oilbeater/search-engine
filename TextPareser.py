import re
def trimUrl(findUrl , currentUrl):
    findUrl = findUrl.strip()
    if findUrl.startswith('/'):
        findUrl = currentUrl + findUrl
    if findUrl.endswith('/'):
        findUrl = findUrl[:-1]
    if not (findUrl.startswith('http') or findUrl.startswith('https')):
        return ''
   # filename = re.search(r'/([^/]*)$',findUrl)
   # suffix = re.search(r'\.(.*)',filename.group(1))
   # if suffix!=None and suffix.group(1) not in ['html','htm','']:
   #     return ''
    return findUrl

def trimKey(findkey):
    return findkey.strip()


findUrl = '   http://oilbeater.com/  '
print trimUrl(findUrl,'http://oilbeater.com')