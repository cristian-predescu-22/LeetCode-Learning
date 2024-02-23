def foo(n):
    if n <= 1:
        return n
    
    one_back = foo(n-1)
    two_back = foo(n-2)
    return one_back + two_back

    # Better example is
    
    # return self.foo(n-1) + self.foo(n-2)


print(foo(5))





# function F(n):
#     if n <= 1:
#         return n

#     oneBack = F(n - 1)
#     twoBack = F(n - 2)
#     return oneBack + twoBack