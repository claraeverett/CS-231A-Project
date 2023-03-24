# -*- coding: utf-8 -*-
"""Repeats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1As_Xv5zyq_wPxl7aEloQywmnUaL8DtAL
"""

from google.colab import drive
import os
import csv

drive.mount('/content/drive', force_remount=True)

short = True
if short:
    csv_dir = 'drive/MyDrive/CS231A/asllvd_shorter_data.csv'
else:
    csv_dir = 'drive/MyDrive/CS231A/asllvd_signs_2022_11_29.csv'

json_dir = 'drive/MyDrive/CS231A/ASLLVD/output_json/'
# column numbers of relavent info in the csv
label_index = 1
json_index = 0
d = dict()

i = 0
count = 0
with open(csv_dir, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    for row in csv_reader:
        i += 1
        if short: i = int(row[json_index])
        if not os.path.exists(json_dir + str(i)):
            continue
        count += 1
        label = row[label_index]
        if label in d: 
            d[label] += 1
        else:
            d[label] = 1
print('Finished')

print('Total instances:', count)
print('Number of classes:', len(d))
d_values = list(d.values())
max_count = max(d_values)
counts = [0] * max_count
for i in range(max_count):
    counts[i] = d_values.count(i+1)
print('Max sign instances:', max_count)
print('i\'th entry is the number of classes with i instances')
print(counts)

[456, 816, 371, 494, 198, 170, 81, 81, 30, 25, 14, 9, 4, 4, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

import json

js_dict = json.dumps({"x": list(d.values())})
with open("drive/MyDrive/CS231A/Project/hist_long.json", "w") as outfile:
    outfile.write(js_dict)

