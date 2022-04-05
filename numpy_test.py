import time
import numpy as np

start_time = time.time()

num_multiplies = 1000000000
# data = range(num_multiplies)
number = 1

number *= np.power(1.0000001, num_multiplies)

end_time = time.time()

print(number)
print("Run time = {}".format(end_time - start_time))