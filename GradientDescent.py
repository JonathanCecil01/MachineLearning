# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
import numpy as np
import sympy as sp 

x, y = sp.symbols("x y")

expr = (x+5)**2
dexpr = sp.diff(expr, x)
lr = 0.01
var =3
dfx = dexpr.evalf(subs = {x : 3})
diff = var - lr*dfx
while(diff>0.0000001):
    var = diff
    print(diff)
    diff = diff = var - lr*dfx

print(var)
print(diff)