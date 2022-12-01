library(readr)
#library(qdap)
library(base)

max1_elf = 0
max2_elf = 0
max3_elf = 0
one_elf = 0
max_list = list()

file = read_lines("input1")

for ( line in file) {
#	act = strip(line,char.keep = c("1","2","3","4","5","6","7","8","9","0"))^
	act = trimws(line)
	if (act == '') {
		max_list <- append(max_list,one_elf)
		one_elf = 0 }
	else {
		one_elf = one_elf + strtoi(act)
	}
}
print("after for")
print(max_list)
max1_elf = max(unlist(max_list))
idx1 <- which(max_list %in% max1_elf)
max_list <- max_list[- idx1]
print("after 1st remove")
print(max_list)
max2_elf = max(unlist(max_list))
idx2 <- which(max_list %in% max2_elf)
max_list <- max_list[- idx2]
print("after 2nd remove")
print(max_list)
max3_elf = max(unlist(max_list))
idx3 <- which(max_list %in% max3_elf)
max_list <- max_list[- idx3]
print("after 3rd remove")
print(max_list)
top3 = max1_elf + max2_elf + max3_elf
print("Sum of top3 calories: ")
print(top3)
print("Top calories elf: ")
print(max1_elf)

