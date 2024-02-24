import numpy as np


def test_array_creation():
    # Original array creation
    array1 = np.random.rand(1000, 1000)

    # Convert the array to bytes
    bytes_array = array1.tobytes()

    # Recreate array from bytes
    array_recreated = np.frombuffer(bytes_array, dtype=array1.dtype).reshape(
        array1.shape
    )

    # Assertion to check if the original array and the recreated array are the same
    assert np.array_equal(
        array1, array_recreated
    ), "The original array and the recreated array are not the same."
