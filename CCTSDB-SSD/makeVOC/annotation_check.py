
import cv2 as cv
import os

path = r"D:\CCTSDB\GroundTruth"
img_path = r"D:\CCTSDB-VOC2007\JPEGImages"


def main():
    check = []
    file = open(os.path.join(path, "GroundTruth.txt"), 'r')
    line = file.readline()
    while line:
        temp = line.rstrip("\n").split(";")
        img_name = "0"+temp[0].split(".")[0]+".jpg"
        img = cv.imread(os.path.join(img_path, img_name))
        if img is not None:
            width = float(img.shape[1])
            height = float(img.shape[0])
            xmin = float(temp[1])
            ymin = float(temp[2])
            xmax = float(temp[3])
            ymax = float(temp[4])
            if 0 <= xmin < xmax <= width and 0 <= ymin < ymax <= height:
                print(">>>" + img_name + ":检查完毕!")
            else:
                check.append(img_name)
                print(img_name+":错误标注,存在越界!")
        else:
            print("检查结束！")
            print("- - - - - - - - - - - - - - python - - - - - - - - - - - - - - - ")
            print(check)
            break
        line = file.readline()
    file.close()


if __name__ == "__main__":
    main()