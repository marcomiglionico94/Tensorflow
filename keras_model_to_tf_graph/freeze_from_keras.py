from wide_resnet import WideResNet
import os, argparse
import tensorflow as tf
import numpy as np
import cv2
from pyagender import PyAgender
from tensorflow.python.platform import gfile
import utils_func
 
 # Directory to Save the model
os.makedirs('./model', exist_ok=True)

from keras import backend as K
# This line must be executed before loading Keras model.
K.set_learning_phase(0)


# Keras Model you want to save
model = WideResNet(64)()
model.load_weights("./resnet_weights/weights.28-3.73.hdf5")
model.summary()

# Save
saver = tf.train.Saver()
saver.save(K.get_session(), './model/keras_model.ckpt')

# Print output layers
print(model.output)
