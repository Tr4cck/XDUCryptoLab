import gmpy2
from functools import reduce
from Crypto.Util.number import long_to_bytes


def CRT(mi, ai):
  M = reduce(lambda x, y: x * y, mi)
  ai_ti_Mi = [a * (M // m) * gmpy2.invert(M // m, m) for (m, a) in zip(mi, ai)]
  return reduce(lambda x, y: x + y, ai_ti_Mi) % M


def broadcast_attack(args):
  (n, e, c) = zip(*args)
  assert len(set(e)) == 1
  e = e[0]
  m = CRT(n, c)
  tmp = gmpy2.iroot(m, e)
  if tmp[1]: # root completely
    return [tmp[0]]
