#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# cpu.load()
# cpu.run()

if len(sys.argv) > 1:
    cpu.load(sys.argv[1])
    cpu.run()
else:
    None