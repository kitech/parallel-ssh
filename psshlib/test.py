#!/usr/bin/env python

import sys
import os

os.write(sys.stdout.fileno(), 'hello')

# vim: et sw=4 sts=4
