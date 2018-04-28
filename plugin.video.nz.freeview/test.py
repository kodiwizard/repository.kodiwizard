import os
import sys

BASE_RESOURCE_PATH = os.path.join('.', 'resources', 'lib')
sys.path.append(BASE_RESOURCE_PATH)

from router import Router

if __name__ == '__main__':
    router = Router('')
    router.route('')