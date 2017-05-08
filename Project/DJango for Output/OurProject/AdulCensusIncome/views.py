from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	from keras.models import Sequential
	from keras.layers import Dense
	import csv
	from keras.utils import np_utils
	import keras
	import numpy
	import gc
	numpy.random.seed(7)
	dataset = numpy.genfromtxt("E:/University/Artificial Intelligence/Lab/LastProject/adult1.csv", delimiter=",", skip_header=1)
	X = dataset[1:32561, 0:14]
	Y = dataset[1:32561, 14]
	evalX = dataset[32551:, 0:14]
	evalY = dataset[32551:, 14]
	# evalX = dataset[22795:32562,0:14]
	# evalY = dataset[22795:32562,14]
	model = Sequential()
	model.add(Dense(12, input_dim=14, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(7, activation='relu'))
	model.add(Dense(6, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	model.fit(X, Y, epochs=100, batch_size=20)
	scores = model.evaluate(evalX, evalY)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
	prediction = model.predict(X)
	rounded = [round(x[0]) for x in prediction]
	if (scores[1] * 100 >= 50):
		return HttpResponse("<h1>Adult Salary Income</h1><hr /><br /><h3>Salary will be greater than 50000</h3>")
	else:
		return HttpResponse("<h1>Adult Salary Income</h1><hr /><br /><h3>Salary will be less than 50000</h3>")
	gc.collect()