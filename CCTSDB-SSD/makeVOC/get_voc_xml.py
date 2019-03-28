'''该脚本根据长沙理工大学制作的数据集CCTSRD转换为VOC2007格式的XML文件
'''
import os
from xml.dom.minidom import Document
import cv2 as cv

DIRECTORY_ANNOTATIONS = "Annotations/"
DIRECTORY_IMAGES = "JPEGImages/"

path = r"C:\Users\lxr\Desktop\CCTSDB\GroundTruth"
vocpath = r"C:\Users\lxr\Desktop\CCTSDB-VOC2007"

#获取GroundTruth/中的所有grouthtrue
def get_filenames(fileMap):
    file = open(os.path.join(path,'GroundTruth.txt'), 'r')
    line = file.readline()
    while line:
        res = line.rstrip("\n").split(";")
        num = int(res[0].split(".")[0])
        name = "0"+res[0].split(".")[0]+".jpg"
        if(len(fileMap) == num):
            fileMap[name] = []
            fileMap[name].append(res[1:])
        else:
            fileMap[name].append(res[1:])
        if (len(fileMap) < 1000):line = file.readline()
        else:
            line = file.readline()
            res = line.rstrip("\n").split(";")
            num = int(res[0].split(".")[0])
            print("num: %d" % num)
            if (len(fileMap)-1 == num):
                continue
            else: break

    file.close()

#向VOC数据集中写入xml文件
def writeInfoToXml(fileMap, imgname, imgsize):
    xml = Document()   #创建dom文档

    root = xml.createElement("annotation")  #创建根节点
    xml.appendChild(root)                   #根节点插入dom树

    folder = xml.createElement("folder")
    folder_text = xml.createTextNode("CCTSDB-VOC2007")
    folder.appendChild(folder_text)
    root.appendChild(folder)

    filename = xml.createElement("filename")
    filename_text = xml.createTextNode(imgname)
    filename.appendChild(filename_text)
    root.appendChild(filename)

    size = xml.createElement("size")
    width = xml.createElement("width")
    width_text = xml.createTextNode(str(imgsize[1]))
    width.appendChild(width_text)
    height = xml.createElement("height")
    height_text = xml.createTextNode(str(imgsize[0]))
    height.appendChild(height_text)
    depth = xml.createElement("depth")
    depth_text = xml.createTextNode(str(imgsize[2]))
    depth.appendChild(depth_text)
    size.appendChild(width)
    size.appendChild(height)
    size.appendChild(depth)
    root.appendChild(size)

    for obj in fileMap[imgname]:
        object = xml.createElement("object")

        name = xml.createElement("name")
        name_text = xml.createTextNode(obj[4])
        name.appendChild(name_text)

        bndbox = xml.createElement("bndbox")
        xmin = xml.createElement("xmin")
        xmin_text = xml.createTextNode(str(obj[0]))
        xmin.appendChild(xmin_text)
        ymin = xml.createElement("ymin")
        ymin_text = xml.createTextNode(str(obj[1]))
        ymin.appendChild(ymin_text)
        xmax = xml.createElement("xmax")
        xmax_text = xml.createTextNode(str(obj[2]))
        xmax.appendChild(xmax_text)
        ymax = xml.createElement("ymax")
        ymax_text = xml.createTextNode(str(obj[3]))
        ymax.appendChild(ymax_text)
        bndbox.appendChild(xmin)
        bndbox.appendChild(ymin)
        bndbox.appendChild(xmax)
        bndbox.appendChild(ymax)

        object.appendChild(name)
        object.appendChild(bndbox)
        root.appendChild(object)

    xmldir = os.path.join(vocpath, DIRECTORY_ANNOTATIONS)
    xmlname = imgname.split(".")[0]+".xml"
    with open(os.path.join(xmldir, xmlname), 'w') as f:   # 将dom对象写入本地xml文件
        xml.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')

def main():
    fileMap = {}
    print("正在存取中到 fileList中>>>")
    get_filenames(fileMap)
    imgdir = os.path.join(vocpath, DIRECTORY_IMAGES)
    imgnames = sorted(os.listdir(imgdir))
    print("成功存入！")
    print("正在生成xml中>>>")
    for imgname in imgnames:
        img = cv.imread(os.path.join(imgdir, imgname))
        imgsize = img.shape
        writeInfoToXml(fileMap, imgname, imgsize)
    print("成功写入!")

    # for k in fileMap:
    #     print(k + ":\n")
    #     print(fileMap[k])

if __name__ == "__main__":
    main()



