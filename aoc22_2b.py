
my_total_score: int = 0
op_total_score: int = 0
shapedict: dict = {"A":1,"B":2,"C":3,"rock":1,"paper":2,"scissor":3}
lost:int = 0
draw:int = 3
win :int = 6
result_dict: dict = {'X':lost,'Y':draw,'Z':win}
op_result_dict: dict = {'X':win,'Y':draw,'Z':lost}
a_dict: dict = {'X':'scissor','Y':'rock','Z':'paper'} # op: rock 
b_dict: dict = {'X':'rock','Y':'paper','Z':'scissor'}
c_dict: dict = {'X':'paper','Y':'scissor','Z':'rock'}

my_line:str = ''
op_line:str = ''

with open("input2","r") as file: # 13093 is to high, 11995 is to low
    for line in file:
        my_line = line.split(' ')[1].strip()
        op_line = line.split(' ')[0].strip()
        if op_line == 'A':
            my_total_score += result_dict[my_line] + shapedict[a_dict[my_line]]
            op_total_score += op_result_dict[my_line] + shapedict[op_line]
            print('my line: ' + str(my_line) + ' op line: ' + str(op_line) + ' my shape: ' + str(a_dict[my_line]) + ' my score: ' + str(my_total_score) + ' op score: ' + str(op_total_score))
        if op_line == 'B':
            my_total_score += result_dict[my_line] + shapedict[b_dict[my_line]]
            op_total_score += op_result_dict[my_line] + shapedict[op_line]
            print('my line: ' + str(my_line) + ' op line: ' + str(op_line) + ' my shape: ' + str(b_dict[my_line]) + ' my score: ' + str(my_total_score) + ' op score: ' + str(op_total_score))
        if op_line == 'C':
            my_total_score += result_dict[my_line] + shapedict[c_dict[my_line]]
            op_total_score += op_result_dict[my_line] + shapedict[op_line]
            print('my line: ' + str(my_line) + ' op line: ' + str(op_line) + ' my shape: ' + str(c_dict[my_line]) + ' my score: ' + str(my_total_score) + ' op score: ' + str(op_total_score))





