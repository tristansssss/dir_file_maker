#!/usr/bin/env python
from operator import ne
import os
from maker import Maker

main_dir_path = os.getcwd() + "/"
sizes = [
    "300x250", "300x600", "160x600", "728x90", "300x1050", "970x250"
]

try:
    newmaker = Maker()
    for size in sizes:
        # path, filename
        newmaker.create_file(main_dir_path + "sizes", size + "-2.png")
except Exception as e:
    print(e)
