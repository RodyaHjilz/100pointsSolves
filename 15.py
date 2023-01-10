

def f(x, a):
    return (((x%a!=0) and (x%21 == 0)) <= (x%14!=0))

for A in range(1, 10000):
    if all(f(x,A) == 1 for x in range(1, 1000000)):
        print(A)
