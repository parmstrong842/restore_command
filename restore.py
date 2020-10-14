#!/usr/bin/env python3

import os
import sys
import shutil

path = os.path.expanduser("~") + "/rm_trash/"
most_recent = ""
with open(path + "path.log") as f:
    for line in f:
        tokens = line.split(" ")
        if tokens[0] == sys.argv[1]:
            most_recent = tokens[1]

if most_recent:
    shutil.move(path + most_recent.rstrip(), sys.argv[1])
