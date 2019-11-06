"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Simple code to search list for 2**5

"""
L=[1,2,4,8,16,32,64]
X=5

for i in range(len(L)):
    if 2**X==L[i]:
        print('at index',i)
        break
else:
    print(X,'not found')        
