# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:42:47 2018

@author: User
"""
from bs4 import BeautifulSoup
import urllib
import re
import urllib.request



def getImage(url_list, name_of_file):
    header = {'User-Agent' : 'Mozilla'}    

    if(len(url_list) == 0):
        print("there is no images in this website to test")
    else:        
        for img_url in url_list:
            if(img_url.startswith('http') != True):
                img_url = 'http:' + img_url
            print('下載圖片中')
            print(img_url)
            
            req = urllib.request.Request(img_url, None, header)
            try:        #排除url失效的可能
                response = urllib.request.urlopen(req)
            except urllib.error.URLError:
                print('Oops 抓取 %s 時出了問題' %img_url)
                continue
                
            if(img_url.endswith('jpg') == True):
                img = open('%s.jpg' %name_of_file, 'wb')
                name_of_file += 1
                img.write(response.read())
                img.close()
                
            if(img_url.endswith('png') == True):
                img = open('%s.png' %name_of_file, 'wb')
                name_of_file += 1
                img.write(response.read())
                img.close()
                
            if(img_url.endswith('gif') == True):
                img = open('%s.gif' %name_of_file, 'wb')
                name_of_file += 1
                img.write(response.read())
                img.close()
                
        #for img_url in url_list:
        #    print(img_url)
        #    urllib.request.urlretrieve(img_url, '%s.jpg' %name_of_file, None, header)
        #    name_of_file += 1
        #    print("正在下載第%s張圖片" %name_of_file)

def Crawl_the_website(url):
    header = {'User-Agent' : 'Mozilla'}
    global name_of_file

    req = urllib.request.Request(url, None, header)
    response = urllib.request.urlopen(req)
    data = response.read()

    soup = BeautifulSoup(data, 'html.parser')
    img_tags = soup('img')     ##############每個網站都不同


    img_pattern = re.compile('((.+gif$)|(.+jpg$)|(.+png$))')
    img_url_list = list()      #用來存gif, png, jpg檔的url

    for img_tag in img_tags:
        for context in img_tag.attrs.values():
            if(type(context) == list):       #  context might be list object
               for value in context:
                   context = img_pattern.search(value)
                   if(context != None):
                       #print(context.string)
                       img_url_list.append(context.group(0))
            else:
                 context = img_pattern.search(context)
                 if(context != None):
                     #print(context.string)  
                     img_url_list.append(context.group(0))
    
    name_of_file = 0
    
    response.close()
    print(len(img_url_list))              
    print(img_url_list) 
        
    getImage(img_url_list, name_of_file)
