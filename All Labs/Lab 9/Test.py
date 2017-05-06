import numpy
from keras.constraints import maxnorm
from keras.models import Sequential
from keras.datasets import cifar10
from keras.optimizers import SGD
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras import backend as K
K.set_image_dim_ordering('th')
seed = 7
numpy.random.seed(seed)



