'''
Created on Nov 5, 2019

@author: tfu
'''
from __future__ import absolute_import, division, print_function, unicode_literals
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
def loadData():
    dataset_path = keras.utils.get_file(r"D:\python\HUAWEI AI\resources\auto-mpg.data",
                                        r"http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
    
    column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight', 'Acceleration', 'Model Year', 'Origin']
    dataset = pd.read_csv(dataset_path, names=column_names,na_values = "?", comment='\t', sep=" ", skipinitialspace=True)
    
#    print('Find Empty Col')
#    print(dataset.isnull().any())
    dataset = dataset.dropna()
    return dataset

def makeSummary(train_dataset):
    train_stats = train_dataset.describe()
    train_stats.pop("MPG")
    train_stats=train_stats.transpose()
    print(train_stats)
    return train_stats

def drawSum(train_dataset):
    sns.pairplot(train_dataset[['MPG',"Cylinders", "Displacement", "Weight"]], 
                 diag_kind="kde")
    plt.show()

def autoNormed(train_dataset,test_dataset):

    train_labels = train_dataset.pop('MPG')
    test_labels = test_dataset.pop('MPG')
    
    train_dataset=(train_dataset - train_stats['mean']) / train_stats['std']
    test_dataset=(test_dataset - train_stats['mean']) / train_stats['std']
    print(train_dataset)
    
    return train_labels,test_labels,train_dataset,test_dataset

def makeBatch(train_dataset,train_labels,test_dataset,test_labels):
    train_slice = tf.data.Dataset.from_tensor_slices((train_dataset.values, train_labels.values))
    train_slice = train_slice.shuffle(1000).batch(500)
    
    test_slice = tf.data.Dataset.from_tensor_slices((test_dataset.values, test_labels.values))
    test_slice = test_slice.shuffle(1000).batch(500)
    return train_slice,test_slice

def makeModel():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
      ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse',optimizer=optimizer,metrics=['mae', 'mse'])
    model.summary()
    return model

def runModel(model,train_slice,test_slice):    
    history = model.fit_generator(train_slice, epochs=1000,validation_data=test_slice)
    model.save(r'D:\python\HUAWEI AI\HCIA-AI V2.0 Manual\mnistDenseExp2.h5')
    return history

def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mae'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mae'],label = 'Val Error')
    plt.ylim([0,5])
    plt.legend()
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mse'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mse'],label = 'Val Error')
    plt.ylim([0,20])
    plt.legend()
    plt.show()

if __name__=='__main__':
    dataset= loadData()
    train_dataset = dataset.sample(frac=0.8,random_state=0)
    test_dataset = dataset.drop(train_dataset.index)
    
    drawSum(train_dataset)
    
    train_stats = makeSummary(train_dataset)
    
    train_labels,test_labels,train_dataset,test_dataset=autoNormed(train_dataset,test_dataset)
    
    train_slice,test_slice=makeBatch(train_dataset,train_labels,test_dataset,test_labels)
    print(train_slice)
    print(test_slice)
    
    model=makeModel()
    hist=runModel(model,train_slice,test_slice)
    
    plot_history(hist)
    
    
    