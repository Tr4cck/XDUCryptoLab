from gmpy2 import invert, gcd, powmod


def factorization(args):
  (n, e, c) = zip(*args)
  p = gcd(n[0], n[1])
  if p != 1:
    q1 = n[0] // p
    q2 = n[1] // p
    phi1 = (p - 1)*(q1 - 1)
    phi2 = (p - 1)*(q2 - 1)
    d1 = invert(e[0], phi1)
    d2 = invert(e[1], phi2)
    m1 = powmod(c[0], d1, n[0])
    m2 = powmod(c[1], d2,n[1])

  return m1, m2
