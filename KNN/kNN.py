#coding=utf-8
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

filename = '../KNN/datafiles/datingTestSet2.txt'

# TXT格式的数据转化为矩阵
def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector  = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

returnMat,classLabelVector = file2matrix(filename)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(returnMat[:, 0],returnMat[:, 1], 15.0*np.array(classLabelVector),15.0*np.array(classLabelVector))
plt.show()