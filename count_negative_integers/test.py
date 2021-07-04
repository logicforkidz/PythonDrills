import unittest
import inspect
from countNegativeIntegers import countNegative

class MyTestCase(unittest.TestCase):

    currentResult = None # holds last result object passed to run method

    @classmethod
    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            amount, errors, failures, skipped

    @classmethod
    def tearDownClass(cls):
        failed = len(cls.errors) + len(cls.failures)
        success = cls.amount - failed
        percent = round((success - failed)*10/cls.amount, 1)
        print(f"\nTests run:{cls.amount} Passed:{success} Failed:{failed}")
        print(f"Score: {percent}")

    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        self.setResult(amount, errors, failures, skipped)

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_a(self):
        name = inspect.currentframe().f_code.co_name
        grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        eret = 8
        got = countNegative(grid)
        print (f"{name}: Trying input:\"{grid}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{grid}\" Expected Output:{eret} but got:{got}")

    def test_b(self):
        name = inspect.currentframe().f_code.co_name
        grid = [[3, 2], [1, 0]]
        eret = 0
        got = countNegative(grid)
        print (f"{name}: Trying input:\"{grid}\"", end= " ")
        if eret==got: print ("...PASSED")
        else: print()
        if not self.assertEqual(eret,got, f"Failed {name}. Input:\"{grid}\" Expected Output:{eret} but got:{got}"):
            return
        print ("PASSED")


    def test_c(self):
        name = inspect.currentframe().f_code.co_name
        grid = [[1, -1], [-1, -1]]
        eret = 3
        got = countNegative(grid)
        print (f"{name}: Trying input:\"{grid}\"", end= " ")
        if eret==got: print ("...PASSED")
        else: print()
        if not self.assertEqual(eret,got, f"Failed {name}. Input:\"{grid}\" Expected Output:{eret} but got:{got}"):
            return
        print ("PASSED")


    def test_d(self):
        name = inspect.currentframe().f_code.co_name
        grid = [[-1]]
        eret = 1
        got = countNegative(grid)
        print (f"{name}: Trying input:\"{grid}\"", end= " ")
        if eret==got: print ("...PASSED")
        else: print()
        if not self.assertEqual(eret,got, f"Failed {name}. Input:\"{grid}\" Expected Output:{eret} but got:{got}"):
            return
        print ("PASSED")

if __name__ == '__main__':
    unittest.main()