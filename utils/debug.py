import sys
import time


ANSI_FG_BLACK   = "\33[1;30m"
ANSI_FG_RED     = "\33[1;31m"
ANSI_FG_GREEN   = "\33[1;32m"
ANSI_FG_YELLOW  = "\33[1;33m"
ANSI_FG_BLUE    = "\33[1;34m"
ANSI_FG_MAGENTA = "\33[1;35m"
ANSI_FG_CYAN    = "\33[1;36m"
ANSI_FG_WHITE   = "\33[1;37m"
ANSI_BG_BLACK   = "\33[1;40m"
ANSI_BG_RED     = "\33[1;41m"
ANSI_BG_GREEN   = "\33[1;42m"
ANSI_BG_YELLOW  = "\33[1;43m"
ANSI_BG_BLUE    = "\33[1;44m"
ANSI_BG_MAGENTA = "\33[1;35m"
ANSI_BG_CYAN    = "\33[1;46m"
ANSI_BG_WHITE   = "\33[1;47m"
ANSI_NONE       = "\33[0m"


ANSI_FORMAT = lambda s, fmt : fmt + s + ANSI_NONE


def log(*args):
  print(f"{ANSI_FORMAT('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' ' + __file__ + ':' + str(sys._getframe().f_lineno) + ']', ANSI_FG_BLUE)}: ", *args)


if __name__ == '__main__':
  log(f"Hello, {__file__}")
