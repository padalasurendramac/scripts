#!/usr/local/bin/python3
import sys
import pdb
from datetime import datetime
#pdb.set_trace()

split_file_name = sys.argv[1].replace(".txt","")
more_questions = True
limit = 10000
file_name_low_num = 1
file_name_high_num =10000
count = 1
row = 1
with open(sys.argv[1], 'r', encoding="utf-8-sig") as in_f:
    utterance_file  = in_f.readlines()
out_fs = open(split_file_name + str(file_name_low_num) + "to" + str(file_name_high_num) + ".txt", 'a')
for i in utterance_file:
    if count <= 10000 and more_questions:
        out_fs.write(i)
        count += 1
        row += 1
        if row > len(utterance_file):
            more_questions = False
    else:
        if more_questions:
            if len(utterance_file) - row < 10000:
                count -= 1
                out_fs.close()
                file_name_low_num += count
                file_name_high_num = len(utterance_file)
                count = 1
                out_fs = open(split_file_name + str(file_name_low_num) + "to" + str(file_name_high_num) + ".txt", 'a')
            else:
                count -=1
                out_fs.close()
                file_name_low_num += count
                file_name_high_num += count
                count = 1
                out_fs = open(split_file_name + str(file_name_low_num) + "to" + str(file_name_high_num) + ".txt", 'a')
        else:
            out_fs.close()
