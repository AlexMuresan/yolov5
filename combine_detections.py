import os
import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

# Path for the detections
path = os.path.abspath('/data_disk/ds_ro/amuresan/yolov5/runs/detect/exp6/labels')
file_list = []
path_list = []


for file in os.listdir(path):
    file_list.append(file)
    path_list.append(os.path.join(path, file))

path_list = natural_sort(path_list)

final_file_name = file_list[-1].split('_')[0] + "_all-detections." + file_list[-1].split('.')[-1]
final_file_path = os.path.join(path, final_file_name)

print(f"Writting to {final_file_path}\n")

for file in path_list:
    frame = file.split('_')[-1].split('.')[0]
    with open(file, 'r') as f:
        with open(final_file_path, "a+") as g:
            for line in f.readlines():
                g.write(f"{frame} {line}")

print("Done!")
