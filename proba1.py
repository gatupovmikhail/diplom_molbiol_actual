from sys import exit
import  time as ti
# проверяет схожесть геномов
file1=open('changing_genome.txt','r')
file0=open('genom.fa','r')
n1=0
n0=0
fl=0
st0=''
for st1 in file0:
    st2=file1.readline()
    n0+=1
    n1+=1
    if not(st1.upper()==st2.upper()):
        print('st0 {}'.format(st0),end='')
        print('st1 {}'.format(st1.upper()),end='')
        print('st2 {}'.format(st2.upper()),end='')
        print('n1 {}'.format(n1))
        print('next str:')
        if not '>' in st1:
            for r in range(20):
                n1+=1
                st1n=file0.readline()
                st2=file1.readline()
                print('{} {}'.format(r,n1))
                print('st1 {}'.format(st1n.upper()), end='')
                print('st2 {}'.format(st2.upper()), end='')
        #print('n0 {}'.format(n0))
        break
    st0=st1
file1.close()
file0.close()



# mfile=open('genom.fa','r')
# n=0
# t0=ti.time()
# for st in mfile:
#     n+=1
# t1=ti.time()
# print('time of working line: {:.3}'.format(t1-t0))
#
# mfile.close()
#
# mfile=open('genom.fa','r')
# n=0
# t0=ti.time()
# st='a'
# stro=0
# while not(st==''):
#     st=mfile.read(1)
#     n+=1
#     if st=='\n':
#         stro+=1
# print(stro)
# t1=ti.time()
# print('time of working char: {:.3}'.format(t1-t0))
#
# mfile.close()





# st0=''
# n=0
# g=0
# mfile=open('num_repeat_str.txt','r')
# for st in mfile:
#     n+=1
#     if st==st0:
#         print(n)
#         print(st)
#         g+=1
#         mfile.close()
#         exit()
#     st0=st
# print(g)
# mfile.close()

