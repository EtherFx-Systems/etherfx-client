import numpy as np
import ether.numpy as enp
import random
import time

mylists = [[random.randint(0, 100) for i in range(1000000)] for i in range(3)]
start = time.time()
for i in mylists:
    test = np.mean(i)
print("On machine:", time.time() - start)
start = time.time()
prs = []
for i in mylists:
    prs.append(enp.mean(i))
for i in prs:
    i.exec()
print("Cluster:",time.time() - start)
