print("Factorial de un número")


n = int(input("Cargue un número: "))
f = 1
for i in range(n,0,-1):
    f *= i
print("Factorial de", n, "=",f)