# -*- coding: utf-8 -*-
"""Naive Bayes Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18v81S-h1yN0ZdVKkcy9hH5RaZbnJ39jU

# Naive Bayes Classification
"""

# Commented out IPython magic to ensure Python compatibility.
#importing libraries
import numpy as np
from matplotlib import pyplot as plt

# %matplotlib inline

#Loading Training Data
train_X = np.loadtxt('/content/drive/MyDrive/AI/trainX.txt')
train_Y = np.loadtxt('/content/drive/MyDrive/AI/trainY.txt')

#Loading Testing Data
test_X = np.loadtxt('/content/drive/MyDrive/AI/testX.txt')
test_Y = np.loadtxt('/content/drive/MyDrive/AI/testY.txt')

"""## Displaying Training Data"""

# 2
img2=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,
0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,
0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0],dtype=np.uint8)

print(img2.shape)

img_2 = np.reshape(img2,(16,16),order='F')

print(img_2.shape)

plt.imshow(img_2)

# 4
img4=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,
0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,
1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,
0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0],dtype=np.uint8)

print(img4.shape)

img_4 = np.reshape(img4,(16,16),order='F')

print(img_4.shape)

plt.imshow(img_4)

"""## Training Data"""

#Divinding Training Data
train_Divider = int(((len(train_X)/2)))

train_2 = train_X[:train_Divider, :]
train_4 = train_X[train_Divider:, :]

#Computing Probabilities of 2 and 4

#Probability of 2
prob_T_2 = ((train_2.sum(axis = 0) + 1)/(train_2.shape[0] + 2))
prob_F_2 = 1 - prob_T_2

#Probability of 4
prob_T_4 = ((train_4.sum(axis = 0) + 1)/(train_4.shape[0] + 2))
prob_F_4 = 1 - prob_T_4

#Probability of Training Data
train_2_prob = []
train_4_prob = []

for m in train_X:
  train_p_2 = 1
  train_p_4 = 1
  length = len(m)
  for i in range(length):
    if m[i] == 1:
      train_p_2 = train_p_2 * prob_T_2[i]
      train_p_4 = train_p_4 * prob_T_4[i]
    elif m[i] == 0:
      train_p_2 = train_p_2 * prob_F_2[i]
      train_p_4 = train_p_4 * prob_F_4[i]

  train_2_prob.append(train_p_2)
  train_4_prob.append(train_p_4)

#Finding Values in Training Data
train_Value = []
len_X = len(train_X)
for i in range(len_X):
  Maximum = max(train_2_prob[i], train_4_prob[i])

  if Maximum == train_2_prob[i]:
    train_Value.append(2)
  elif Maximum == train_4_prob[i]:
    train_Value.append(4)

#Training Data Predictions
train_2_prediction = 0
train_4_prediction = 0

for i in range(len(train_Value)):
  if train_Value[i] == 2 and train_Y[i] == 2:
    train_2_prediction = train_2_prediction + 1
  elif train_Value[i] == 4 and train_Y[i] == 4:
    train_4_prediction = train_4_prediction + 1

#Checking Accuracy of Training Data
train_2_total = 0
train_4_total = 0

for i in range(len(train_Y)):
  if train_Y[i] == 2:
    train_2_total = train_2_total + 1
  elif train_Y[i] == 4:
    train_4_total = train_4_total + 1

train_2_accuracy = train_2_prediction/train_2_total
train_4_accuracy = train_4_prediction/train_4_total

print('Training Accuracy of 2: ', train_2_accuracy)
print('Training Accuracy of 4: ', train_4_accuracy)

#Checking overall accuracy of Training Data
#2 is Positive and 4 in Negative
train_TP = 0
train_FP = 0
train_TN = 0
train_FN = 0

for i in range(len(train_Y)):
  if train_Value[i] == 2 and train_Y[i] == 2:
    train_TP = train_TP + 1
  elif train_Value[i] == 2 and train_Y[i] == 4:
    train_FP = train_FP + 1
  elif train_Value[i] == 4 and train_Y[i] == 4:
    train_TN = train_TN + 1
  elif train_Value[i] == 4 and train_Y[i] == 2:
    train_FN = train_FN + 1

train_Accuracy = (train_TP + train_TN) / (train_TP + train_FP + train_TN + train_FN)

print('trainTP: ', train_TP)
print('trainTN: ', train_TN)
print('trainFP: ', train_FP)
print('trainFN: ', train_FN)
print('Total Training Accuracy: ', train_Accuracy)

"""## Testing Data"""

#Probability of Testing Data
test_2_prob = []
test_4_prob = []

for m in test_X:
  test_p_2 = 1
  test_p_4 = 1
  length = len(m)
  for i in range(length):
    if m[i] == 1:
      test_p_2 = test_p_2 * prob_T_2[i]
      test_p_4 = test_p_4 * prob_T_4[i]
    elif m[i] == 0:
      test_p_2 = test_p_2 * prob_F_2[i]
      test_p_4 = test_p_4 * prob_F_4[i]

  test_2_prob.append(test_p_2)
  test_4_prob.append(test_p_4)

#Finding Values in Testing Data
test_Value = []
len_X = len(test_X)
for i in range(len_X):
  Maximum = max(test_2_prob[i], test_4_prob[i])

  if Maximum == test_2_prob[i]:
    test_Value.append(2)
  elif Maximum == test_4_prob[i]:
    test_Value.append(4)

#Testing Data Predictions
test_2_prediction = 0
test_4_prediction = 0

for i in range(len(test_Value)):
  if test_Value[i] == 2 and test_Y[i] == 2:
    test_2_prediction = test_2_prediction + 1
  elif test_Value[i] == 4 and test_Y[i] == 4:
    test_4_prediction = test_4_prediction + 1

#Checking Accuracy
test_2_total = 0
test_4_total = 0

for i in range(len(test_Y)):
  if test_Y[i] == 2:
    test_2_total = test_2_total + 1
  elif test_Y[i] == 4:
    test_4_total = test_4_total + 1

test_2_accuracy = test_2_prediction/test_2_total
test_4_accuracy = test_4_prediction/test_4_total

print('Testing Accuracy of 2: ', test_2_accuracy)
print('Testing Accuracy of 4: ', test_4_accuracy)

#Checking overall accuracy of Testing Data
#2 is Positive and 4 in Negative
test_TP = 0
test_FP = 0
test_TN = 0
test_FN = 0

for i in range(len(test_Y)):
  if test_Value[i] == 2 and test_Y[i] == 2:
    test_TP = test_TP + 1
  elif test_Value[i] == 2 and test_Y[i] == 4:
    test_FP = test_FP + 1
  elif test_Value[i] == 4 and test_Y[i] == 4:
    test_TN = test_TN + 1
  elif test_Value[i] == 4 and test_Y[i] == 2:
    test_FN = test_FN + 1

test_Accuracy = (test_TP + test_TN) / (test_TP + test_FP + test_TN + test_FN)

print('testTP: ', test_TP)
print('testTN: ', test_TN)
print('testFP: ', test_FP)
print('testFN: ', test_FN)
print('Total Testing Accuracy: ', test_Accuracy)