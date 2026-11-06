print('module is added')
p= 3.14

def add(p,q):
    return p+q

def sub(p,q):
    if p>q:
        return p-q
    else:
        return q-p        

def div(p,q):
    from math import inf
    if q==0:
        return inf
    else:
        return p/q

def mul(p,q):
    return p*q

