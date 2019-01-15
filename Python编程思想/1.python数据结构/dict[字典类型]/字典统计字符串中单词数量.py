str = "a a a a b b b b c c c c"
l = str.split(" ")
d = {}
for word in l:
    c = d.get(word)
    if c == None:
        d[word] = 1
    else:
        d[word] += 1
print(d)
