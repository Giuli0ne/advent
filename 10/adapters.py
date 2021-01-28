f = open("./10/data.txt", "r")

all_lines = f.read().split("\n")

adapters = [int(i) for i in all_lines]
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

ones_count = 0
threes_count = 0


for idx in range(1, len(adapters)):
    if adapters[idx] - adapters[idx-1] == 3:
        threes_count += 1
    elif adapters[idx] - adapters[idx-1] == 1:
        ones_count += 1

print(ones_count * threes_count)

def good(val, ad_set, complete_set):
    if val == max(complete_set):
        global count
        count += 1
        return
    for val_set in [v for v in ad_set[:3] if v - val <= 3 ]:
        good(val_set, ad_set[ad_set.index(val_set) +1:], complete_set)


def test_func(complete_set):
    global count
    for el in complete_set[1:]:
        s = 0
        if el - 1 in complete_set:
            s += 1
        if el - 2 in complete_set:
            s += 1
        if el - 3 in complete_set:
            s += 1
    if s == 3:
        count += 4
    if s == 2:
        count += 3

def split_adapters(complete_set):
    res = []
    temp = []
    for idx in range(len(complete_set)):
        temp.append(complete_set[idx])
        if idx + 1 == len(complete_set) or complete_set[idx + 1] - complete_set[idx] == 3:
            res.append(temp)
            temp = []
    return res

spl = split_adapters(adapters)
second_result = 1
for el in spl:
    count = 0
    good(el[0], el[1:], el)
    second_result *= count

print(second_result)




# count = 0
# test1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
# test1.append(max(test1) + 3)
# test1.append(0)
# test1.sort()
# good(test1[0], test1[1:], test1)
# print(count)

# count=0
# test2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
# test2.append(max(test2) + 3)
# test2.append(0)
# test2.sort()
# good(test2[0], test2[1:], test2)
# print(count)


# count = 0
# test3 = range(10)

# count = 1
# test_func(test1)
# print(count)

# count=1
# test_func(test2)
# print(count)
#count = 0
#good(adapters[0], adapters[1:], adapters)

