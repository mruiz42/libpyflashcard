from datetime import *
class Session:
    def __init__(self,
                 start_time: datetime = datetime.now(),
                 end_time: datetime = datetime.max,
                 session: int = 0):
        self.start_time = start_time
        self.end_time = end_time
        self.session = session
        self.words_studied = 0
