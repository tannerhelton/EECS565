import time
import itertools

def printAllKLength(set, k):
 
    n = len(set)
    printAllKLengthRec(set, "", n, k)
 
allArr = []

def printAllKLengthRec(set, prefix, n, k):
    if (k == 0) :
        allArr.append(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)
 
# Driver Code
if __name__ == "__main__":
    set1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    k = 6
    start_time = time.time()
    printAllKLength(set1, k)
    end_time = time.time()-start_time
    print("Finished length " + str(k) + " in "+str(end_time)+" seconds")
    print("Running itertools")
    allArr = [];
    start_time = time.time()
    for subset in itertools.product(set1, repeat=k):
        allArr.append(''.join(subset))
    end_time = time.time()-start_time
    print("Finished length " + str(k) + " in "+str(end_time)+" seconds")