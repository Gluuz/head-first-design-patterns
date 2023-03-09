from fly_behavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")
