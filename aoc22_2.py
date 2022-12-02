
my_total_score: int = 0
op_total_score: int = 0
shapedict: dict = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}
lost:int = 0
draw:int = 3
win :int = 6
a_dict: dict = {"Z":lost,"X":draw,"Y":win} # if A is drawn which give lost,draw,win
b_dict: dict = {"X":lost,"Y":draw,"Z":win} # if A is drawn which give lost,draw,win
c_dict: dict = {"Y":lost,"Z":draw,"X":win} # if A is drawn which give lost,draw,win
op_a_dict: dict = {"Z":win,"X":draw,"Y":lost} # if A is drawn which give lost,draw,win
op_b_dict: dict = {"X":win,"Y":draw,"Z":lost} # if A is drawn which give lost,draw,win
op_c_dict: dict = {"Y":win,"Z":draw,"X":lost} # if A is drawn which give lost,draw,win
my_line:str = ''
op_line:str = ''

with open("input2","r") as file:
    for line in file:
        my_line = line.split(' ')[1].strip()
        op_line = line.split(' ')[0].strip()
        if op_line == 'A':
            my_total_score += a_dict[my_line] + shapedict[my_line]
            op_total_score += op_a_dict[my_line] + shapedict[op_line]
        if op_line == 'B':
            my_total_score += b_dict[my_line] + shapedict[my_line]
            op_total_score += op_b_dict[my_line] + shapedict[op_line]
        if op_line == 'C':
            my_total_score += c_dict[my_line] + shapedict[my_line]
            op_total_score += op_c_dict[my_line] + shapedict[op_line]
        print('my line: ' + str(my_line) + ' op line: ' + str(op_line) + ' my score: ' + str(my_total_score) + ' op score: ' + str(op_total_score))

