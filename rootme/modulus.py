from gmpy2 import invert , powmod
from utils.debug import log


def common_modulus(args):
  (n1, e1, c1), (n2, e2, c2) = args
  assert n1 == n2, log("n1 must be equal to n2")
  r = invert(e1 , e2)
  s = (r * e1 - 1) // e2
  c2 = invert(c2 , n1) # avoid minus
  ans = (powmod(c1 , r , n1) * powmod(c2 , s , n1)) % n1
  return [ans]
