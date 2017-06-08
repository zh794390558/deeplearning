import numpy as np

import tensorflow as tf

m1 =np.array([[1., 2.], [3., 4.], [5., 6.], [7., 8.]], dtype=np.float32)


# 4x2
m1_input = tf.placeholder(tf.float32, shape=[4,2])
# 2x3
m2 = tf.Variable(tf.random_uniform([2,3], -1.0 , 1.0))
# 4x3
m3 = tf.matmul(m1_input, m2)

#this is an identity op with the side effect of printing data when evaluating
m3 = tf.Print(m3, [m3], message="m3 is: ")

init = tf.global_variables_initializer()


with tf.Session() as sess:
	init.run()
	print("initailized")

	print("m2: {}".format(m2))
	print("eval m2: {}".format(m2.eval()))

	feed_dict = {m1_input: m1}

	result = sess.run([m3], feed_dict=feed_dict)
	print("\nresult: {}\n".format(result))
