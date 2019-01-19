import tensorflow as tf
z = tf.Variable(4)
with tf.Session() as session:
        print(session.run(z)) 
# 다음과 같이 실행해보면 z가 실행이 되지않습니다.
'''
FailedPreconditionError: Attempting to use uninitialized value Variable_1
	 [[{{node _retval_Variable_1_0_0}} = _Retval[T=DT_INT32, index=0, _device="/job:localhost/replica:0/task:0/device:CPU:0"](Variable_1)]]
다음과 같은 Error 메세지를 띄우는데요 Variable을 initialize해달라고 하네요.
즉 Tensorflow에서 변수를 사용하기 위해서는 초기화가 필요합니다.
이때 변수는 상수도 포함됩니다.
그렇기 때문에 global_variable_initializer 함수를 사용합니다.
이 함수를 사용하면 편하게 모든 변수들을 초기화 해주기 때문입니다.
'''
'''
x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')
z = tf.Variable(4)

a = y + z
with tf.Session() as session:
        #session.run(tf.global_variables_initializer())
        print("x = ", session.run(y))
'''
