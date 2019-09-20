import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

######### Original Code ##########
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime on my machine was 12.94 seconds


# use bst to optomize 
# import in bst
# iterate through names_1 list using insert from bst 
# insert thoses names into "names"
# go through i of names_2
# check to see if any names in names_2 are in the new "names"
# if so the append names_2 to only have the duplicates

duplicates = []

names = BinarySearchTree(names_1[0])
for i in names_1:
    names.insert(i)
for i in range(len(names_2)):
    if names.contains(names_2[i]):
        duplicates.append(names_2[i])
# runtime on my machine was 0.33 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

