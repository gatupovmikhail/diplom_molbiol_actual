import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import sys
np.random.seed(1200) #725
xgrid,ygrid = np.mgrid[-1.6:1.6:0.2, -1.6:1.6:0.2]
x1 = np.arange(-1.6,1.6,0.2)
y1 = np.arange(-1.6,1.6,0.2)
N = 1000
beg_gran = 100
gran = 1000000
# z = (0.5**2)/(2*np.pi)*np.exp(-0.5*np.sqrt(x**2+y**2))
def mnog_norm(x,y,r=0.1,m_x=0,m_y=0,s_x=1,s_y=1):
    return 1/(2*np.pi*s_x*s_y*np.sqrt(1-r**2))*np.exp(-1/(2*(1-r**2))*((x-m_x)**2/s_x**2 - 2*r*(x-m_x)*(y-m_y)/(s_x*s_y) + (y-m_y)**2/s_y**2))
zgrid = mnog_norm(xgrid,ygrid)
def one_norm(x,m=0,s=1):
    return 1/(np.sqrt(2*np.pi*s**2))*np.exp(-(x-m)**2/(2*s**2))
def marg_norm(x):
    #return integrate.trapz([mnog_norm(x,y) for y in np.arange(-3,3,0.01)])
    def integ(y):
        return mnog_norm(x,y)
    return integrate.quad(integ,-5,5)[0]
def usl_norm_xy(x,y):
    return mnog_norm(x,y)/marg_norm(y)
def usl_norm_yx(x,y):
    return mnog_norm(x,y)/marg_norm(x)
#print(one_norm(1))
#print(integrate.trapz([usl_norm_yux(1,y) for y in np.arange(-3,3,0.01)]))
# def odn_ocond(y):
#     return usl_norm_yux(1,y)
# print(integrate.quad(odn_ocond,-5,5))
### hohoho!
# print(marg_norm(2))
# print(one_norm(2))
#sys.exit()

# fig_th = pylab.figure()
# axes3dth = Axes3D(fig_th)
# axes3dth.set_title('Распределение плотности частиц')
# axes3dth.set_xlabel('x')
# axes3dth.set_ylabel('y')
# axes3dth.set_zlabel('x')
# axes3dth.plot_surface(xgrid, ygrid, zgrid, color='b')
# plt.show()
xs = []
ys = []
xs.append(1)
ys.append(1)
M = 1
### algoritm accept-reject using twice
shag = 0
for i in range(N+beg_gran):
####### for x
    shag+=1
    if (shag%50 == 0):
        print(shag,end=' ')
    while min(M*np.exp(-x1)-usl_norm_xy(x1,ys[len(ys)-1])) < 0 and (M < 100):
        M+=0.05
    assert M<100

    h = 0
    otn = 1
    u_ind = otn
    while u_ind >= otn and (h < gran):
        h+=1
        u = np.random.random()
        x_try = -np.log(u)
        u_ind = np.random.random()
        otn = usl_norm_xy(x_try, ys[len(ys) - 1])/(M * np.exp(-x_try))
    assert h<gran
    znak = np.random.random()
    if znak > 0.5:
        xs.append(x_try)
    else:
        xs.append(-x_try)
########## for y
    M=1
    while min(M*np.exp(-y1)-usl_norm_yx(xs[len(xs)-1],y1)) < 0 and (M < 100):
        M+=0.05
    assert M <100
    h = 0
    otn = 1
    u_ind = otn
    while u_ind >= otn and (h < gran):
        h+=1
        u = np.random.random()
        y_try = -np.log(u)
        u_ind = np.random.random()
        otn = usl_norm_yx(xs[len(xs) - 1],y_try)/(M * np.exp(-y_try))
    assert h<gran
    znak = np.random.random()
    if znak > 0.5:
        ys.append(y_try)
    else:
        ys.append(-y_try)



xp = xs[beg_gran:]
yp = ys[beg_gran:]

# GRAF PRACT
# frequency popadalovo
nd = 20
freq3pr = [[0]*nd for i in range(nd)]
a1x = min(xs)
a2x = max(xs)
dx = (a2x-a1x)/nd
a1y = min(ys)
a2y = max(ys)
dy = (a2y-a1y)/nd
for i in range(len(xp)):
    for k in range(nd):
        if a1x + k * dx <= xs[i] < a1x + (k + 1) * dx:
            break
    for j in range(nd):
        if a1y + j*dy <= yp[i] < a1y+ (j + 1) * dy:
            break
    freq3pr[j][k] += 1
## condicional probabilities
yf_cond = []
for k in range(nd):
    yf_cond.append((freq3pr[k][9])/(6*N))
xf_cond = []
for k in range(nd):
    xf_cond.append((freq3pr[9][k])/(6*N))
# otrezki
x_bar = []
y_bar = []
for k in range(nd): # создание отрезков гистограммы
    x_bar.append(a1x+k*dx + dx/2)
for k in range(nd): # создание отрезков гистограммы
    y_bar.append(a1y+k*dy + dy/2)
## cond_graf
# plt.bar(x_bar,xf_cond,width=0.8*dx)
# plt.plot(x_bar,[mnog_norm(x,0) for x in x_bar])
# plt.show()
# plt.bar(y_bar,yf_cond,width=0.8*dx)
# plt.plot(x_bar,[mnog_norm(x,0) for x in x_bar])
# plt.show()

## 3D
x3 = np.array(x_bar)
y3 = np.array(y_bar)
x_grid, y_grid = np.meshgrid(x3,y3)
# PRACT
z_grid = np.array(freq3pr)
z_grid = np.divide(z_grid, (N)/6.5)
dx3 = [[dx] * nd for i in range(nd)]
dy3 = [[dy] * nd for i in range(nd)]
dz3 = [[0] * nd for i in range(nd)]
fig_pr = pylab.figure()
axes3dpr = Axes3D(fig_pr)
axes3dpr.set_title('Sampling.Size={}'.format(N))
#axes3dpr.set_title('2D normal distribution \n $r=0.1,~~m_x=0,~~m_y=0,~~\sigma_x=1,~~\sigma_y=1$'.format(N))
axes3dpr.set_xlabel('x')
axes3dpr.set_ylabel('y')
axes3dpr.set_zlabel('Frequency')
for i in range(nd):
    axes3dpr.bar3d(list(x_grid)[i], list(y_grid)[i], dz3[i], dx3[i], dy3[i], list(z_grid)[i], color='r')
# fig_pr.savefig('sveta_biof/3d_pr_{}.png'.format(N))
axes3dpr.plot_surface(xgrid, ygrid, zgrid, color='b')
pylab.show()
plt.scatter(xp,yp)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Sampling. 2D representation')
plt.show()


