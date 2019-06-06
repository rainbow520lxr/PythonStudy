# -*- coding：utf-8 -*-
# -*- author：zzZ_CMing  CSDN address:https://blog.csdn.net/zzZ_CMing
# -*- 2018/07/18; 15:19
# -*- python3.5
import os
import random

trainval_percent = 0.7
train_percent = 0.8
xmlfilepath = r'D:\CCTSDB-VOC2007\Annotations'           #写自己的路径
txtsavepath = r'D:\CCTSDB-VOC2007\ImageSets\Main'        #写自己路径
total_xml = os.listdir(xmlfilepath)

def main():
    num = len(total_xml)
    list = range(num)
    tv = int(num*trainval_percent)
    tr = int(tv*train_percent)
    trainval = random.sample(list,tv)
    train = random.sample(trainval,tr)

    ftrainval = open(txtsavepath+'/trainval.txt', 'w')
    ftest = open(txtsavepath+'/test.txt', 'w')
    ftrain = open(txtsavepath+'/train.txt', 'w')
    fval = open(txtsavepath+'/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4]+'\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest .close()
    print('Well Done！！！')

if __name__ == "__main__":
    main()