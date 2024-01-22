#!/usr/bin/python3
start, end = 97, 122
while start < end :
    if start == 101 or start == 113:
        start += 1
    else:
        print("{}".format(chr(start)), end="")
    start += 1
