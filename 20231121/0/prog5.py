import random
import struct
import sys


with open(sys.argv[1], 'wb') as f1:
    with open(sys.argv[2], 'wb') as f2:
        for i in range(10):
            flt, bts, num = (random.random(),
                             random.randbytes(3),
                             random.randint(-2**31, 2**31 - 1))
            f1.write(struct.pack("<f3si", flt, bts, num))
            f2.write(struct.pack("!f3si", flt, bts, num))
