from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.models import load_model
from helpers import *

x_test, y_test = loaddata('D:/Datasets/Poker/pokersudden_change.data', True)
print("array_x: ", x_test, "size: ", x_test[0].__len__(), "array_y: ", y_test, "size: ", y_test[0].__len__())

loaded = load_model('poker_predictor.h5')

# Check its architecture
loaded.summary()

# Evaluate the model on the test data using `evaluate`
print('\n# Evaluate on test data')
results = loaded.evaluate(x_test, y_test, batch_size=32)
print('test loss, test acc:', results)