try:
    f =open(path, "r", encoding="utf-8")
finally:
    if f:f.close()

#简单过程
with open(path, "r", encoding = "utf-8") as f:
    print(f.read())

