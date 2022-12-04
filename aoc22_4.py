cnt_overlap:int = 0

with open('input4','r') as file:
    for line in file:
        part_a = line.split(',')[0]
        part_b = line.split(',')[1]
        len_a = abs(int(part_a.split('-')[0])-int(part_a.split('-')[1]))
        len_b = abs(int(part_b.split('-')[0])-int(part_b.split('-')[1]))
        print('len a/b: ' + str(len_a) + ' ' + str(len_b))
        if len_a <= len_b:
           short_start = int(part_a.split('-')[0])
           short_stop = int(part_a.split('-')[1])
           long_start = int(part_b.split('-')[0])
           long_stop = int(part_b.split('-')[1])
        else:
           short_start = int(part_b.split('-')[0])
           short_stop = int(part_b.split('-')[1])
           long_start = int(part_a.split('-')[0])
           long_stop = int(part_a.split('-')[1])
        print('short_start: ' + str(short_start) + ' short_stop: ' + str(short_stop) + ' long_start: ' + str(long_start) + ' long_stop: ' + str(long_stop))
        if short_start >= long_start and short_stop <= long_stop:
            cnt_overlap += 1
            print('overlap found for line: ' + str(line))
        else:
            print('no overlap for line: ' + str(line))
    print('Overlap: ' + str(cnt_overlap))
