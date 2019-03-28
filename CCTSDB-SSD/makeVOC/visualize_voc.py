'''该脚本用于对制作的voc数据集进行可视化，可以更好的观察数据集的标注结果
'''
import os
import random
import matplotlib.pyplot as plt
import  cv2 as cv
import xml.etree.ElementTree as ET

DIRECTORY_ANNOTATIONS = r"C:\Users\lxr\Desktop\CCTSDB-VOC2007\Annotations"
DIRECTORY_IMAGES = r"C:\Users\lxr\Desktop\CCTSDB-VOC2007\JPEGImages"


def plt_gboxes(img, names, boxes, figsize=(10,10), linewidth=1.5):
    plt.figure(figsize=figsize)
    plt.imshow(img)
    colors = dict()
    for i in range(len(names)):
        cls_id = i
        xmin = boxes[cls_id][0]
        ymin = boxes[cls_id][1]
        xmax = boxes[cls_id][2]
        ymax = boxes[cls_id][3]
        if cls_id not in colors:
            colors[cls_id] = (random.random(), random.random(), random.random())
        rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                             ymax - ymin, fill=False,
                             edgecolor=colors[cls_id],
                             linewidth=linewidth)
        plt.gca().add_patch(rect)
        class_name = names[cls_id]
        id = str(cls_id+1)
        plt.gca().text(xmin, ymin - 12,
                       '{:s} | {:s}'.format(id, class_name),
                       bbox=dict(facecolor=colors[cls_id], alpha=0.5),
                       fontsize=8, color='white')
    plt.show()


def show(no):

    no_ = no.zfill(6)
    xmlname = no_ + ".xml"
    imgname = no_ + ".jpg"

    # 获取img
    imgdir = os.path.join(DIRECTORY_IMAGES, imgname)
    img = cv.imread(imgdir)

    # 获取xml
    names = []
    boxes = []
    xmldir = os.path.join(DIRECTORY_ANNOTATIONS, xmlname)
    tree = ET.parse(xmldir)
    root = tree.getroot()

    # 获取obj
    for obj in root.findall('object'):
        names.append(obj.find('name').text)
        bndbox = obj.find('bndbox')
        boxes.append([int(bndbox.find('xmin').text),
                      int(bndbox.find('ymin').text),
                      int(bndbox.find('xmax').text),
                      int(bndbox.find('ymax').text),
                      ])
    # 渲染
    plt_gboxes(img, names, boxes)


def main():
    while(True):
        no = input("请输入您要检查的图片：")
        show(no)

if __name__ == "__main__":
    main()