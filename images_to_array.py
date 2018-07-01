# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 00:23:35 2018

@author: User
"""
import os
import cv2
import numpy as np
from PIL import Image 


def turn_git_to_images(gif_file, name_of_file):             #把gif換成jpg檔
    try:
        im = Image.open(gif_file)
    except IOError:
        print('Can not open name %d file' %gif_file)
        return 
    
    mypalette = im.getpalette()
    try:                        #把gif檔的每個frame轉換成.jpg檔
        while True:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('gifTojpg_%s.jpg' % name_of_file)
            name_of_file += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass

i = 0 

def fromImgToArray():                       #把路徑中的所有圖片處理成array
    images_list = os.listdir()
    global name_of_file
    name_of_file = 0
    gif_list = [turn_git_to_images(image, name_of_file) for image in images_list if image.endswith('gif')]
    
    images_list = os.listdir()              #重新讀取一次 
    images_list.remove("web_parser.py")
    images_list.remove("images_to_array.py")

    image_array_list = [cv2.imread(image_original) for image_original in images_list]

    image_array_list = [cv2.resize(image_array, dsize=(100, 100), interpolation=cv2.INTER_CUBIC) for image_array in image_array_list if image_array is not None]

 
    data_train = np.stack(image_array_list, axis = 0)           #堆疊出新的維度 ?x100x100x3
    return data_train 

