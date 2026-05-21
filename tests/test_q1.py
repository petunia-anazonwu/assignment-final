import random
from Q1.q1 import solve_q1
def brute_force(arr):
  s=0
  for x in arr:
    s += x
    return s
def test_small()
  assert solve_q1([1,2,3]) == 6
def test_edge_empty():
  assert solve_q1([]) == 0
def test_random_vs_bruteforce():
   for _ in range(50):
     arr = [random.randint(-10,10) for _ in range(20)]
     assert solve_q1(arr) == brute_force(arr)
