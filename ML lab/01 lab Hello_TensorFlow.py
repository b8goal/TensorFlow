import tensorflow as tf
Hello = tf.constant('Hello Tensorflow!')
sess = tf.Session()
sess.run(Hello)