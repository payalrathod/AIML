import time
from concurrent.futures import ThreadPoolExecutor


def return_num(a):
    time.sleep(1)
    return a


print(return_num(22))

start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    for result in executor.map(return_num, range(100)):
        print("Count: {0}".format(result))
print("total time: {0}".format(time.time() - start))



# vulture: to find dead code
message = 0

import os
# run command vulture filename.py in terminal to execute vulture library
















