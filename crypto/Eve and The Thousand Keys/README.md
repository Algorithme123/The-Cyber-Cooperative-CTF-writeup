
![Alt text](image.png)



For `Eve and The Thousand Keys` we used rsactftool to get 261 private keys from the public keys, a script then tried all of them. Initially I didn't know I got the flag, because I was expecting a shell which would pause the script, but the flag was printed as the MOTD or something and then closed the connection, so searching in the terminal for `flag{` would give you the flag.

## One

``` python
#!/usr/bin/env python
import os
import concurrent.futures
import random
import subprocess

N_CPUS = 30
ARGS = "--publickey ./public/key.{}.pub --private --output ./private/key.{}.priv --timeout 100 --attack SQUFOF"


def worker(i):
    if "key.{}.priv".format(i) in os.listdir("./private/"):
        print("key.{}.priv already exists".format(i))
        return

    program = ["/mnt/d/Random Github Repos/RsaCtfTool/RsaCtfTool.py"]
    args = ARGS.format(i, i)
    program += args.split(" ")
    subprocess.run(program)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=N_CPUS) as executor:
        # randomize order of tasks
        indexes = list(range(1, 1001))
        random.shuffle(indexes)


        tasks = [executor.submit(worker, i) for i in indexes]

        concurrent.futures.wait(tasks)


if __name__ == "__main__":
    main()




```

## Two

``` python

import os
import subprocess

files = os.listdir("./private/")

# Remove all the files that don't work
with open("non_working.txt", "r") as f:
    non_working = f.readlines()
    non_working = [x.strip() for x in non_working]

for filename in non_working:
    files.remove(filename)

print(files)

# For batches of at most 4 files
for i in range(0, len(files), 4):
    cmd = "ssh challenge@0.cloud.chals.io -p 17009 -v -o IdentitiesOnly=yes -o BatchMode=yes"
    for j in range(4):
        if i+j >= len(files):
            break
        cmd += " -i ./private/" + files[i+j]
    print(cmd)
    subprocess.run(cmd, shell=True)

    # Now we know all the keys that don't work, append them to non_working.txt
    with open("non_working.txt", "a") as f:
        for j in range(4):
            if i+j >= len(files):
                break
            f.write(files[i+j] + "\n")

    # break


```