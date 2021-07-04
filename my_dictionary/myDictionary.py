'''
Design a Dictionary without using any built-in python dictionaries using the following functions:

1. myDictionaryInit() initializes and returns a dictionary.
2. put(dictionary, key, value) inserts a (key, value) pair into the given dictionary. If the key already exists in it
update the corresponding value.
3. get(dictionary, key) returns the value to which the specified key is mapped, or -1 if no mapping is found for the key
4. remove(dictionary, key) removes the key and its corresponding value if the dictionary contains
the mapping for the key.

Note: key is always an integer

Example 1:
myDict = myDictionaryInit(); // dictionary is now initialized
put(myDict, 1, 1); // The dictionary is now [[1,1]]
put(myDict, 2, 2); // The dictionary is now [[1,1], [2,2]]
get(myDict, 1);    // return 1, The dictionary is now [[1,1], [2,2]]
get(myDict, 3);    // return -1 (i.e., not found), The dictionary is now [[1,1], [2,2]]
put(myDict, 2, 1); // The dictionary is now [[1,1], [2,1]] (i.e., update the existing value)
get(myDict, 2);    // return 1, The dictionary is now [[1,1], [2,1]]
remove(myDict, 2); // remove the mapping for 2, The dictionary is now [[1,1]]
get(myDict, 2);    // return -1 (i.e., not found), The dictionary is now [[1,1]]
'''

# initializes and returns a dictionary.
def myDictionaryInit():
    # write your code here
    return None

# inserts a (key, value) pair into the given dictionary. If the key already exists in it
# update the corresponding value.
def put(dictionary, key, value):
    # write your code here
    return None

#  returns the value to which the specified key is mapped, or -1 if no mapping is found for the key
def get(dictionary, key):
    # write your code here
    return -1

# removes the key and its corresponding value if the dictionary contains
def remove(dictionary, key):
    # write your code here
    return None

# print the dictionary
def printDict(dictionary):
    # write your code here
    return None

if __name__ == "__main__":
    myDict = myDictionaryInit()
    printDict(myDict)
    print("Storing (1,1)...")
    put(myDict, 1, 1)
    printDict(myDict)
    print("Storing (2,2)...")
    put(myDict, 2, 2)
    printDict(myDict)
    print ("Got value ", get(myDict, 1) ," for key=1")
    print ("Got value ", get(myDict, 3) ," for key=3")
    print("Storing (2,1)...")
    put(myDict, 2, 1)
    printDict(myDict)
    print ("Got value ", get(myDict, 2) ," for key=2")
    print("Removing key = 2...")
    remove(myDict, 2)
    printDict(myDict)
    print ("Got value ", get(myDict, 2) ," for key=2")
    print("Storing (601,601)...")
    put(myDict, 601, 601)
    print("Storing (2,2)...")
    put(myDict, 2, 2)
    printDict(myDict)
    print("Storing (2,603)...")
    put(myDict, 2, 603)
    printDict(myDict)

