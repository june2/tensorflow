
from operator import eq
from tensorflow.contrib import learn

import numpy as np
import tensorflow as tf
import data_parser as dp
import json

# read file
text_file = open("IT.txt", "r")
arr = text_file.readlines()
text_file.close()

# originString = "기술 안드로이드 mac \n 기술 안드로이드 mac"

stringParser = dp.StringParser()

stringParser.isDebug = False

stringParser.setString(arr)

x_text = stringParser.getXData()
category, y_data = stringParser.getYData()

nb_classes = len(category)

thefile = open('model/category.txt', 'w')
for item in category:
    thefile.write("%s\n" % item)

print(x_text)
print(category)
print(y_data)



#########
# make vocaburary dic
######
max_document_length = max([len(x.split(" ")) for x in x_text])

# ## Create the vocabularyprocessor object, setting the max lengh of the documents.
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)

# ## Transform the documents using the vocabulary.
x_data = np.array(list(vocab_processor.fit_transform(x_text)))  

# ## Extract word:id mapping from the object.
vocab_dict = vocab_processor.vocabulary_._mapping

# ## save vocab
vocab_processor.save("model/vocab")

print(x_data)
print(y_data)




# nb_classes = 3  # 경우 수

X = tf.placeholder(tf.float32, [None, max_document_length], name='X')
Y = tf.placeholder(tf.int32, [None, 1], name='Y')  # 0 ~ 6

Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot
print("one_hot", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
print("reshape", Y_one_hot)

W = tf.Variable(tf.random_normal([max_document_length, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits,
                                                 labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


#########
# 신경망 모델 학습
######
sess = tf.Session()
# 모델을 저장하고 불러오는 API를 초기화합니다.
# global_variables 함수를 통해 앞서 정의하였던 변수들을 저장하거나 불러올 변수들로 설정합니다.
saver = tf.train.Saver(tf.global_variables())

ckpt = tf.train.get_checkpoint_state('./model')
if ckpt and tf.train.checkpoint_exists(ckpt.model_checkpoint_path):
    saver.restore(sess, ckpt.model_checkpoint_path)
else:
    sess.run(tf.global_variables_initializer())

    
# 최적화 진행
for step in range(2000):
    sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
    if step % 100 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={X: x_data, Y: y_data})
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc))

        

# 최적화가 끝난 뒤, 변수를 저장합니다.
saver.save(sess, './model/output.ckpt', global_step=1000)



#########
# evaluate
######
print(hypothesis)

sorted_vocab = sorted(vocab_dict.items(), key=lambda x: x[1])
vocabulary = list(list(zip(*sorted_vocab))[0])
# print(sorted_vocab);
# print(vocabulary);


input_data = []
input_text = input('사용자 평가를 문장으로 입력하세요: ').split()
for data in input_text:        
    if(data in vocabulary):
        index = vocabulary.index(data) #index 체크
        input_data.append(index) #데이터 입력

#  array size 조절   
size = max_document_length - len(input_data)

for i in range(0,size):
    input_data.append(0)
    

# 평가
prob = sess.run(hypothesis, feed_dict={X: [input_data]})
pred = sess.run(prediction, feed_dict={X: [input_data]})

print(input_data)
print('probability', prob)
print("Prediction: {}".format(pred), category[int(pred)])
