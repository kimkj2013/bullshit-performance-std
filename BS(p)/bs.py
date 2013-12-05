# The Bullshit Performance Index
# Python Implimentation

import time
import os

count = 0
start_time = time.time()
f = open("bs", "w")

while count <= 50000000:
    f.write("bullshit")
    count += 1

print time.time() - start_time

f.close()
os.remove("bs")
