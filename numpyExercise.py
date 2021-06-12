# 1. import NumPy Lib as np
import numpy as np

# 2. create zeroes array w/ 10 elements
arr = np.zeros(10)
print(arr)

# 3. create ones array w/ 10 elements
arO = np.ones(10)
print(arO)

# 4. create array w/ 10 elements which each element contains 5 
print(arO * 5)

# 5. create array which contains a number from 10 - 50
Arr = np.arange(10,51)
print(Arr)

# 6. create array which contains an even number from 10 - 50
ArE = np.arange(10,51,2)
print(ArE)

# 7. create matrix 3x3 which contains a number from 0 - 8
M3_3 = np.array(([0,1,2],[3,4,5],[6,7,8]))
print(M3_3)

# 8. create matrix 3x3 which matrix is identity matrix
MI3_3 = np.eye(3,3)
print(MI3_3)

# 9. use Numpy to random a number between (0,1)
ArrR = np.random.rand(1)
print(ArrR)

# 10. use Numpy to random a number in a form of STD. Normal Dis. which contains 25 elements
Arr_STD = np.random.randn(25)
print(Arr_STD)

# 11. Matrix 10x10 which contains a number from 0.01 - 1.00
M10_10 = np.arange(1,101)
M10_10 / 100 # vector
M10_10 = np.arange(1,101).reshape(10,10) / 100 # matrix
print(M10_10) 

# 12. use linespace which include 20 elements and ascending from 0 - 1
LP = np.linspace(0,1,20)
print(LP)