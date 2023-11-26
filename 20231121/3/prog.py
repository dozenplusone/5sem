import sys


# RIFF uses little-endian format.
endian = "little"


def is_legit_wav_hdr(hdr):
    return (len(hdr) == 44
            and hdr[:4] + hdr[8:16] + hdr[36:40] == b"RIFFWAVEfmt data"
            and int.from_bytes(hdr[16:20], endian) == 16)


data = sys.stdin.buffer.read(44)
print(
    "Size=%d, Type=%d, Channels=%d, Rate=%d, Bits=%d, Data size=%d" % (
        int.from_bytes(data[4:8], endian),
        int.from_bytes(data[20:22], endian),
        int.from_bytes(data[22:24], endian),
        int.from_bytes(data[24:28], endian),
        int.from_bytes(data[34:36], endian),
        int.from_bytes(data[40:44], endian)
    ) if is_legit_wav_hdr(data) else "NO"
)
