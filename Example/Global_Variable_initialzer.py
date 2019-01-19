import tensorflow as tf
z = tf.Variable(4)
with tf.Session() as session:
        print(session.run(z)) 

'''
x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')
z = tf.Variable(4)

a = y + z
with tf.Session() as session:
        #session.run(tf.global_variables_initializer())
        print("x = ", session.run(y))
'''