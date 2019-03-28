import re
def checkPhone(str):
    #18215527557
    pat = r"^1[3578]\d{9}$"
    res = re.match(pat, str)
    print(res)

print(checkPhone(18215527557))
print(checkPhone(12215527557))
print(checkPhone(13215527557))

