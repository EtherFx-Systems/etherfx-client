import numpy as np
import ether.numpy as enp
import random
import time

mylist = [random.randint(0, 100) for i in range(10000000)]
start = time.time()
test = np.mean(mylist)
print("On machine:", time.time() - start)
start = time.time()
test2 = enp.mean(mylist).exec()
print("Cluster:",time.time() - start)
