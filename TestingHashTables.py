import time
st = time.time()
import Phase2DoubleHashTable

HT = Phase2DoubleHashTable.HashTable()

for i in range(10000):
    HT.insert(str(i), "testme")

for i in range(10000):
    HT.remove(str(i))
#DLink.print_list()
#for i in range(10000):
 #   DLink.remove(i)
et = time.time()
elapsed = et - st
print("Execition time: ", elapsed, " seconds")
