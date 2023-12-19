from pwn import *

# context.log_level = 'debug'

host = '0.cloud.chals.io'
port = 15076

client = remote(host, port)
data = client.recvuntil(b'(Y/N):')

dict = {}

for i in range(49):
    dict[i] = []

try:
    while True:
        client.sendline(b'Y')
        data = client.recvuntil(b'(Y/N):')
        data = eval(data.splitlines()[0]).hex()
        data = [data[x:x+2] for x in range(0, len(data), 2)]
        for i, d in enumerate(data):
            if d not in dict[i]:
                dict[i].append(d)
        valid = True
        for i in range(len(dict)):
            if len(dict[i]) < 127:
                valid = False
        if valid:
            break
except:
    print('Caught error')

res = []
tab = []
for i in range(128):
    tab.append(i)

charset = "abcdefghijklmnopqrstuvwxyz{}_"

for i in dict:
    b = [int(x, 16) for x in dict[i]]
    c = [chr(x) for x in tab if x not in b and chr(x) in charset]
    res.append(c)

print(res)