# The Bullshit Performance Index
# Python Implimentation

import time
import os
import sys

args = sys.argv[1:]
count = 0
max = 50000000
version = "0.1-alpha"
percent = 0

print("Bullshit Performance Standard Benchmarking Utility")
print("Version " + version)

start_time = time.time()

f = open("bull.shit", "w")

while count <= max:
    f.write("bullshit")
    if (count % 5000001 == 5000000):
        percent += 10
        print(str(percent) + "%")
    count += 1

final_time = time.time() - start_time

print(final_time)

f.close()
if "-k" not in args:
    os.remove("bull.shit")
