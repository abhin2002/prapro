import numpy as np
from multiprocessing import shared_memory
from concurrent.futures import ProcessPoolExecutor
import os

def fill_array(name, shape, start, end):
    existing_shm = shared_memory.SharedMemory(name=name)
    np_array = np.ndarray(shape, dtype=np.float64, buffer=existing_shm.buf)
    np_array[start:end] = np.random.rand(end-start)

if __name__ == "__main__":
    # Create a large numpy array
    large_array = np.zeros((1000000,), dtype=np.float64)
    shm = shared_memory.SharedMemory(create=True, size=large_array.nbytes)
    np_array = np.ndarray(large_array.shape, dtype=large_array.dtype, buffer=shm.buf)
    np_array[:] = large_array[:]

    # Define the number of processes and the size of chunks
    num_processes = os.cpu_count()
    chunk_size = len(np_array) // num_processes

    # Create a process pool and submit tasks
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(fill_array, shm.name, np_array.shape, i*chunk_size, (i+1)*chunk_size) for i in range(num_processes)]
        for future in futures:
            future.result()

    print(np_array)
    shm.close()
    shm.unlink()
