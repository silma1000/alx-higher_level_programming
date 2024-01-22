#!/usr/bin/python3
start, end = 97, 123
while start < end:
    if start == 101 or start == 113:
        start
    else:
        print("{}".format(chr(start)), end="")
    start += 1
