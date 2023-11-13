from abc import ABC, abstractmethod

class Scaler(ABC):
    @abstractmethod
    def transform(self, x):
        pass

    @abstractmethod
    def fit(self, x):
        pass

    def transform_fit(self, x):
        self.fit(x)
        return self.transform(x)

class MinMaxScaler(Scaler):
    def fit(self, x):
        self.min = min(x)
        self.max = max(x)

    def transform(self, x):
        return [(v - self.min) / (self.max - self.min) for v in x]

class MaxAbsScaler(Scaler):
    def fit(self, x):
        self.max = max([abs(v) for v in x])

    def transform(self, x):
        return [v / self.max for v in x]