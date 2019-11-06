"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code to search list for 2**5

"""
L=[]
for i in range(7):
    L.append(2**i)
X=5

if 2**X in L:
    print('at index',L.index(2**X))
else:
    print(X,"not found")
