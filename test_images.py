# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:40:39 2018

@author: User
"""

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Activation, PReLU, ZeroPadding2D
import numpy as np
import images_to_array
import web_parser

valid_num = 5000
batch_size = 200
num_classes = 1
epochs = 1



def test_images(data_x):
    data_x = data_x.astype('float32') / 255           

    model = Sequential()
    model.add(ZeroPadding2D((1, 1),input_shape = (100, 100, 3)))
    model.add(Conv2D(32, (3, 3)))
    model.add(BatchNormalization())                         #BatchNorm    
    model.add(PReLU()) 
    model.add(ZeroPadding2D((1,1)))

    model.add(Conv2D(32, (3, 3)))   
    model.add(BatchNormalization())                         #BatchNorm    
    model.add(PReLU())
    model.add(MaxPooling2D(pool_size=(2, 2)))               #2
    #model.add(Dropout(0.5))   #--------
    model.add(ZeroPadding2D((1,1)))

    model.add(Conv2D(64, (3, 3)))   
    model.add(BatchNormalization())                         #BatchNorm    
    model.add(PReLU())
    model.add(ZeroPadding2D((1,1)))
    #model.add(Dropout(0.5))

    model.add(Conv2D(64, (3, 3)))   
    model.add(BatchNormalization())                         #BatchNorm    
    model.add(PReLU())
    model.add(MaxPooling2D(pool_size=(2, 2)))               #3
    #model.add(Dropout(0.5))   #--------
    model.add(Flatten())

    model.add(Dense(4096))               #4
    model.add(BatchNormalization())                         #BatchNorm
    model.add(PReLU())
    #model.add(Dropout(0.25))
    
    #model.add(Dense(2048))                #4
    #model.add(BatchNormalization())                        #BatchNorm
    #model.add(PReLU())
    #model.add(Dropout(0.5))
    
    model.add(Dense(1000))                #4
    model.add(BatchNormalization())                         #BatchNorm
    model.add(PReLU())
    #model.add(Dropout(0.5))
    
    model.add(Dense(num_classes, activation='sigmoid'))     #5
    
    model.compile(loss = 'binary_crossentropy',
              optimizer = keras.optimizers.Adadelta(),
              metrics=['accuracy'])

    inputfile = 'cnn_model_with_ep1_100x100_noDP_Ep1'
    model.load_weights(inputfile)

    score2 = model.predict(data_x, verbose = 1)     #回傳array表示猜測的結果
    
    if score2.max() > 0.5:
        print('Warning!!! This website is not safe')
    else:
        print('This website is safe')

url_link = input('Input a url: ')

while 1:        
    web_parser.Crawl_the_website(url_link) 
    test_images(images_to_array.fromImgToArray())   
    url_link = input('Input a url: ')