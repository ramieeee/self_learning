import tensorflow as tf
import numpy as np

# train AND operator
x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[1]]
x_data = np.array(x_data)
y_data = np.array(y_data)

# create model sequence
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid', input_shape=(2,)))

model.compile(tf.keras.optimizers.SGD(learning_rate=0.1), loss='binary_crossentropy', metrics = ['accuracy'])
history = model.fit(x_data, y_data, batch_size=4, epochs=400)

# save model as h5
model.save("test.h5")
