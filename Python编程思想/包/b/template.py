#定义一个模块


def sayGood():
    print("lxr is a good man")
def sayNice():
    print("lxr is a nice man")
def sayHandsome():
    print("lxr is a sayHandsome man")



TT = 100

# if __name__ == "__main__":
#     print("我是主程序")
# else:
#     print("我是一个模块")


def main():
    print("我也执行了！")

if __name__ == "__main__":
    main()
else:
    print("我是模板，主程序已经内置，该模板的主程序不会执行")

