# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:16:46 2018

@author: User
"""
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Activation, PReLU, ZeroPadding2D
from keras import backend as K
import numpy as np

valid_num = 8000
batch_size = 200
num_classes = 1
epochs = 2

data_x = np.load('data_train_100x100.npy')
data_y = np.load('label_y_100x100.npy')

data_x = data_x.astype('float32') / 255    #換成60000x764 且為float的矩陣, 並轉換精確度
data_y = data_y.astype('float32')          #換成10000x764 且為float的矩陣, 並轉換精確度
input_shape = data_x.shape[1], data_x.shape[2], data_x.shape[3]
print(input_shape)

model = Sequential()
model.add(ZeroPadding2D((1, 1),input_shape = input_shape))
model.add(Conv2D(32, (3, 3)))
model.add(BatchNormalization())                         #BatchNorm    
model.add(PReLU()) 
model.add(ZeroPadding2D((1,1)))

model.add(Conv2D(32, (3, 3)))   
model.add(BatchNormalization())                         #BatchNorm    
model.add(PReLU())
model.add(MaxPooling2D(pool_size=(2, 2)))               #2
model.add(Dropout(0.5))   #--------
model.add(ZeroPadding2D((1,1)))

model.add(Conv2D(64, (3, 3)))   
model.add(BatchNormalization())                         #BatchNorm    
model.add(PReLU())
model.add(ZeroPadding2D((1,1)))
model.add(Dropout(0.5))

model.add(Conv2D(64, (3, 3)))   
model.add(BatchNormalization())                         #BatchNorm    
model.add(PReLU())
model.add(MaxPooling2D(pool_size=(2, 2)))               #3
model.add(Dropout(0.5))   #--------
model.add(Flatten())

model.add(Dense(4096))               #4
model.add(BatchNormalization())                         #BatchNorm
model.add(PReLU())
model.add(Dropout(0.25))

#model.add(Dense(2048))                #4
#model.add(BatchNormalization())                        #BatchNorm
#model.add(PReLU())
#model.add(Dropout(0.5))

model.add(Dense(1000))                #4
model.add(BatchNormalization())                         #BatchNorm
model.add(PReLU())
model.add(Dropout(0.5))

model.add(Dense(num_classes, activation='sigmoid'))     #5

model.compile(loss = 'binary_crossentropy',
              optimizer = keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(data_x[valid_num :], data_y[valid_num :],
          batch_size = batch_size,
          epochs = epochs,
          verbose = 1,
          validation_data = (data_x[: valid_num], data_y[: valid_num]))

score1 = model.evaluate(data_x[valid_num :], data_y[valid_num :], verbose = 1)
score2 = model.evaluate(data_x[: valid_num], data_y[: valid_num], verbose = 1)

outfile = 'cnn_model_with_ep2_100x100_DP_2FCN'
model.save_weights(outfile)

print('epochs: %d, batch size: %d' %(epochs, batch_size))
print('Test ideal cost:', score1[0])
print('Test ideal accuracy:%f ' %(score1[1] * 100))
print('Test loss:', score2[0])
print('Test accuracy:', score2[1])