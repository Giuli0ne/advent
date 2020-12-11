f = open("./5/data.txt", "r")

data = f.read().split("\n")

maxid = 0
for d in data:
    binary = d.replace("F","0").replace("B","1").replace("L","0").replace("R","1")
    row = int(binary[:-3],2)
    column = int(binary[-3:],2)
    id = row * 8 + column
    if id > maxid:
        maxid = id

print(maxid)

idlist = list(range(128 * 8))
for d in data:
    binary = d.replace("F","0").replace("B","1").replace("L","0").replace("R","1")
    row = int(binary[:-3],2)
    column = int(binary[-3:],2)
    id = row * 8 + column
    idlist.remove(id)

#print(idlist)
for id in idlist:
    if id + 1 not in idlist and id - 1 not in idlist:
        print(id)