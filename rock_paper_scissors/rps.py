#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    outcomes = []
    def recurse(rounds, played):
        if rounds == 0:
            outcomes.append(played)
            return
        for i in range(len(plays)):
            recurse(rounds - 1, played.append(plays[i]))
    recurse(n, [])
    return outcomes            

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python rps.py [n]` with different n values
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')