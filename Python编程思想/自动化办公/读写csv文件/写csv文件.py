import csv

def writeCsv(path, data):
    with open(path,"w", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            print("row =", row)
            writer.writerow(row)

data = [[1,2,3],[1,2,3],[1,2,3] ]
path = "writer.csv"

writeCsv(path,data)
