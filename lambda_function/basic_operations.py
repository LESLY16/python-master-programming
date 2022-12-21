def f(x, opr):
    if opr == "sum":
        x = x+2
    if opr == "difference":
        x = x-2
    if opr == "product":
        x = x*2
    if opr == "division" and x > 0:
        x = x // 2
    return x

if __name__ == "__main__":
    difference = f(1, "difference")
    print(difference)
    
    prod = (lambda x : x*2)(3)
    print(prod)

    prod = lambda x,y : x*y
    sol = prod(9, 5)
    print(sol)

    sum = (lambda x,y : x+y)(5, 3)
    print(sum)

    algebra = (lambda x, y=4: x*y // 2)
    print(algebra)

    
