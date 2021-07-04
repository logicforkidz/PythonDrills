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
    # we will use a list of bins to store the key/values mapping
    # to store we will compute a hash of key and mod it with the number of bins to determine the bin number
    # if multiple elements hash to the same bin then we will store them in a list in that bin
    l = []
    for i in range(599):
        l.append(None)
    return l

# inserts a (key, value) pair into the given dictionary. If the key already exists in it
# update the corresponding value.
def put(dictionary, key, value):
    #determine the bin
    bin = key % 599
    #if the key already exists, remove it
    if dictionary[bin] != None:
        for k, v in dictionary[bin]:
            if k == key:
                remove(dictionary,key)
    else:
        #if the bin is empty store an empty list of tuples
        if dictionary[bin] == None:
            dictionary[bin] = []
    #append (key,value) tuple
    dictionary[bin].append((key,value))

#  returns the value to which the specified key is mapped, or -1 if no mapping is found for the key
def get(dictionary, key):
    #determine the bin
    bin = key % 599
    # return -1 for empty bin
    if not dictionary[bin]:
        return -1
    #find the key return the value
    for k, v in dictionary[bin]:
        if k == key:
            return v
    return -1

# removes the key and its corresponding value if the dictionary contains
def remove(dictionary, key):
    #determine the bin
    bin = key % 599
    index = 0
    #if the key exists, remove it
    for k, v in dictionary[bin]:
        if k == key:
            dictionary[bin].pop(index)
        index = index + 1

# print the dictionary
def printDict(dictionary):
    index = 0
    for itemList in dictionary:
        if not itemList:
            index = index + 1
            continue
        print (f"bin {index}: ", dictionary[index])
        index = index + 1

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

