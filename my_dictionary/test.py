import unittest
import inspect
from myDictionary import myDictionaryInit, put, get, remove

class MyTestCase(unittest.TestCase):

    currentResult = None # holds last result object passed to run method
    @classmethod
    def setUpClass(cls):
        cls.dict = myDictionaryInit()

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
        op = "put(mydict, 1, 1)"
        eret = 1
        print (f"{name}: Trying input:\"{op}\"", end="")
        put(self.dict, 1, 1)
        got = get(self.dict, 1)
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{op}\" Expected Output:{eret} but got:{got}")

    def test_b(self):
        name = inspect.currentframe().f_code.co_name
        op = "put(mydict, 2, 2)"
        eret = 2
        print (f"{name}: Trying input:\"{op}\"", end="")
        put(self.dict, 2, 2)
        got = get(self.dict, 2)
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{op}\" Expected Output:{eret} but got:{got}")


    def test_c(self):
        name = inspect.currentframe().f_code.co_name
        op = "get(mydict, 3)"
        eret = -1
        print (f"{name}: Trying input:\"{op}\"", end="")
        got = get(self.dict, 3)
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{op}\" Expected Output:{eret} but got:{got}")


    def test_d(self):
        name = inspect.currentframe().f_code.co_name
        op = "put(mydict, 2, 1)"
        eret = 1
        print (f"{name}: Trying input:\"{op}\"", end="")
        put(self.dict, 2, 1)
        got = get(self.dict, 2)
        if eret==got: print ("...PASSED")
        else: print()
        self.assertEqual(eret,got, f"Failed {name}. Input:\"{op}\" Expected Output:{eret} but got:{got}")


    def test_e(self):
        name = inspect.currentframe().f_code.co_name
        op = "remove(mydict, 2)"
        eret = -1
        print(f"{name}: Trying input:\"{op}\"", end="")
        remove(self.dict, 2)
        got = get(self.dict, 2)
        if eret == got:
            print("...PASSED")
        else:
            print()


if __name__ == '__main__':
    unittest.main()