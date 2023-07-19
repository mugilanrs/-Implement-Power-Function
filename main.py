#  Implement Power Function

def PowFunc(a, n, m):
    if n == 0:
        return 1
    if n == 1:
        return a
    p = PowFunc(a, n // 2, m)
    if n % 2 == 0:
        return (p * p) % m
    else:
        return (p * p * a) % m

a = int(input("Enter the value of a: "))
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

print(PowFunc(a, n, m))
