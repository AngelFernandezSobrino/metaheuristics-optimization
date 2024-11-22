import math
import random

s_list = [2, 1, 3, 4, 6, 5, 7, 9, 0, 8]  # savings (efficiency) list s list
s_list.sort(reverse=True)  # sort list from higher to lower savings

beta = 0.30  # parameter of the geometric probability distribution
print("Greegy behavior: ", s_list)

for i in range(
    10
):  # generate 10 biased-rand. lists using the geometric distribution
    c_list = s_list.copy()  # work on a copy of the original list
    o_list = []  # auxiliary list to store the selected value
    for i in range(len(c_list)):
        index = int(math.log(random.random()) / math.log(1 - beta))
        index = index % len(c_list)
        o_list.append(c_list[index])

c_list.pop(index)  # remove the index
print("Biased-Rand", i, ":", o_list)
