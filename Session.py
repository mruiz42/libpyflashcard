from datetime import *
class Session:
    def __init__(self, start_time: datetime = datetime(0, 0, 0, 0, 0, 0, 0),
                 end_time: datetime = datetime(0, 0, 0, 0, 0, 0, 0), session: int = 0):
        self.start_time = start_time
        self.end_time = end_time
        self.session = session
