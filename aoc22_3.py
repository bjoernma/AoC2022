compart_a_list: dict = {}
compart_b_list: dict = {}
overlap_list: list = []
prio:int = 0

with open("input3","r") as file:
    for line in file:
        line = line.strip()
        length_line = int(len(line)) // 2
        compart_a = line[:length_line]
        compart_b = line[length_line:]
        print(compart_a + ' ' + compart_b)
        for letter in compart_a:
            compart_a_list[letter] = compart_a_list.get(letter,0) + 1
        for letter in compart_b:
            compart_b_list[letter] = compart_b_list.get(letter,0) + 1
        print(compart_a_list)
        for entry in compart_a_list:
            print(entry)
            try:
                if compart_b_list[entry] != None:
                    overlap_list.append(entry)
            except:
                print(entry + ' not found in compart_b_list.')
        del compart_a_list
        compart_a_list: dict = {}
        del compart_b_list
        compart_b_list: dict = {}
    print('overlap_list: ' + str(overlap_list))
    for overlap_entry in overlap_list:
        if 65 <= ord(overlap_entry) <= 90:
            prio += ord(overlap_entry) - 64 + 26
            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-64+26)))
        elif 97 <= ord(overlap_entry) <= 122:
            prio += ord(overlap_entry) - 96
            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-96)))
    print('Prio: ' + str(prio))

