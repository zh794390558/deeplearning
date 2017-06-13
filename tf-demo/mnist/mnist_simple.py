from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import argparse

from six.moves import xrange 
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.dataset.mnist import read_data_sets

FLAGS = None

def main(_):
	print("Downloding and reading data sets...")
	mnist = read_data_sets(FLAGS.data_dir, one_hot=True)

	# create model
	x = tf.placeholder(tf.float32, [None, 784])
	W = tf.Variable(tf.zeros([784, 10]))
	b = tf.Variable(tf.zeros([10]))
	y = tf.matmul(x, W) + b

	y_ = tf.placeholder(tf.float32, [None, 10])

	#Define loss and optimizer
	# the raw formulation of cross-entropy
	# tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.softmax(y)),
	# 					reduction_indices=[1]))
	# can be numercically unstable
	# so here we use tf.nn.softmax_cross_entropy_with_logits on the raw
	# outputs of 'y', and then average across the batch.
	cross_entropy = tf.reduce_mean(
			tf.nn.softmax_cross_entropy_with_logtis(logits=y, labels=y_)
			)
	train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


	sess = tf.InteractiveSession()
	tf.global_variables_initializer().run()

	#train
	print("trainning for %s steps" % FLAGS.num_steps)
	for _ in xrange(FLAGS.num_steps):
		batch_xs, batch_ys = mnist.train.next_batch(100)
		sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

	# test trained model
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print("accuracy: %s" % sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_dir', type=str, default='./data', help="Directory for storing data")
	parser.add_argument('--num_steps', type=int, default=10000, help='number of trainnig steps to run')
	FLAGS = parser.parse_args()
	tf.app.run(main)

