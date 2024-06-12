class RecentCounter:

    def __init__(self):
        self.requests = []
        self.left = 0
        self.length = 0

    def ping(self, t: int) -> int:
        if t:
            self.length += 1
            self.requests.append(t)
            while self.requests[self.left] < t - 3000:
                self.left += 1
            return self.length - self.left
        else:
            return None


obj = RecentCounter()
param_1 = obj.ping(1)
print(param_1)
param_1 = obj.ping(100)
print(param_1)
param_1 = obj.ping(3001)
print(param_1)
param_1 = obj.ping(3002)
print(param_1)
