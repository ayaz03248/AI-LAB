from keras.models import Sequential
from keras.layers import Dense
import numpy
numpy.random.seed(7)
dataset = numpy.genfromtxt("cs-training.csv",delimiter=",", skip_header=1)
X = dataset[:100000,2:10]
Y = dataset[:100000,1]
evalX = dataset[100001:150000,2:10]
evalY = dataset[100001:150000,1]
model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(7,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=80,batch_size=50)
scores = model.evaluate(evalX,evalY)
print("\n%s: %.2f%%"%(model.metrics_names[1],scores[1]*100))
prediction = model.predict(X)
rounded = [round(x[0]) for x in prediction]
print(rounded)


