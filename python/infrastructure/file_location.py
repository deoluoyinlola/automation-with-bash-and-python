#!/usr/bin/env python

import os


directory = os.getcwd()
file_attr_list = []

for file_name in os.listdir(directory):
    
    for file_size in range(os.path.getsize(directory)):
        
        file_attr = {
    "name": file_name,
    "size": os.path.getsize(file_name)
}

    file_attr_list.append(file_attr)

    print(file_attr)