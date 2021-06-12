import numpy as npp
# ONE DIMENSION ARRAY
#print normal array
arr = npp.arange(0,11)
print(arr)
#print array with colon
print(arr[0:11])
arr[0:5] = 100
print(arr)

# > ONE DIMENSION ARRAY
arr_2d = npp.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
# row column in matrix
print(arr_2d[1][0])
