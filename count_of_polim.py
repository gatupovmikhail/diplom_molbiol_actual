import matplotlib.pyplot as plt

# with open('gnomad_polim_all.vcf','r') as polim:
#     zag = polim.readline()
#     border = [-1,0,10**(-4),0.001,0.01,0.05,0.1,0.2,0.3,0.4,0.5,1]
#     count = [0]*len(border)
#     for st in polim:
#         try:
#             af = float(st.split('\t')[4])
#         except ValueError:
#             print(st)
#         for i in range(len(border)-1):
#             if border[i] < af <= border[i+1]:
#                 count[i]+=1
#                 break
# print(count)
# s = sum(count)
# print(sum(count))
# for i in range(len(count)):
#     count[i] = count[i]/s
# print(count)
kolvo = [5630509,154879536, 35296357, 15473082, 5799724, 1642263, 1679828, 1063735, 795142, 642346, 1895933]
p1 = sum(kolvo[0:5])
p2 = sum(kolvo[5:])
print(p1)
print(p2)
print(p1/p2)
x = [0,10**(-4),0.001,0.01,0.05,0.1,0.2,0.3,0.4,0.5]

# 224798455
doli = [0.025046920362508718,0.6889706426140696, 0.157013343352382, 0.06883090900246623, 0.025799661301052983, 0.007305490600458086, 0.007472595841461632, 0.004731949781416425, 0.003537132850846328, 0.0028574306705088344, 0.00843392362282917]
print(len(x))
print(len(kolvo))

# plt.bar(x,doli,width=0.005)
# plt.grid(True)
# plt.show()

'''всего полиморфизмов 224.798.455
Из них менее 1 % - 217.079.208 (96,5 % от общего числа)
Более 1 % - 7719247 (3,5 % от всех)
Редких полиморфизмов больше частых в 28 раз.
Стоит отметить, что в базе 5630509, частота которых равна 0. (2,5 % от всех)
'''