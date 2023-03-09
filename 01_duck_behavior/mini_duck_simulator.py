from mallard_duck import MallardDuck
from model_duck import ModelDuck
from fly_rocket_powered import FlyRocketPowered

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

    # to change a duck's behavior at runtime
    # just call the duck's setter method for that behavior
    model = ModelDuck()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()
