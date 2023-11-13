from abc import ABC, abstractmethod

class Callable(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class DefaultCallback(Callable):
    def __call__(self, *args, **kwargs):
        return False
    
class EarlyStoppingCallback(Callable):
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, *args, **kwargs):
        return args[0] < self.threshold

class EarlyStopping():
    def __init__(self, callback: Callable = DefaultCallback()):
        self.callback = callback

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)