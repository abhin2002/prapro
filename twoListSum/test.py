# test.py
from twoSum import Solution  # Assuming the class is defined in a file named solution.py

def test_two_sum():
    # Create an instance of the Solution class
    s = Solution()

    # Test cases
    test_cases = [
        {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": [0, 1]},
        {"input": {"nums": [3, 2, 4], "target": 6}, "expected": [1, 2]},
        {"input": {"nums": [3, 3], "target": 6}, "expected": [0, 1]},
    ]

    # Iterate through test cases
    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]["nums"]
        target = test_case["input"]["target"]
        expected = test_case["expected"]

        # Get the actual result from the function
        result = list(s.twoSum(nums, target))  # Convert tuple to list for comparison

        # Check if the result matches the expected output
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
