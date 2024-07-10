def p(n):
    print("*"*n, end="")

def square(n,m):
    for i in range(n):
        if i == 0 or i == n-1:
            p(m)
            print()
        else:
            print("*", end="")
            for k in range(m-2):
                print(" ", end="")
            print("*")

square(8,18)