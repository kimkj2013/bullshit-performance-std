# The Bullshit Performance Index
# Python Implimentation

import time
import os

count = 0
version = "0.1-alpha"

print "Bullshit Performance Standard Benchmarking Utility"
print "Version " + version

start_time = time.time()

f = open("bs", "w")

while count <= 50000000:
    f.write("bullshit")
    count += 1

final_time = time.time() - start_time

print final_time

f.close()
os.remove("bs")
