import csv

def  readCsv(path):
    infoList = []
    with open(path, "r", encoding="utf-8") as f:
        fileInfo = csv.reader(f)
        print(fileInfo)
        for row in fileInfo:
            infoList.append(row)
    return infoList
path = "demo.csv"
info = readCsv(path)
for item in info:
    print(item)