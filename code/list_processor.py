import os
import re
from parse_config import parse_config

def process_train_list(config_dict):
    with open(config_dict['train_list'], 'rb') as train_list_file:
        train_list = train_list_file.readlines()
    
    picname_list = []
    label_list = []
    for line in train_list:
        line = line.strip()
        m = re.match(r'(.+\.jpg).+(ZJL.+)', line)
        if m is not None:
            picname_list.append(m.group(1))
            label_list.append(m.group(2))
    #print 'total %d images' % (len(picname_list))
    return picname_list, label_list

def get_label_dict(config_dict):
    with open(config_dict['label_list'], 'rb') as label_list_file:
        label_list = label_list_file.readlines()
    label_dict = {}
    for line in label_list:
        line = line.strip()
        m = re.match(r'(ZJL[0-9]+)\s+([a-zA-Z]+)', line)
        if m is not None:
            label_dict[m.group(1)] = m.group(2)
    #print 'total %d kind of label' % (len(label_dict))
    return label_dict

def search_picname(picname, namelist):
    if os.path.isfile(namelist) is False:
        return -1
    with open(namelist, 'rb') as f:
        lines = f.readlines()
    for i,line in enumerate(lines):
        if picname in line:
            return i
    return -1

def add_picname(picname, namelist):
    with open(namelist, 'a') as f:
        f.writelines(picname+'\n')

def remove_picname(picname, namelist):
    col = search_picname(picname, namelist)
    if col >= 0:
        with open(namelist, 'rb') as f:
            lines = f.readlines()
            lines[col] = ''
        with open(namelist, 'wb') as f:
            f.writelines(lines)

if __name__ == '__main__':
    pass
