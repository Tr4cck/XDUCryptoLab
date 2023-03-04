from gmpy2 import iroot,invert,powmod

def fermat_decompose(args):
  n , e , c = args[0]
  x = iroot(n , 2)[0] + 1
  while not iroot(x**2 - n, 2)[1]:
    x += 1
  
  y = iroot(x**2 - n, 2)[0]
  p = (x + y)
  q = (x - y)
  phi = (p-1) * (q-1)
  d = invert(e, phi)
  m = powmod(c, d, n)
  return [m]