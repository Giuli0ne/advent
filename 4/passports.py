f = open("./4/data.txt", "r")

data = f.read().split("\n\n")


count = 0
missing = []
for el in data:
    passport = el.split()
    if len(passport) == 8:
        count += 1
    else:
        missing.append(passport)

for passport in missing:
    if len(passport) == 7:
        condition = False
        for code in passport:
            condition = condition or (code[:3] == "cid")
        if not condition:
            count += 1

print(count)

count = len(data)
print("length ", count)
for el in data:
    passport = el.split()
    passportDictionary = {el.split(":")[0]: el.split(":")[1] for el in passport}
    if "byr" not in passportDictionary or int(passportDictionary["byr"]) < 1920 or int(passportDictionary["byr"]) > 2002:
        count -= 1
        continue
    if "iyr" not in passportDictionary or int(passportDictionary["iyr"]) < 2010 or int(passportDictionary["iyr"]) > 2020:
        count -= 1
        continue
    if "eyr" not in passportDictionary or int(passportDictionary["eyr"]) < 2020 or int(passportDictionary["eyr"]) > 2030:
        count -= 1
        continue

    if "hgt" not in passportDictionary:
        count -= 1
        continue
    else:
        if passportDictionary["hgt"][-2:] != "in" and passportDictionary["hgt"][-2:] != "cm":
            count -= 1
            continue
        else:
            if passportDictionary["hgt"][-2:] == "in" and (int(passportDictionary["hgt"][:-2]) < 59 or int(passportDictionary["hgt"][:-2]) >76):
                count -=1
                continue
            elif passportDictionary["hgt"][-2:] == "cm" and (int(passportDictionary["hgt"][:-2]) < 150 or int(passportDictionary["hgt"][:-2]) > 193):
                count -=1
                continue
    
    if "hcl" not in passportDictionary:
        count -= 1
        continue
    else:
        if passportDictionary["hcl"][0] != "#" or len(passportDictionary["hcl"]) != 7:
            count -= 1
            continue
        else:
            found = False
            for ch in passportDictionary["hcl"][1:]:
                if ch not in ['a','b','c','d','e','f'] and int(ch) not in range(10):
                    found = True
                    break
            if found:
                count -= 1
                continue
    
    if "ecl" not in passportDictionary or passportDictionary["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        count -= 1
        continue
    

    if "pid" not in passportDictionary or len(passportDictionary["pid"]) != 9:
        count -= 1
        continue

    #print("good")

print(count)
