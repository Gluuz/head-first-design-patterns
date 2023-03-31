from abc import ABC, abstractmethod


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass
