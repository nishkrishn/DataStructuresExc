# fibonacci example

import sys

def fib(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n:int):
    """Return the nth fibonacci number"""
    computed = {}  # already-computed values of fib
    def fibmem(k:int):    
        if k in computed:  # this and next op are O(1)
            return computed[k]  
        elif k < 2:
            computed[k] = k
        else:
            computed[k] = fibmem(k - 1) + fibmem(k - 2)
        return computed[k]        

    return fibmem(n)


if __name__== '__main__':    
    from time import time
    #fib3 = mkmemoized(fib)
    n = 30
    
    start = time()
    fib(n)
    dur = time() - start
    print("{} took {} seconds".format("fib({})".format(n), dur) )

    start = time()
    fib2(n)
    dur2 = time() - start
    print("{} took {} seconds".format("fib({})".format(n), dur2) )
    
    print("speedup: {} times faster".format(int(dur/dur2)))
    #start = time()
    #fib3(30)
    #print("{} took {} seconds".format("fib3(10)",str(time()-start)[:p]) )    