import os
from pip.__main__ import _main as main

error_log = open('error_log.txt', 'w')

def install(package):
    try:
        main(['install'] + [str(package)])
    except Exception as e:
        error_log.write(str(e))

if __name__ == '__main__':
    f = open('requirements.txt', 'r')
    for line in f:
        install(line)
    f.close()
    error_log.close()