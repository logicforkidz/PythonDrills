import unittest
import inspect
from nUniqueAddingToZero import zeroSumList

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
        num = 0
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_b(self):
        name = inspect.currentframe().f_code.co_name
        num = 1
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_c(self):
        name = inspect.currentframe().f_code.co_name
        num = 2
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_d(self):
        name = inspect.currentframe().f_code.co_name
        num = 3
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_e(self):
        name = inspect.currentframe().f_code.co_name
        num = 4
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_f(self):
        name = inspect.currentframe().f_code.co_name
        num = 5
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_g(self):
        name = inspect.currentframe().f_code.co_name
        num = 6
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_h(self):
        name = inspect.currentframe().f_code.co_name
        num = 7
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_i(self):
        name = inspect.currentframe().f_code.co_name
        num = 8
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

    def test_j(self):
        name = inspect.currentframe().f_code.co_name
        num = 9
        eret = 0
        l = zeroSumList(0)
        got = 0
        for item in l:
            got = got + item
        print (f"{name}: Trying input:\"{num}\"", end="")
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{num}\" Expected Output:{eret} but got:{got}")

if __name__ == '__main__':
    unittest.main()