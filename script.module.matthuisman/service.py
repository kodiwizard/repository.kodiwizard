#!/usr/bin/env python2.7
import sys
sys.path.append('lib')

from matthuisman.service import Service

Service().run((60*5))