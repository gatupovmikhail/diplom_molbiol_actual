import math
def pus(k):
    return (10^k)/math.factorial(k)*math.exp(-10)
sum = 0
for i in range(10):
    sum+=pus(i)
print(sum)
print(1-sum)
#0.0012361328180878356
# ans = 0.9987638671819121

# 0.001236132819847234
# 0.9987638671801528