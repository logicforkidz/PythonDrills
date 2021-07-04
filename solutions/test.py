import os
import unittest
from importlib import import_module


# build a list of packages
pkgs = []
for file in os.listdir('.'):
    if file == "test.py": continue
    if file.endswith('.py'):
        pkgs.append(file[:-3])

# our test suite
suite_list = []
# for each package, if there is a test file in it then import it
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for pkg in pkgs:
    #make package directory name
    pkg_dir = ""
    for c in pkg:
        if c not in capitals:
            pkg_dir = pkg_dir + c
        else:
            pkg_dir = pkg_dir + '_' + c.lower()
    #make test file name
    test_file_name = os.path.join("..",pkg_dir,"test.py")
    # import test cases from file if it exists
    if os.path.isfile(test_file_name):
        mod = import_module(pkg_dir + '.test')
        suite_list.append((pkg_dir, unittest.loader.findTestCases(mod)))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    for pkg, suite in suite_list:
        print("\n---------------------------------")
        print(f"Running tests for {pkg}")
        print("---------------------------------")
        runner.run(suite)

