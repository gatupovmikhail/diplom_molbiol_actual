import os


def more50(st):
    global more_50_predictions
    try:
        info = st[:-1].split('\t')[7]
    except IndexError:
        return None
    try:
        spliceai = info.split(';')[2].split(',')
    except IndexError:
        return None

    for pred in spliceai:
        try:
            probs = pred.split('|')[2:6]
        except IndexError:
            return None
        flag = 0
        for p in probs:
            if float(p) >= 0.5:
                flag = 1
        if flag == 1:
            more_50_predictions += 1


os.chdir('/home/gatupov/PycharmProjects/first_project/Ref_prediction')
files = os.listdir()
all_predictions = 0
more_50_predictions = 0
f_count = 0
for name_file in files:
    f_count += 1
    if f_count % 50 == 0:
        print(f_count, end=' ')
    try:
        f = open(name_file, 'r')
    except UnicodeDecodeError:
        print('UH!')
        print(name_file)
        continue
    f.close()
    with open(name_file, 'r') as f:
        st = '#'
        while '#' in st:
            try:
                st = f.readline()
            except UnicodeDecodeError:
                print('UH!')
                print(name_file)

        all_predictions += 3
        more50(st)
        for st in f:
            all_predictions += 3
            more50(st)

print('MORE 50')
print(more_50_predictions)
print('ALL:')
print(all_predictions)
print('PERSENT:')
print(more_50_predictions/all_predictions)
# MORE 50
# 185638
# ALL:
# 149696232
# PERSENT:
# 0.0012400980139566906

