import sys
n = int(input("Antall Punkter: "))
i = 0
v = 0
x = []
y = []
Sx = 0.0
Sy = 0.0
Sxy = 0.0
Sxx = 0.0

while i < n:
    sys.stdout.write("x%d" %(i+1))
    x.append(int(input(": ")))
    sys.stdout.write("y%d" %(i+1))
    y.append(int(input(": ")))
    i += 1

while v < n:
    Sx = Sx + x[v]
    Sy = Sy + y[v]
    Sxy = Sxy + (x[v]*y[v])
    Sxx = Sxx + (x[v]*x[v])
    v += 1

print("Sy*Sx =", Sy*Sx)
print("Sx*Sx =", Sx*Sx)
print("Sy*Sy =", Sy*Sy)

a = (n*Sxy-Sx*Sy)/(n*Sxx-(Sx)*(Sx))
b = (Sy/n)-a*(Sx/n)
print("a = %6f" %a)
print("b = %6f" %b)
print("y = %6fx + %6f" %(a, b))


print("Job done!")
