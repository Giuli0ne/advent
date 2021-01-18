f = open("./9/data.txt", "r")

all_lines = f.read().split("\n")

preamble_length = 25

numbers = []
for line in all_lines:
    numbers.append(int(line))

def good(first_set, number):
    for el in first_set:
        if number - el in first_set and number - el != el:
            return True
    return False
    

def first_part():
    for count in range(len(numbers) - preamble_length):
        selected_set = numbers[count:count + preamble_length]
        selected_number = numbers[count + preamble_length]
        if not good(selected_set, selected_number):
            return selected_number

print(first_part())

fp = first_part()
idx = numbers.index(fp)

def second_part():
    for count1 in range(idx):
        for count2 in range(count1, idx):
            if sum(numbers[count1:count2]) == fp:
                print(max(numbers[count1:count2]) + min(numbers[count1:count2]))
second_part()