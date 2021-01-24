# project: codeincode,
# module: encdec.py,
# author: John Lynch
# date: January 2021
# >>> A playground for encoding and decoding, encrypting and decrypting

from math import ceil


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
