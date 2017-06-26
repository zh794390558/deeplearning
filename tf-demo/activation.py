# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:35:43 2017

@author: Administrator
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)

y_relu = tf.nn.relu(x)
y_sigmoid = tf.nn.sigmoid(x)
y_tanh = tf.nn.tanh(x)
y_softplus = tf.nn.softplus(x)
y_softmax = tf.nn.softmax(x)

sess = tf.Session()

y_relu, y_sigmoid, y_tanh, y_softplus, y_softmax = sess.run([
    y_relu, 
    y_sigmoid, 
    y_tanh, 
    y_softplus, 
    y_softmax])
    
    
plt.figure(1, figsize=(8,6))
plt.subplot(221)
plt.plot(x, y_relu, c='r', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x, y_sigmoid, c='r', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()
