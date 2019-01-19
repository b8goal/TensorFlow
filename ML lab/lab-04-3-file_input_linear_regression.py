import tensorflow as tf
import numpy as np
tf.set_random_seed(777) # for reproducibility

xy = np.loadtxt('data-01-test-score.csv', delimiter=',',dtype=np.float32)
x_data = xy[:, 0:-1] # 0 to the (last element -1)
y_data = xy[:, [-1]] # y data is only one so [-1]

# Make sure the shape and data are OK
print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)

# placeholders for a tensor that will be always fed
X = tf.placeholder(tf.float32, shape=[None, 3]) # number of x's data is 3
Y = tf.placeholder(tf.float32, shape=[None, 1]) # number of y's data is 1

W = tf.Variable(tf.random_normal([3,1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

# Hypothesis
hypothesis = tf.matmul(X, W) + b

# Simplified cost / Loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate= 1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())
# Set up feed_dict variables inside the Loop
for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
        
# Ask my score
print("Your score will be ", sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
print("Other score will be ", sess.run(hypothesis, feed_dict={X: [[60, 70, 110],[90, 100, 80]]}))
