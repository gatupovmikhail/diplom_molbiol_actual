# Фильтр данных по числовым значениям в столбцах
from tkinter import Tk
from tkinter import *
from sys import getsizeof
import sys
import time
import os
filtrat=[] # #Здесь будут номера столбцов, по которым идет фильтрация

def destr(event):
    sys.exit()

def myfunction(event): # для полосы прокрутки
    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=800)

def myfunction1(event): # для полосы прокрутки
    canvas1.configure(scrollregion=canvas1.bbox("all"),width=700,height=740)


def com_knopki_dalee(event): # запуск фильтрации
    ###################################################################################
    def com_itog(event): ##################################################################
        # запись параметров фильтрации и запись в файл результата
        frame_l=Frame(new_wind,width=1000, height=30, bd=1)
        frame_l.place(x=10, y=800)
        process_start = Label(frame_l,height=5, text='Процесс запущен',font=14)
        process_start.pack(side=LEFT)

        filtr_min = [0]*len(filtrat) # min знач
        filtr_max = [0]*len(filtrat) # max знач
        filtr_text = [0]*len(filtrat) # text
        maska_filtr_chislo = [] # номера столбцов с числовой инф
        maska_filtr_text = [] # номера столбцов с текстовой инф

        # получение данных от пользователя. Сортировка на текстовую и числовую информацию
        for j in range(len(filtrat)):
            if  not(val[j].get() == '') and is_digit(val[j].get().split()[0]) == True:
                chisla=val[j].get()
                chisla2=chisla.split()
                if (len(chisla2) == 1):
                    process_interrupt = Label(frame_l, height=5, text='Неправильные данные', font=14)
                    process_interrupt.pack(side=RIGHT)
                    time.sleep(5)
                    sys.exit()

                filtr_min[j] = float(chisla2[0])
                filtr_max[j] = float(chisla2[1])
                maska_filtr_chislo.append(j)

            if not (val[j].get() == '') and is_digit(val[j].get().split()[0]) == False:
                maska_filtr_text.append(j)
                filtr_text[j] = val[j].get().replace(' *','')
        # запись заголовка
        name_file_output=''
        if (name_file.find('.vcf') == -1):
            name_file_output = name_file+'_sorted.txt'

        if not(name_file.find('.vcf') == -1):
            name_file_output = name_file+'_sorted.vcf'

        file_output = open(name_file_output,'w')

        if (name_file.find('.vcf') == -1):
            zagolovok_text = '\t'.join(zagolovok)
            file_output.write(zagolovok_text)
        else:
            zagolovok_text=''
            for slovo in text:
                zagolovok_text+= slovo
            file_output.write(zagolovok_text)

        file_output.close()
        new_wind.withdraw()
        # отбор. запись отфильтрованных данных
        file_output = open(name_file_output, 'a')

        sost = 0.01
        read_size = 0
        num1 = 0
        with open(name_file) as mfile:
            for str_tex in mfile:
                read_size += getsizeof(str_tex)
                if (read_size / size_mfile > sost):
                    print('\r {:.0%} '.format(sost), end='')
                    sys.stdout.flush()
                    sost += 0.01

                if (name_file.find('.vcf') == -1 ) and str_tex == text:
                    continue

                if not(name_file.find('.vcf') == -1) and (num1 < num) and str_tex == text[num1]:
                    num1 += 1
                    continue

                negoden = 0
                str1 = str_tex.split('\t')



                if not (len(maska_filtr_chislo) == 0):
                    for j in maska_filtr_chislo:
                        try:
                            fstr = float(str1[filtrat[j]])
                            if ( fstr < filtr_min[j] ) or ( fstr > filtr_max[j] ):
                                negoden+=1
                        except ValueError:
                            if not('*' in val[j].get()):
                                negoden+=1

                if not(len(maska_filtr_text) == 0):
                    for j in maska_filtr_text:
                        if not(str1[filtrat[j]] == filtr_text[j]) and not(str1[filtrat[j]] == '.'):
                            negoden+=1
                        if not(str1[filtrat[j]] == filtr_text[j]) and (str1[filtrat[j]] == '.') and not('*' in val[j].get()):
                            negoden+=1

                if negoden == 0:
                    #print(str_tex)
                    file_output.write(str_tex)




        file_output.close()
        process_end = Label(frame_l, height=5, text='Процесс окончен', font=14)
        process_end.pack(side = RIGHT)

        print('\n готово')
        sys.stdout.flush()
        sys.exit()
        ## конец выполнения программы

    ###########################################################################
    ##########################################################################
    # запуск фильтрации

    filtr=[0]*razmer
    for j in range(razmer):
        filtr[j]=flag[j].get()
    for j in range(razmer):
        if filtr[j]:
            filtrat.append(j)  #Здесь будут номера столбцов, по которым идет фильтрация

    # новое окно
    wind.destroy()
    new_wind = Toplevel(root)
    new_wind.geometry('1650x900')
    new_wind.title('Введите диапазон значений через пробел')
    root.withdraw()
    frame_title = Frame(new_wind, relief=GROOVE, width=100, height = 3)
    frame_title.place(x=150,y=0)
    rule = Label(frame_title, width = 80, height=3, text='Введите диапазон значений  через пробел \n Если допустимы пропуски значений,  введите также *')
    rule.config(font=('helvetica', 14, 'italic'))
    rule.pack(side=TOP)
    # виджеты для полосы прокрутки 2
    myframe1 = Frame(new_wind, relief=GROOVE, width=120, height=800, bd=1)
    myframe1.place(x=200, y=100)
    global canvas1
    canvas1 = Canvas(myframe1, width=120, height=1000)

    frame1 = Frame(canvas1)

    myscrollbar1 = Scrollbar(myframe1, orient="vertical", command=canvas1.yview)
    canvas1.configure(yscrollcommand=myscrollbar1.set)

    myscrollbar1.pack(side="right", fill="y")


    framezag=[0]*len(filtrat) # для создания полей ввода
    vvod= [0] * len(filtrat) # для сохранения значений из полей ввода
    text_zag = [0] * len(filtrat) # для сохранения значений из полей ввода
    val = []
    for j in range(len(filtrat)):
        tat = StringVar()
        val.append(tat)

    ############################################################
    # создание полей ввода
    for j in range(len(filtrat)):
        framezag[j] = Frame(frame1, width=1000, height=800, bd=1)
        #framezag[j].place(x=200, y=70+j*80)
        vvod[j] = Entry(framezag[j], width=30, bd=3, textvariable=val[j])
        text_zag[j] = Label(framezag[j],height=3, text=text_menu[filtrat[j]],font=12)

    #################################################################
    # кнопки
    new_wind.bind('<Return>',com_itog)
    new_wind.bind('<Escape>',destr)
    # frame_but = Frame(new_wind)
    #
    # stop = Button(frame_but, command=root.destroy)
    # stop.config(text='Выход')
    # stop.config(bd=8, relief=RAISED)
    # stop.config(width=15, height=3)
    # stop.config(font=('helvetica', 20, 'italic'))
    # stop.pack(side='bottom', padx=5, pady=5)
    #
    # dalee = Button(frame_but, text='Далее', command=com_itog)
    # dalee.config(width=12, height=3)
    # dalee.config(bd=8, relief=RAISED)
    # dalee.config(font=('helvetica', 20, 'italic'))
    # dalee.pack(side='top', padx=5, pady=5)
    # frame_but.pack(side='right')

    # упаковка
    for j in range(len(filtrat)):
        text_zag[j].grid(row=0,column=0)
        vvod[j].grid(row=0,column=1)
        framezag[j].grid(row=j,column=5)

    ## упаковка еще одна

    frame1.bind("<Configure>", myfunction1)

    canvas1.create_window((0, 0), window=frame1, anchor='nw')

    canvas1.pack(expand=YES, fill=BOTH, side='left')
    new_wind.mainloop()



####################################################################################################
def is_digit(string):  # Проверит, является ли строка числом
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

##########################################################################################
#####################################################################################
# здесь начало кода. Открытие и проверка качества файла.

#name_file='big_file.txt'
#name_file = 'PIBF1-anno.txt'

#print('ВВедите имя файлa')
name_file=str(input())




size_mfile = os.path.getsize(name_file)

mfile = open(name_file, 'r')

if not(name_file.find('.vcf') == -1 ):
    text = ['']*2000
    num = -1
    text1 = mfile.readline()
    text0 =''
    while (text1[0] == '#'):
        text0 = text1
        num+=1
        text[num]+=text0
        text1 = mfile.readline()
    text2 = mfile.readline()

    zagolovok = text0.split('\t')
    mfile.close()
    if not len(zagolovok) == len(text1.split('\t')):
        print("ВНИМАНИЕ: Количество заголовков не совпадает с числом столбцов. \n Есть столбцы, у которых нет заголовков!")
    if not len(text1.split('\t')) == len(text2.split('\t')):
        print("Внимание! С файлом явно что-то не так. Количество колонок в соседних строчках не совпадают!")
else:
    text = mfile.readline()
    row_1 = mfile.readline().split('\t')
    row_2 = mfile.readline().split('\t')
    mfile.close()

    zagolovok = text.split('\t')

    if not len(zagolovok) == len(row_1):
        print("ВНИМАНИЕ: Количество заголовков не совпадает с числом столбцов. \n Есть столбцы, у которых нет заголовков!")
    if not len(row_1) == len(row_2):
        print("Внимание! С файлом явно что-то не так. Количество колонок в соседних строчках не совпадают!")


razmer = len(zagolovok)  # количество столбцов







## формирование наполнения текстом для окна
text_menu = [''] * razmer
for j in range(razmer):
    text_menu[j] += zagolovok[j]

mfile.close()




## создание графического интерфейса Первое окно

root = Tk()
root.withdraw()
wind = Toplevel(root)

wind.geometry('1650x900')
wind.title('Выбор опций для фильтрации')

# логический массив для списка
flag =[]
for j in range(razmer):
    hah = BooleanVar()
    hah.set(FALSE)
    flag.append(hah)


# виджеты для полосы прокрутки
myframe=Frame(wind,relief=GROOVE,width=120,height=800,bd = 1)
myframe.place(x=600,y=50)

canvas=Canvas(myframe,width=120,height=1000)

frame=Frame(canvas)

myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand = myscrollbar.set)

myscrollbar.pack(side="right",fill="y")

# создание списка для выбора
spisok = [0]*razmer
for j in range(razmer):
    spisok[j] = Checkbutton(frame, text=text_menu[j], variable = flag[j])

for j in range(razmer):
    spisok[j].pack()

frame.bind("<Configure>",myfunction)

canvas.create_window((0, 0), window=frame, anchor='nw')

canvas.pack(expand=YES, fill=BOTH)

# создание кнопок
# frame_but=Frame(wind)
#
#
# dalee = Button(frame_but, text='Фильтр', command=com_knopki_dalee)
# dalee.config(width=12, height=3)
# dalee.config(bd=8, relief=RAISED)
# dalee.config(font=('helvetica', 20, 'italic'))
# dalee.pack(side='top',padx=5, pady=5)
#
# stop = Button(frame_but,command=root.destroy)
# stop.config(text='Выход')
# stop.config(bd=8, relief=RAISED)
# stop.config(width=15, height=3)
# stop.config(font=('helvetica', 20, 'italic'))
# stop.pack(side='bottom',padx=5, pady=5)
#
# frame_but.pack(side = 'right')
wind.bind('<Return>',com_knopki_dalee)
wind.bind('<Escape>',destr)


root.mainloop()

# gap.minder допкурсы

'''
#CHROM| Буквы. Заполнено строк: 30042658
POS| Числа. Диапазон: 6166.0 : 249212334.0 Заполнено строк: 30042658
ID| Буквы. 30042644 Пропусков. Заполнено строк: 14
REF| Буквы. Заполнено строк: 30042658
ALT| Буквы. Заполнено строк: 30042658
QUAL| Буквы. 30042644 Пропусков. Заполнено строк: 14
FILTER| Буквы. 30042644 Пропусков. Заполнено строк: 14
INFO
| Символы. Заполнено строк: 30042658


Всего строк: 30042658
'''