# SHA-secure hash algorithm base of blockchain
import hashlib

str1 = 'abc def2'
# process of hashing
# fist step is to encode
# then apply hashing algo
a = hashlib.sha256(str1.encode())
print(a)  # hash object
print(a.hexdigest())

a = hashlib.sha384(str1.encode())
print(a)
print(a.hexdigest())
print(len(a.hexdigest()))

a = hashlib.sha224(str1.encode())
print(a)
print(a.hexdigest())
print(len(a.hexdigest()))

# numba library can used for numpy arrays
# python is interpreted programming lang so is slow
from numba import jit
import numpy as np
import time

x = np.arange(1000).reshape(100, 10)


@jit(nopython=True)
def fast(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


start = time.time()
fast(x)
end = time.time()
print('time taken: %s' % (end - start))

start = time.time()
fast(x)
end = time.time()
print('time taken: %s' % (end - start))
