import matplotlib as mpl
import matplotlib.pyplot as plt
import collections

def plotting_hist(name_file,name_file_out,title):

    x=[]
    y=[]


    hist=[['']*2500 for i in range(51)]
    fhist=[0]*51
    for k in range(51):
        fhist[k]=k/100





    with open(name_file) as mfile:
        zag=mfile.readline()
        st1=mfile.readline()
        print(zag)
        print(st1)
        for st in mfile:
            stm=st.split()
            x.append(stm[0][0:-1])
            y.append(float(stm[1]))




    g=[0]*51
    for j in range(len(y)):
        fl=0
        for k in range(len(fhist)-1):

            if y[j]==0 and fl==0:
                hist[0][g[0]]=x[j]
                g[0]+=1
                fl=1

            if (y[j]>fhist[k]) and (y[j]<fhist[k+1]) and not(y[j]==0):
                hist[k+1][g[k+1]]=x[j]
                g[k+1]+=1

    # g=0
    # while not(hist[0][g]==''):
    #     print(hist[0][g])
    #     g+=1


    file_out=open(name_file_out,'w')

    for k in range(len(fhist)):
        file_out.write(str(fhist[k]) + '\n')
        for t in range(2500):
            if hist[k][t] == '':
                file_out.write('\n')
                break
            else:
                file_out.write(str(hist[k][t]) + '\t')
    file_out.close()

    fig,ax=plt.subplots()


    plt.bar(fhist,g,width=0.007)
    ax.grid(True)
    plt.xlabel('score')
    plt.ylabel('Number of genes with this score')
    plt.title(title)
    print(fhist)
    print(g)
    plt.show()


plotting_hist('genes_score_ad','raspr_score_genes_ad.txt','genes AD')
plotting_hist('genes_score_ar','raspr_score_genes_ar.txt','genes AR')
plotting_hist('genes_score_adar','raspr_score_genes_adar.txt','genes AD/AR')

