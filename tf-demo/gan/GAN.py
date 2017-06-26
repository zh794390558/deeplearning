# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:45:18 2017

@author: Administrator
"""

# E:\python\MNIST_data
import tensorflow as tf
import numpy as np
import datetime
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('E:\python\MNIST_data')


def discriminator(images, reuse_variables=None):
    with tf.variable_scope(tf.get_variable_scope(), reuse=reuse_variables) as scope:
        d_w1 = tf.get_variable('d_w1', [5,5,1,32], initializer=tf.truncated_normal_initializer(stddev=0.02))
        d_b1 = tf.get_variable('d_b1', [32], initializer=tf.constant_initializer(0))
        d1 = tf.nn.conv2d(input=images, filter=d_w1, strides=[1,1,1,1], padding='SAME')
        d1 = d1 + d_b1
        d1 = tf.nn.relu(d1)
        d1 = tf.nn.avg_pool(d1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        
        d_w2 = tf.get_variable('d_w2', [5,5,32,64], initializer=tf.truncated_normal_initializer(stddev=0.02))
        d_b2 = tf.get_variable('d_b2', [64], initializer=tf.constant_initializer(0))
        d2 = tf.nn.conv2d(input=d1, filter=d_w2, strides=[1,1,1,1], padding='SAME')
        d2 = d2 + d_b2
        d2 = tf.nn.relu(d2)
        d2 = tf.nn.avg_pool(d2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        
        d_w3 = tf.get_variable('d_w3', [7*7*64, 1024], initializer=tf.truncated_normal_initializer(stddev=0.02))
        d_b3 = tf.get_variable('d_b3', [1024], initializer=tf.constant_initializer(0))
        d3 = tf.reshape(d2, [-1, 7*7*64])
        d3 = tf.matmul(d3, d_w3)
        d3 = d3 + d_b3
        d3 = tf.nn.relu(d3)
        
        d_w4 = tf.get_variable('d_w4', [1024, 1], initializer=tf.truncated_normal_initializer(stddev=0.02))
        d_b4 = tf.get_variable('d_b4', [1], initializer=tf.constant_initializer(0))
        d4 = tf.matmul(d3, d_w4) + d_b4
        
        return d4
        
def generator(z, batch_size, z_dim):
    g_w1 = tf.get_variable('g_w1', [z_dim, 3136], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.02))
    g_b1 = tf.get_variable('g_b1', [3136], initializer=tf.truncated_normal_initializer(stddev=0.02))
    g1 = tf.matmul(z, g_w1) + g_b1
    g1 = tf.reshape(g1, [-1, 56, 56, 1])
    g1 = tf.contrib.layers.batch_norm(g1, epsilon=1e-5, scope='bn1')
    g1 = tf.nn.relu(g1)
    
    g_w2 = tf.get_variable('g_w2', [3,3, 1, z_dim/2], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.02))
    g_b2 = tf.get_variable('g_b2', [z_dim/2], initializer=tf.truncated_normal_initializer(stddev=0.02))
    g2 = tf.nn.conv2d(g1, g_w2, strides=[1,2,2,1], padding='SAME')
    g2 = g2 + g_b2
    g2 = tf.contrib.layers.batch_norm(g2, epsilon=1e-5, scope='bn2')
    g2 = tf.nn.relu(g2)
    g2 = tf.image.resize_images(g2, [56, 56])
    
    g_w3 = tf.get_variable('g_w3', [3,3,z_dim/2, z_dim/4], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.02))
    g_b3 = tf.get_variable('g_b3', [z_dim/4], initializer=tf.truncated_normal_initializer(stddev=0.02))
    g3 = tf.nn.conv2d(g2, g_w3, strides=[1,2,2,1], padding='SAME')
    g3 = g3 + g_b3
    g3 = tf.contrib.layers.batch_norm(g3, epsilon=1e-5, scope='bn3')
    g3 = tf.nn.relu(g3)
    g3 = tf.image.resize_images(g3, [56, 56])
    
    g_w4 = tf.get_variable('g_w4', [1,1,z_dim/4, 1], dtype=tf.float32, initializer=tf.truncated_normal_initializer(stddev=0.02))
    g_b4 = tf.get_variable('g_b4', [1], initializer=tf.truncated_normal_initializer(stddev=0.02))
    g4 = tf.nn.conv2d(g3, g_w4, strides=[1,2,2,1], padding='SAME')
    g4 = g4 + g_b4
    g4 = tf.sigmoid(g4)
    
    return g4
    
    
if __name__ == '__main__':    
    tf.reset_default_graph()
    print(tf.get_variable_scope().name)
    
    batch_size = 50
    z_dimensions = 100
    
    z_placeholder = tf.placeholder(tf.float32, [None, z_dimensions], name='z_placeholder')
    x_placeholder = tf.placeholder(tf.float32, [None, 28, 28, 1], name='x_placeholder')
    
    Gz = generator(z_placeholder, batch_size, z_dimensions)

    Dx = discriminator(x_placeholder)

    Dg = discriminator(Gz, reuse_variables=True)    
    
    d_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dx, targets =tf.ones_like(Dx)))
    d_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dg, targets =tf.zeros_like(Dg)))
    g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dg, targets =tf.ones_like(Dg)))

    tvars = tf.trainable_variables()
    d_vars = [var for var in tvars if 'd_' in var.name]
    g_vars = [var for var in tvars if 'g_' in var.name]
    print([v.name for v in d_vars])
    print([v.name for v in g_vars])
    
    
    d_trainer_fake  = tf.train.AdamOptimizer(0.0003).minimize(d_loss_fake, var_list=d_vars)
    d_trainner_real = tf.train.AdamOptimizer(0.0003).minimize(d_loss_real, var_list=d_vars)
    g_trainer = tf.train.AdamOptimizer(0.0001).minimize(g_loss, var_list=g_vars)



    tf.get_variable_scope().reuse_variables()
    tf.summary.scalar('Generator_loss', g_loss)
    tf.summary.scalar('Discriminator_loss_real', d_loss_real)
    tf.summary.scalar('Discriminator_loss_fake', d_loss_fake)
    images_for_tensorboard = generator(z_placeholder, batch_size, z_dimensions)
    tf.summary.image('Generated_images', images_for_tensorboard)
    merged = tf.summary.merge_all()
    logdir = 'tensorborad/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '/'
    
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter(logdir, sess.graph)
        
        for i in range(300):
            z_batch = np.random.normal(0, 1, [batch_size, z_dimensions])
            real_image_batch = mnist.train.next_batch(batch_size)[0].reshape([batch_size, 28,28,1])
            
            _,_, dLossReal, dLossFake = sess.run([d_trainner_real, d_trainer_fake, d_loss_real, d_loss_fake], {x_placeholder:real_image_batch, z_placeholder: z_batch})
            
            if i % 100 == 0:
                print('dLossReal:', dLossReal, 'dLossFake:', dLossFake)
        
        
        for i in range(100000):
            real_image_batch = mnist.train.next_batch(batch_size)[0].reshape([batch_size, 28, 28, 1])
            z_batch = np.random.normal(0, 1, [batch_size, z_dimensions])
            
            _, _, dLossReal, dLossFake = sess.run([d_trainner_real, d_trainer_fake, d_loss_real, d_loss_fake], {x_placeholder: real_image_batch, z_placeholder: z_batch})
            
            z_batch = np.random.normal(0,1,size=[batch_size, z_dimensions])
            _ = sess.run(g_trainer, feed_dict={z_placeholder: z_batch})
             
             
            if i % 10 == 0:
                # Update TensorBoard with summary statistics
                z_batch = np.random.normal(0, 1, size=[batch_size, z_dimensions])
                summary = sess.run(merged, {z_placeholder: z_batch, x_placeholder: real_image_batch})
                writer.add_summary(summary, i)
                
            if i % 100 == 0:
                # Every 100 iterations, show a generated image
                print("Iteration:", i, "at", datetime.datetime.now())
                z_batch = np.random.normal(0, 1, size=[1, z_dimensions])
                generated_images = generator(z_placeholder, 1, z_dimensions)
                images = sess.run(generated_images, {z_placeholder: z_batch})
                plt.imshow(images[0].reshape([28, 28]), cmap='Greys')
                plt.show()
        
                # Show discriminator's estimate
                im = images[0].reshape([1, 28, 28, 1])
                result = discriminator(x_placeholder)
                estimate = sess.run(result, {x_placeholder: im})
                print("Estimate:", estimate)