#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  rounds = n
  outcomes = []
  plays = [["rock"], ["paper"], ["scissors"]]
  if n == 0:
    return [[]]
  
  def play(round,rounds):
    if rounds == 0:
      outcomes.append(round)
      return outcomes
    for i in range(0,3):
      play(round + plays[i], rounds - 1)


  play([],rounds)
  return outcomes

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')