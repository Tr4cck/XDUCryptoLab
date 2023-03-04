from gmpy2 import invert , powmod , is_prime , gcd , next_prime


def core_d(n):
    a = 2
    f = a
    while True:
      for i in range(1, 200000):
        f = powmod(f, i, n)
        if is_prime(i):
          d = gcd(f-1, n)
          if 1 < d < n:
            return d
          elif d >= n:
            f = next_prime(a)
            break
      else:
        break


def pmo_attack(args):
  (n, e, c) = zip(*args)
  ans = []
  for i in range(len(n)):
    p = core_d(n[i])
    q = n[i] // p
    phi = (p-1) * (q-1)
    d = invert(e[i], phi)
    m = powmod(c[i], d, n[i])
    ans.append(m)

  return ans