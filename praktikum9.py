# import pickle as pc

# # example_dict = {1: "1", 2: "2", 3: "3"}

# # pickle_out = open("dict.praktikum", "wb")
# # pc.dump(example_dict, pickle_out)
# # pickle_out.close()

# pickle_in = open("dict.praktikum", "rb")
# example_dict = pc.load(pickle_in)

# print(example_dict)
# print(example_dict[2])

# FILE PATH
# os.path.basename
import os

# folder = os.path.basename(
#     "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9")
# print(folder)
# file = os.path.basename(
#     "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9\STRINGS.py")
# print(file)

# os.path.dirname
DIR = os.path.dirname(
    "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9")
print(DIR)
