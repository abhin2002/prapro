import numpy as np 
import time

start_time = time.time()

array1 = np.random.rand(1000,1000)

end_time = time.time()

print("time taken : ",end_time - start_time)


#convert the array to bytes
bytes_array = array1.tobytes()

#recreate array from bytes
array_recreated = np.frombuffer(bytes_array, dtype=array1.dtype).reshape(array1.shape)

if np.array_equal(array1, array_recreated):
    print("The original array and the recreated array are the same.")
else:
    print("The original array and the recreated array are not the same.")