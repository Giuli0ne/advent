def toboggan (hop, down):
    f = open("./3/data.txt", "r")
    position = 0
    count = 0
    line = f.readline()
    linelength = len(line) - 1
    while(line):
        charc = line[position]
        if charc == "#":
            count += 1
        position = (position + hop) % linelength
        for i in range(down):
            line = f.readline()
    return count

# print(toboggan(1,1))
# print(toboggan(3,1))
# print(toboggan(5,1))
# print(toboggan(7,1))
# print(toboggan(2,2)) 
print(toboggan(1,1) * toboggan(3,1) * toboggan(5,1) * toboggan(7,1) * toboggan(1,2)) 
