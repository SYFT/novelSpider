﻿# -*- coding: utf-8 -*-
# coding: url-8

# url configuration
base_url = "http://www.vodtw.com/Html/Book/33/33745/" 
index_url = base_url + "Index.html"

import os
base_file = os.path.abspath('.')

# cookie file configuration
cookie_file = os.path.join(base_file, "cookie.txt")

# output file configuration
out_file = os.path.join(base_file, "outfile.html")

# headers
headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Host":"www.vodtw.com",
	"Referer":"http://www.vodtw.com/Html/Book/33/33745/16806708.html",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
		}

