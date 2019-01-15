#true/false startwith("ni", start=0, end=len(str)
#判断在start与end范围内是否以"ni"开始的

#true/false endwith("ni", start=0, end=len(str)
#判断在start与end范围内是否以"ni"开始的

#编码
#encode(encoding="utf-8", erors="strict")
str = "sunck is a good man凯"
data = str.encode("utf-8")

#解码 注意：要与编码时的编码格式一致
str1 = data.decode("utf-8")

print(str1)