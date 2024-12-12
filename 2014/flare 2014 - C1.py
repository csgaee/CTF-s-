import binascii
with open(r"./dat_secret.file",'rb') as f:
    #print(f.read())
    data = f.read()


def txt_logic(bytes):
    for b in bytes:
        print(chr((b >> 4 | b << 4 & 240) ^ 41),end="")



if __name__ == "__main__":
    txt_logic(data)