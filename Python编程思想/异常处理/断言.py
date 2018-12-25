
'''

方便寻找错误，基本用不着断言，可以谢了后在IDE关闭

'''

def fun(num, div):

    sssert(div != 0) ,"div不能为0"
    return num/div


print (fun(10, 0))