# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 01:26:45 2018

@author: User
"""
import numpy as np


cars =  np.load('cars_data_train_50x50.npy')
nude = np.load('test_nude_data_50x50.npy')
otherimg = np.load('norPeople_data_test_50x50.npy')

print(nude.shape)
print(cars.shape)
print(otherimg.shape)

data_train = np.concatenate((nude, cars, otherimg), axis = 0)     
print(data_train.shape)

label_y1 = np.ones(10027)
label_y0 = np.zeros(12719)

label_y = np.concatenate((label_y1, label_y0), axis = 0)
print(label_y.shape)
#data_train = np.concatenate([data_train, label_y], axis = 3)
#print(data_train.shape)

#rand_state = np.random.RandomState(1337)
#rand_state.shuffle(data_train)
#rand_state.seed(1337)
#rand_state.shuffle(label_y)

print(data_train.shape)
print(label_y.shape)

np.save("test_train_50x50", data_train)
np.save("test_label_y_50x50", label_y)