from threading import Timer
from AcMonitor import AcMonitor

if __name__ == '__main__':
    acm = AcMonitor()
    acm.addresses.add('0xb3f1507591583ebf14b5b31d134d700c83c20fa1')
    acm.start()
    Timer(7, acm.stop).start()

