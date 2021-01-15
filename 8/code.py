f = open("./8/data.txt", "r")

all_instructions = f.read().split("\n")

instruction_set = [[el.split(" ")[0], el.split(" ")[1]] for el in all_instructions]

def execute(st_p):
    if instruction_set[st_p][0] == "jmp":
        return (st_p + int(instruction_set[st_p][1]), 0)
    elif instruction_set[st_p][0] == "nop":
        return (st_p +1, 0)
    else:
        return (st_p +1, int(instruction_set[st_p][1]))

def execute_program(instructions):
    executed = []
    accum = 0
    stack_pointer = 0
    while(True):
        temp_pointer, temp_accum = execute(stack_pointer)
        executed.append(stack_pointer)
        accum += temp_accum
        if temp_pointer in executed or temp_pointer<0:
            return (1, accum)
        elif temp_pointer == len(instructions):
            return (0, accum)
        else:
            stack_pointer = temp_pointer

for index in range(len(instruction_set)):
    if instruction_set[index][0] == "acc":
        continue

    backup_instruction = instruction_set[index][0]
    if instruction_set[index][0] == "jmp":
        instruction_set[index][0] = "nop"
    else:
        instruction_set[index][0] = "jmp"
    
    result = execute_program(instruction_set)
    if(result[0] == 0):
        print(index, result[1])
        break
    else:
        instruction_set[index][0] = backup_instruction

    
