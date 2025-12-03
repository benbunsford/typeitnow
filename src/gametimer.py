from threading import Timer


class GameTimer(Timer):
    def __init__(self, interval, function, args):
        super().__init__(interval, function, args)
        self.interval = interval
        self.function = function
        self.starting_interval = interval

    def speed_up(self):
        if self.interval > (self.starting_interval * 0.5):
            self.interval -= (self.starting_interval * 0.05)
