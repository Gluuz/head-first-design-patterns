from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass
