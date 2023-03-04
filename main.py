import os
from typing import List, Tuple
import binascii

from utils.debug import log

from rootme.modulus import common_modulus
from rootme.lowe    import broadcast_attack
from rootme.factor  import factorization
from rootme.fermat  import fermat_decompose
from rootme.pollard import pmo_attack


WORK_LIST = {
  common_modulus  : (0, 4),
  broadcast_attack: (3, 8, 12, 16, 20),
  factorization   : (1, 18),
  fermat_decompose: (10,),
  pmo_attack      : (2, 6, 19),
  # 🤣 coppersmith   : (7, 9, 11, 13, 14, 15, 17)
}


frame_cnt = len(os.listdir('Frames'))
data: List[Tuple[int, int, int]] = []
for i in range(frame_cnt):
  with open(f"Frames/Frame{i}", 'r') as fin:
    raw_str = fin.read()    
    n, e, c = int(raw_str[:256], 0x10), int(raw_str[256:512], 0x10), int(raw_str[512:], 0x10)
    data.append((n, e, c))


for func, aim in WORK_LIST.items():
  args = [data[i] for i in aim]
  rets = func(args)
  log(f"[*] {func.__name__}({aim}) -> {rets}")
  for ret in rets:
    print(binascii.a2b_hex(hex(ret)[2:])[-8:])
