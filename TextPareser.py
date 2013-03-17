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
    trimedKey = findkey.strip()
    return re.sub(r'<[^>]*?>',' ',trimedKey,0,re.IGNORECASE)
    
def findTitle(text):
    title = re.findall(r'<title[^>]*?>(.*?)(?=</title>)',text,re.IGNORECASE|re.MULTILINE|re.DOTALL)
    return [trimKey(x) for x in title]

def findHx(text):
    Hx = re.findall(r'<h(\d)[^>]*?>(.*?)(?=</h\1>)',text,re.IGNORECASE|re.MULTILINE|re.DOTALL)
    return [trimKey(x[1]) for x in Hx]

def findP(text):
    P = re.findall(r'<p[^>]*?>(.*?)(?=</p>)',text,re.IGNORECASE|re.MULTILINE|re.DOTALL)
    return [trimKey(x) for x in P]
text = '<h2>asdfa<>dfa<1></p>asdfa<>dfa</h2><h1>asdfa<>dfa</h1>'
print trimKey(text)

