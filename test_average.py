def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return total / len(numbers)



#Unitted testcase
import unittest

class TestCalculateAverage(unittest.TestCase):
    def test_empty_list(self):
        numbers = []
        result = calculate_average(numbers)
        self.assertIsNone(result)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = calculate_average(numbers)
        self.assertEqual(result,-3)

    def test_mixed_numbers(self):
        numbers = [-1, 2, -3, 4, -5]
        result = calculate_average(numbers)
        self.assertEqual(result,-0.6)

#unittest.main() # not quite sure how to test this from the terminal without this.
# need to run the following in the terminal 
# "python3 -m unittest -v /home/dci-student/Desktop/python/exercise/testing-unittest/test_average.py" so the file path needs to start after "python3" directory