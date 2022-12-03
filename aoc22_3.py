compart_a_list: dict = {}
compart_b_list: dict = {}
three_compart_a_list: dict = {}
three_compart_b_list: dict = {}
three_compart_c_list: dict = {}
overlap_list: list = []
three_overlap_list: list = []
prio:int = 0
three_prio:int = 0
line_count:int = 0
with open("input3","r") as file:
    for line in file:
        line_count += 1
        line = line.strip()
        length_line = int(len(line)) // 2
        compart_a = line[:length_line]
        compart_b = line[length_line:]
        print(compart_a + ' ' + compart_b)
        for letter in compart_a:
            compart_a_list[letter] = compart_a_list.get(letter,0) + 1
        for letter in compart_b:
            compart_b_list[letter] = compart_b_list.get(letter,0) + 1
        if line_count % 3 == 1:
            for letter in line:
                three_compart_a_list[letter] = three_compart_a_list.get(letter,0) + 1
        elif line_count % 3 == 2:
            for letter in line:
                three_compart_b_list[letter] = three_compart_b_list.get(letter,0) + 1
        elif line_count % 3 == 0:
            for letter in line:
                three_compart_c_list[letter] = three_compart_c_list.get(letter,0) + 1
  
#        print(compart_a_list)
        print('3A: ' + str(three_compart_a_list))
        print('3B: ' + str(three_compart_b_list))
        print('3C: ' + str(three_compart_c_list))
#        for entry in compart_a_list:
#            print(entry)
#            try:
#                if compart_b_list[entry] != None:
#                    overlap_list.append(entry)
#            except:
#                print(entry + ' not found in compart_b_list.')
#        del compart_a_list
#        compart_a_list: dict = {}
#        del compart_b_list
#        compart_b_list: dict = {}
        for entry in three_compart_a_list:
            try:
                if three_compart_b_list[entry] != None and three_compart_c_list[entry] != None:
                    three_overlap_list.append(entry)
            except:
                print(entry + ' not found in three_compart_b_list.')
        if line_count % 3 == 0:
            print('del lists')
            del three_compart_a_list
            three_compart_a_list : dict = {}
            del three_compart_b_list
            three_compart_b_list : dict = {}
            del three_compart_c_list
            three_compart_c_list : dict = {}
    print('three_overlap_list: ' + str(three_overlap_list))

#    for overlap_entry in overlap_list:
#        if 65 <= ord(overlap_entry) <= 90:
#            prio += ord(overlap_entry) - 64 + 26
#            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-64+26)))
#        elif 97 <= ord(overlap_entry) <= 122:
#            prio += ord(overlap_entry) - 96
#            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-96)))
#    print('Prio: ' + str(prio))
    for overlap_entry in three_overlap_list:
        if 65 <= ord(overlap_entry) <= 90:
            three_prio += ord(overlap_entry) - 64 + 26
            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-64+26)))
        elif 97 <= ord(overlap_entry) <= 122:
            three_prio += ord(overlap_entry) - 96
            print('Letter ' + overlap_entry + ' with priority: ' + str(int(ord(overlap_entry)-96)))
    print('three_Prio: ' + str(three_prio)) # 9169 is to high


