"""
Uma rede Neural baseada no vídeo: https://www.youtube.com/watch?v=_lsdUFM0BjA&list=PLHE8rK0D_mSBhi_OCeNuKM_4dWwdYeszg
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# IMPORTANDO OS DADOS (treinar) 
company = 'TSLA'

start = dt.datetime(2021, 4, 10) # one year before the data
final = dt.datetime(2022, 4, 10) # one year after the data

data = web.DataReader(company, 'yahoo', start, final)

# Preparing data

normalizing = MinMaxScaler(feature_range=(0, 1)) # seting values between 0 and 1 (0% - 100%)
normalizing_data = normalizing.fit_transform(data['Close'].values.reshape(-1, 1))

prediction_days = 30

x_train, y_label = [], []

for x in range(prediction_days, len(normalizing_data)): # preparing values to train
    x_train.append(normalizing_data[x-prediction_days:x, 0])
    # y_label.append(normalizing_data[x, 0])
