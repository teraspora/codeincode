# project: codeincode,
# module: encdec.py,
# author: John Lynch
# date: January 2021
# >>> A playground for encoding and decoding, encrypting and decrypting


import sys
from math import ceil
from PIL import Image
from random import randint


def stoi(s):
    """
    Encode a string to an integer.

    Ex.: stoi('cat') = 6513012
    """
    return int(''.join(format(ord(ch), 'b').zfill(8) for ch in s), 2)

def itos(n):
    """
    Decode an integer into the original string.

    Ex.: itos(6513012) = 'cat'
    """
    b = format(n, 'b')
    bl = ceil(len(b) / 8) * 8
    b = b.zfill(bl)
    bsl = ''.join([chr(int(''.join(b[i:i+8]), 2)) for i in range(0, bl, 8)])
    return bsl

def stobs(s):
    """
    Encode a string to an string of binary digits 0 || 1

    Ex.: stobs('cat') = '011000110110000101110100'
    """
    return ''.join(format(ord(ch), 'b').zfill(8) for ch in s)

def bstos(b):
    """
    Decode a bitstring into the original string.

    Ex.: bstos('011000110110000101110100') = 'cat'
    """
    bl = ceil(len(b) / 8) * 8
    b = b.zfill(bl)
    bsl = ''.join([chr(int(''.join(b[i:i+8]), 2)) for i in range(0, bl, 8)])
    return bsl

def enc(img, msg):
    done = False
    bs = stobs(msg)
    bsl = len(bs)
    print(f"{bs=}")
    w, h = img.size
    curs = 0
    pin = randint(0, w * h - 1024)
    x0, y0 = pin % w, pin // w
    for y in range(y0, h):
        for x in range(x0, w):
            alpha = 254 + int(bs[curs])
            print(f"{alpha=}")
            p = img.getpixel((x, y))
            print(p, curs)
            t = (*p[:3], alpha)
            print((x, y), f"{t=}")
            img.putpixel((x, y), t)
            curs += 1
            if curs >= bsl:
                done = True
                break
        if done:
            break
        
    of = input(">> Enter path to output file:  ")
    try:
        img.save(of)
    except:
        print("<!> Can't save the image.   Tough.   Debug me.")
    print(f">> Done ok.   Pin is {pin}. Cartesian ({x0}, {y0}).   Exiting.")
    sys.exit(0)
    
def dec(img, pin):
    w, h = img.size
    vals255 = 0
    bs = []
    for p in range(pin, w * h):
        val = img.getpixel((p % w, p // w))[3]
        if val == 255:
            vals255 += 1
            if vals255 > 16:
                break
        else:
            vals255 = 0
        bs.append(str(val - 254))
        return = bstos(''.join(bs))

    
if __name__ == '__main__':
    img_path = input(">> Enter path to source image:  ")
    try:
        img = Image.open(img_path)
    except:
        print("<!> Can't find an image at that location.   Exiting.")
        sys.exit(1)
    msg = input(">> Enter message to be hidden in the image:  ")
    enc(img, msg)