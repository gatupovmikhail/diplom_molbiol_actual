from time import time
t1 = time()
import os  # ctrl + alt+ 7
def func_sort_chr(name):
    try:
        nchr = int(name.split('_')[0].replace('chr',''))
        return nchr
    except ValueError:
        return 25
def func_sort_pos(name):
    nchr = int(name.split('_')[1])
    return(nchr)

path = '/home/gatupov/PycharmProjects/first_project/Predictions on whole alternative genome/archives'
files = os.listdir(path)
files.sort(key=lambda x: (func_sort_chr(x),func_sort_pos(x)) )
for i in range(len(files)):
    files[i] = path + '/' + files[i]
    print(files[i])
t2 = time()
print(t2-t1)