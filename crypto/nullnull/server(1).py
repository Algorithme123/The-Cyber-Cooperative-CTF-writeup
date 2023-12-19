import random

def generate(n):
    key = b""
    for i in range(n):
        key += chr(random.randint(1, 127)).encode() #can't have the flag leaking, can we?
    return key


def server():  
    print("Welcome to my secure flag sharer where there are null nulls!")
    
    flag = open("flag.txt", "rb").read()
    while True:
        guess = input("Print encrypted flag? (Y/N): ")

        if str(guess).upper() == "Y":
            enc = b""
            key = generate(64)
            for i in range(len(flag)):
                enc += chr(flag[i] ^ key[i] % 128).encode()
            print(enc)
        else:
            exit()

if __name__ == "__main__":
    server()