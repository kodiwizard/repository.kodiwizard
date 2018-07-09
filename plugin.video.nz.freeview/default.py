#!/usr/bin/env python2.7
import sys

import resources.lib.config
from resources.lib.controller import Controller

if __name__ == '__main__':
    Controller().route(sys.argv[2])