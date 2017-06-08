import argparse
import math
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

# feature: shape [4,2]
def make_graph(feature, labels, num_hidden=8):
	# 2 x num_hidden
	hidden_weights = tf.Variable(tf.truncated_normal(
			[2, num_hidden], 
			stddev=1/math.sqrt(2)
	))

	#shape [4, num_hidden]
	hidden_activations = tf.nn.relu(tf.matmul(features, hidden_weights))

	# num_hidden x 1
	output_weights = tf.Variable(tf.truncated_normal(
			[num_hidden, 1],
			stddev= 1 / math.sqrt(num_hidden)
	))
	
	# [4, 1]
	logits = tf.matmul(hidden_activations, output_weights)

	# [4]
	predications = tf.sigmoid(tf.squeeze(logits))

        # rank : 0 , scalar
	# loss = mean sauared error 
	loss = tf.reduce_mean(tf.square(predications - tf.to_float(labels)))

	global_step = tf.Variable(0, trainable=False)

	train_op = tf.train.GradientDescentOptimizer(0.2).minimize(
		loss, global_step=global_step)
	
	return train_op, loss, global_step

if __name__ == '__main__':
	graph = tf.Graph()
	num_steps = 5000
	
	with graph.as_default():
		features = tf.placeholder(tf.float32, shape=[4,2])
		labels = tf.placeholder(tf.int32, shape=[4])
		
		train_op, loss, gs = make_graph(features, labels)
		init = tf.global_variables_initializer()

	with tf.Session(graph=graph) as sess:
		init.run()
		step = 0
		xy = np.array([
			[True, False],
			[True, True],
			[False, False], 
			[False, True]
		], dtype=np.float)

		y_ = np.array([True, False, False, True], dtype=np.int32)

		while step < num_steps:
			_, step, loss_val = sess.run(
				[train_op, gs, loss], 
				feed_dict={features: xy, labels:y_}
			)
			print("step: {} loss: {}".format(step, loss_val))

		tf.logging.info('Final loss is: {}'.format(loss_val))




