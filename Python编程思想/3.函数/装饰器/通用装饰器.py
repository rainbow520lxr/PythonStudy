def outer(fun):
    def inner(*args, **kwargs):

        #添加修改的功能
        print("&&&&&&&&&&&&&&&&&&&&")

        fun(*args, **kwargs)
    return

@outer
def say(name, age):
    print("my name is %s, my age is %d" % (name, age))