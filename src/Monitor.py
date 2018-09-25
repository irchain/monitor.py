from threading import Timer


class Monitor:
    def __init__(self, interval, action, args=None):
        args = args if args is not None else []
        self.listening = False
        self.status = 'pending'
        self.timer = Timer(interval, self.timing, [action, args])

    def start(self):
        if self.listening:
            print('Monitor has been start.')
        else:
            print('Monitor start listening...')
            self.listening = True
            self.status = 'running'
            # start an new thread
            self.timer.start()

    def stop(self):
        if self.listening:
            print('Monitor been closed.')
            self.listening = False
            self.status = 'pending'
            # force stop monitor
            self.timer.cancel()
        else:
            print('Monitor did not start.')

    def timing(self, action, args):
        print('loop...')
        action(*args)
        if self.listening:
            # loop interval while every x sec
            self.timer.run()
