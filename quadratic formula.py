import math
from matplotlib import pyplot as plt
import numpy as np 

print("x^2의 계수를 입력해주세요.")
a = int(input())
print("x의 계수를 입력해주세요.")
b = int(input())
print("상수항을 입력해주세요.")
c = int(input())

D = int(b ** 2 - 4 * a * c)
t = -b / (2 * a)
#print(t)
if a == 1:
    exp = "x²+ " + str(b) + "x + " + str(c) + " = 0"
else:
    exp = str(a) + "x²+ " + str(b) + "x + " + str(c) + " = 0"

# √±
if D > 0: 
    print("실수인 근이 2개 있습니다.")
     # -b / 2a 부분이 정수일 때
    if t % 1 == 0:
        if math.sqrt(D) % 1 == 0: #판별식이 제곱수라면
            print("x = ", t , "±", D)
        else:
            max_i = 0
            for i in range(1,D):
                if D % i == 0 and math.sqrt(i) % 1 == 0 and max_i < i:
                    max_i = i
            if max_i == 0:
                print("x = ", int(t) , "±√", D)
            else:
             print("x = ", int(t), "±", int(math.sqrt(max_i)) , "√", int(D / max_i))
    elif t % 1 != 0: # -b/2a 부분이 정수가 아닐 때
        gcd = math.gcd(b,(2*a))
        db = int(b / gcd)
        da = int((2*a) / gcd)
        t = str(db) + "/" + str(da)
        if math.sqrt(D) % 1 == 0: #판별식이 제곱수라면
            print("x = ", t , "±", D)
        else:
            max_i = 0
            for i in range(1,D):
                if D % i == 0 and math.sqrt(i) % 1 == 0 and max_i < i:
                    max_i = i
            if max_i == 0:
                print("x = ", t , "±√", D)
        
elif D == 0:
    print("중근입니다.")
    if t % 1 == 0:
        print("x : " , int(t))
    elif t % 1 != 0:
        print("x : ", str(-b) + "/" + str(2 * a))
        
else: print("허근입니다")

x = np.array(range(-10,11))
#print("x : ", x)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(color = "gray", alpha=1, linestyle='--')
plt.plot(x,(a*x)**2 + (b * x) + c)
plt.title(exp)

plt.show()
