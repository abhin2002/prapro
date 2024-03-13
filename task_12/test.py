import pytest
import subprocess

def test_sum():
    # Test case to check if the sum of two integers is calculated correctly
    process = subprocess.Popen(['python', 'task_12/task12.py', '2', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert process.returncode == 0
    assert b"Sum :  5.0" in stdout

