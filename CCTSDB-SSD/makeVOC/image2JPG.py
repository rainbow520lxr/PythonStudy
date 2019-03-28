import os
import cv2 as cv


in_path = r"C:\Users\lxr\Desktop\CCTSDB\Images"
out_path = r"C:\Users\lxr\Desktop\CCTSDB-VOC2007\JPEGImages"
# print(path)

def main():
    for dir in os.listdir(in_path):
        dir_ = os.path.join(in_path, dir)
        for filename in os.listdir(dir_):
            if os.path.splitext(filename)[1] == '.png':
                # print(filename)
                img = cv.imread(os.path.join(dir_, filename))
                # print(filename.replace(".png", ".jpg"))
                newfilename = "0"+filename.replace(".png", ".jpg")
                # cv2.imshow("Image",img)
                # cv2.waitKey(0)
                cv.imwrite(os.path.join(out_path, newfilename), img)

if __name__ == "__main__":
    main()
    print("成功执行！")
