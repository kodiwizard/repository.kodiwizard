#!/usr/bin/env python2.7
import sys
sys.path.append('lib')

from matthuisman.controller import Controller

if __name__ == '__main__':
    Controller(sys.argv[0], int(sys.argv[1])).run(sys.argv[2])