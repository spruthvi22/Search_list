"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code to search list for 2**5

"""
L=[1,2,4,8,16,32,64]
X=5

if 2**X in L:
    print('at index',L.index(2**X))
else:
    print(X,"not found")
