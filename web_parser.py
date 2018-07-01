# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:42:47 2018

@author: User
"""
from bs4 import BeautifulSoup
import urllib
import re

header = {'User-Agent' : 'Mozilla'}

req = urllib.request.Request('https://getrelax.club/', None, header)
response = urllib.request.urlopen(req)
data = response.read()

soup = BeautifulSoup(data, 'html.parser')
#print(soup.contents)

#用tags來尋找圖檔
img_tags = soup('img')
#print(img_tags)
#re = re.findall('.gif', img_tags.)
#print(re)

img_pattern = re.compile('(.+gif$)|(.+jpg$)|(.+png$)')

for img_tag in img_tags:
    for context in img_tag.attrs.values():
      if(type(context) == list):
          for value in context:
              context = img_pattern.match(value)
              if(context != None):
                  print(context.string)
      else:
          context = img_pattern.match(context)
          if(context != None):
              print(context.string)  
      

