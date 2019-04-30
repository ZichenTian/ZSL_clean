import os

def make_list(rootpath, savename, labelname):
    imgs = os.listdir(rootpath)
    results = []
    labels = []
    for img in imgs:
        results.append(os.path.join(rootpath, img) + '\n')
        labels.append('0\n')
    results.sort()
    with open(savename, 'wb') as f:
        f.writelines(results)
    with open(labelname, 'wb ') as f:
        f.writelines(labels)

if __name__ == '__main__':
    make_list('/home/tianzichen/Working/reid/process_data/data', './imglist.txt', './labels.txt')