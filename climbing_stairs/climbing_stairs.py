#!/usr/bin/python

import sys

def climbing_stairs(n):
    answer = 1
    prev = 1
    prevPrev = 1
    prevPrevPrev = 0
    for i in range(n - 1):
        answer = prev + prevPrev + prevPrevPrev
        prevPrevPrev = prevPrev
        prevPrev = prev
        prev = answer
    return answer

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')