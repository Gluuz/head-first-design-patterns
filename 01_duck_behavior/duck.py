from abc import ABC, abstractmethod


class Duck(ABC):
    flyBehavior = None
    quackBehavior = None

    def __init__(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.flyBehavior.fly()

    def perform_quack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def set_fly_behavior(self, fly_behavior):
        self.flyBehavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quackBehavior = quack_behavior
