library(readr)
library(base)
library(stringr)
my_total_score = 0
op_total_score = 0
shapedict = c("A"=1,"B"=2,"C"=3,"rock"=1,"paper"=2,"scissor"=3)
lost= 0
draw= 3
win = 6
result_dict = c('X'=lost,'Y'=draw,'Z'=win)
op_result_dict = c('X'=win,'Y'=draw,'Z'=lost)
a_dict = c('X'='scissor','Y'='rock','Z'='paper')
b_dict = c('X'='rock','Y'='paper','Z'='scissor')
c_dict = c('X'='paper','Y'='scissor','Z'='rock')
tries = 0
my_line = ''
op_line = ''
a="A"
b="B"
c="C"

file = read_lines("input2")
    for (line in file) {
        my_line = substr(line,3,3)
        op_line = substr(line,1,1)
        if (op_line == a) {
            my_total_score = my_total_score + result_dict[my_line] + shapedict[a_dict[my_line]]
            op_total_score = op_total_score + op_result_dict[my_line] + shapedict[op_line]
}
        if (op_line == b){
            my_total_score = my_total_score + result_dict[my_line] + shapedict[b_dict[my_line]]
            op_total_score = op_total_score + op_result_dict[my_line] + shapedict[op_line]
}
        if (op_line == c) {
            my_total_score = my_total_score + result_dict[my_line] + shapedict[c_dict[my_line]]
            op_total_score = op_total_score + op_result_dict[my_line] + shapedict[op_line]
    }
    tries = tries +1
}
    print(my_total_score)
    print(tries)


