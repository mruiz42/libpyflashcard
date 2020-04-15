class Statistic:
    def __init__(self):
        self.num_correct = 0
        self.num_attempts = 0

    def __str__(self):
        return "%" + str(self.percentage())

    def percentage(self) -> float:
        if self.num_attempts != 0:
            return float(self.num_correct/self.num_attempts)
        else:
            return float(0.0)
