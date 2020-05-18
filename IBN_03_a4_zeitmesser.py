import os
import time

n = 10

for myprog in ["./pc", "./pc2"]:
    times = []

    for _ in range(n):
        start = time.time()
        os.system(myprog + " > /dev/null")
        times.append(time.time() - start)

    print(myprog, sum(times)/n)

