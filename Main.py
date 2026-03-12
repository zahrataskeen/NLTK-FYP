import numpy as np

array1 = [1,2,3]
array2 = [4,5,6]
           
print(array1)
print(array2)
print(array1 + array2) # [1, 2, 3, 4, 5, 6]

np_array = np.array(['Zahra', 'Ali'])

np_array1 = np.array(array1)
np_array2 = np.array(array2)

print(np_array1 + np_array2)

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
print(europe)
europe["italy"] = "Room"
print(europe)

print('italy' in europe) # 
