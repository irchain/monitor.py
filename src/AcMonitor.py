from Monitor import Monitor
from DataType import Accounts


class AcMonitor(Monitor):
    def __init__(self):
        super(AcMonitor, self).__init__(1, self.listen_account)
        self.addresses = Accounts()

    def start(self):
        if not self.addresses:
            print('Expected at least 1 address has being monitored.')
        else:
            super(AcMonitor, self).start()

    def listen_account(self):
        print(self.addresses)
