max1_elf = 0
max2_elf = 0
max3_elf = 0
one_elf = 0
max_list: list = []

with open("input1","r") as file:
    for line in file:
        act = line.strip()
        if act == '':
            max_list.append(one_elf)
            one_elf = 0
        else:
            one_elf += int(act)
        
    max1_elf = max(max_list)
    max_list.remove(max1_elf)
    max2_elf = max(max_list)
    max_list.remove(max2_elf)
    max3_elf = max(max_list)
    max_list.remove(max3_elf)
    top3 = max1_elf + max2_elf + max3_elf
    print(str(top3))
