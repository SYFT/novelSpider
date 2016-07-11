# -*- coding: utf-8 -*-
# coding: url-8

# package import 
import urllib, urllib2, cookielib

# reload language
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from config import *

cookie = cookielib.MozillaCookieJar(cookie_file)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

print "Spider begin:"

print "index_url: ", index_url
postdata = None
request = urllib2.Request(index_url, postdata, headers)
response = opener.open(request, timeout = 1000)
# print response.read()
result = response.read()
result.encode()
out = open(out_file, "wb")
out.write(result)
out.close()
unicode(str(result))
