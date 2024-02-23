def foo(i):
    if i > 3:
        return i
    
    print(i)
    foo(i+1)
    print("End of call where i = "+str(i))
    return i


print(foo(1))