#!/usr/bin/env Python3

from __future__ import print_function
from collections import OrderedDict
from time import sleep, strftime


def meminfo():
    ''' Return the informationin /proc/meminfo
    asa dictionary '''
    meminfo = OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__ == '__main__':
    # print(meminfo())
    meminfo = meminfo()
    while True:
        sleep(10)
        print(strftime("%Y-%m-%d %H:%M:%S"))
        print('Total memory:{0}' + str(int(format(meminfo['MemTotal'])[:-2]) /
                                       1024 / 1024)[0:5] + 'G')
        print('Free memory: {0}' + str(int(format(meminfo['MemFree'])[:-2]) /
                                       1024 / 1014)[0:5] + 'G')
